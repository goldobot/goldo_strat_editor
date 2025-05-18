import sys
import signal
import math
import struct
import config
import copy
import numpy as np

from optparse import OptionParser

import PyQt5.QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QFrame, QPushButton, QSpinBox, QSizePolicy
from PyQt5.QtCore import QObject, pyqtSignal, QSize, QRectF, QPointF, Qt, QTimer
from PyQt5.QtWidgets import QTabWidget, QAction, QDialog, QVBoxLayout, QCheckBox
from PyQt5.QtWidgets import  QHBoxLayout, QComboBox, QMessageBox, QShortcut
from PyQt5.QtGui import QKeySequence

from goldo_strat_editor.widgets.table_view import TableViewWidget

from goldo_strat_editor.widgets.goldo_1 import Goldo1

from goldo_strat_editor.dialogs.sequences import SequencesDialog

from goldobot import config

import goldo_strat_editor.dialogs as _dialogs

from experimental.test_importlib import import_positions, get_start_poses, get_preprise_poses, get_predepose_poses, get_resource_poses, get_global_positions

from experimental.test_dijkstra import GoldoDijkstra

dialogs = [
    ("Test sequences", SequencesDialog)
 ]

def compute_dist(p0, p1):
    delta_x = p1[1] - p0[1]
    delta_y = p1[2] - p0[2]
    return np.sqrt(delta_x*delta_x + delta_y*delta_y)

def compute_angle(p0, p1, p2):
    delta_x0 = p1[1] - p0[1]
    delta_y0 = p1[2] - p0[2]
    delta_x1 = p1[1] - p2[1]
    delta_y1 = p1[2] - p2[2]

    dot_prod = delta_x0*delta_x1 + delta_y0*delta_y1
    mod_v0   = np.sqrt(delta_x0*delta_x0 + delta_y0*delta_y0)
    mod_v1   = np.sqrt(delta_x1*delta_x1 + delta_y1*delta_y1)

    return 180.0*(np.arccos(dot_prod/(mod_v0*mod_v1))/np.pi)

class MenuHelper:
    def __init__(self, menu):
        self._actions = []
        self._menu = menu
        
    def addDialog(self, name, dialog):
        action = QAction(name)
        widget = dialog()
        
class MainWindow(QMainWindow):
    def __init__(self, options):
        super().__init__(None)

        # FIXME : TODO
        #config.load_config(options.config_path)
        #cfg = config.robot_config
        #cfg.update_config()        

        # FIXME : DEBUG : EXPERIMENTAL
        import_positions(options.config_path)
        start_poses = get_start_poses()
        #print ("start_poses = {}".format(start_poses))
        preprise_poses = get_preprise_poses()
        #print ("preprise_poses = {}".format(preprise_poses))
        predepose_poses = get_predepose_poses()
        #print ("predepose_poses = {}".format(predepose_poses))
        resource_poses = get_resource_poses()
        print ("resource_poses = {}".format(resource_poses))

        positions = get_global_positions()

        print ()
        print ("DjWayPoint:")
        for k in positions.DjWayPoint:
            print (" k={} : ({} , {})".format(k,positions.DjWayPoint[k][0],positions.DjWayPoint[k][1]))

        print ()
        print ("DjWayPointNet:")
        for it in positions.DjWayPointNet:
            print (" ({} , {})".format(it[0],it[1]))

        self._goldo_dijkstra = GoldoDijkstra(positions.DjWayPoint, positions.DjWayPointNet)
        print()
        print ("GoldoDijkstra:")
        for k in self._goldo_dijkstra.keys:
            print (" k={}".format(k))

        self._robot_x = 0.0
        self._robot_y = 0.0

        self._arrow_x = 0.0
        self._arrow_y = 0.0


        # Create actions

        # FIXME : TODO
        #self._action_upload_config = QAction("Upload config")

        # Add menu
        tools_menu = self.menuBar().addMenu("Tools")

        self._actions = []
        self._dialogs = []

        for d in dialogs:
            action = QAction(d[0])
            widget = d[1]()
            tools_menu.addAction(action)
            self._actions.append(action)
            self._dialogs.append(widget)
            action.triggered.connect(widget.show)

        # FIXME : TODO
        #tools_menu.addAction(self._action_upload_config)

        #self._F5_shortcut = QShortcut(QKeySequence(Qt.Key_F5), self)
        #self._F5_shortcut.activated.connect(self._upload_config)

        self._main_widget = QWidget()
        self._table_view = TableViewWidget(ihm_type=options.ihm_type)

        # FIXME : DEBUG : EXPERIMENTAL
        self._table_view.addStartPoses(start_poses)
        self._table_view.addPreprisePoses(preprise_poses)
        self._table_view.addPredeposePoses(predepose_poses)
        #self._table_view.addRefPoints(resource_poses)
        self._table_view.addWayPointNet(positions.DjWayPoint, positions.DjWayPointNet)

        self.setCentralWidget(self._main_widget)

        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        # FIXME : TODO
        #left_layout.addWidget(self._widget_robot_status)

        table_layout = QVBoxLayout()
        table_layout.addWidget(self._table_view)
        table_layout.addStretch(1)
        
        self._widget_goldo1 = Goldo1(None, parent=self, table_view=self._table_view)
        self._table_view._scene.dbg_mouse_info.connect(self._widget_goldo1._update_mouse_dbg)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(table_layout)
        main_layout.addWidget(self._widget_goldo1)

        self._main_widget.setLayout(main_layout)

        # FIXME : TODO
        #self._action_upload_config.triggered.connect(self._upload_config)

    def _get_path_dijkstra(self, dj_src, dj_dst):
        # FIXME : DEBUG
        #self._goldo_dijkstra.wp_graph[ -70].enabled = False
        #self._goldo_dijkstra.wp_graph[ -40].enabled = False
        #self._goldo_dijkstra.wp_graph[-130].enabled = False
        #self._goldo_dijkstra.wp_graph[-140].enabled = False
        #self._goldo_dijkstra.wp_graph[-220].enabled = False

        # FIXME : DEBUG : EXPERIMENTAL
        if (self._arrow_x>0.0) and (self._arrow_x<2.0) and (self._arrow_y>-1.5) and (self._arrow_y<1.5):
            for k in self._goldo_dijkstra.keys:
                danger_threshold = 0.5
                danger_factor    = 10.0
                p0 = (-1, self._arrow_x, self._arrow_y)
                p1 = (k, self._goldo_dijkstra.wp_graph[k].x, self._goldo_dijkstra.wp_graph[k].y)
                dist = compute_dist(p0, p1)
                if (dist<danger_threshold):
                    extra_cost = danger_factor*(danger_threshold-dist)
                else:
                    extra_cost = 0.0
                self._goldo_dijkstra.wp_graph[k].extra_cost = extra_cost
 
        # FIXME : DEBUG : EXPERIMENTAL
        self._goldo_dijkstra.wp_graph[-220].extra_cost = 20.0
        self._goldo_dijkstra.wp_graph[-210].extra_cost = 20.0
        self._goldo_dijkstra.wp_graph[-200].extra_cost = 20.0
        self._goldo_dijkstra.wp_graph[ 220].extra_cost = 20.0
        self._goldo_dijkstra.wp_graph[ 210].extra_cost = 20.0
        self._goldo_dijkstra.wp_graph[ 200].extra_cost = 20.0
        self._goldo_dijkstra.wp_graph[-21].extra_cost = 10.0
        self._goldo_dijkstra.wp_graph[-20].extra_cost = 10.0
        self._goldo_dijkstra.wp_graph[ 20].extra_cost = 10.0
        self._goldo_dijkstra.wp_graph[-21].extra_cost = 10.0
        self._goldo_dijkstra.wp_graph[1].extra_cost = 0.5
        self._goldo_dijkstra.wp_graph[2].extra_cost = 0.5
        self._goldo_dijkstra.wp_graph[3].extra_cost = 0.5

        (dj_dist, dj_prev) = self._goldo_dijkstra.do_dijkstra(dj_src)
        dj_path = self._goldo_dijkstra.get_path(dj_dst)
        print()
        print ("dijkstra_dist:")
        for k in self._goldo_dijkstra.keys:
            print (" k={} : dist[k]={} ; prev[k]={}".format(k,dj_dist[k],dj_prev[k]))
        print()

        print ("dijkstra_path({} -> {}):".format(dj_src, dj_dst))

        robot_pose = (0, self._robot_x, self._robot_y)
        robot_dist = compute_dist(robot_pose, dj_path[0])
        print ("robot_dist = {}".format(robot_dist))
        if (robot_dist<0.1):
            dj_path[0] = robot_pose
        else:
            dj_path.insert(0,robot_pose)

        print ("First iteration:")
        dj_path_1 = []
        path_len = len (dj_path)
        for i in range(0,path_len):
            it = dj_path[i]
            print (" ({} : ({} , {}))".format(it[0], it[1], it[2]))
            if (i!=0) and (i!=(path_len-1)):
                prev_it = dj_path[i-1]
                next_it = dj_path[i+1]
                angle = compute_angle(prev_it, it, next_it)
                print ("  angle = {}".format(angle))
                if (angle<179.0):
                    dj_path_1.append(it)
            else:
                dj_path_1.append(it)

        print ("Second iteration:")
        dj_supra_path = []
        path_len_1 = len (dj_path_1)
        dj_sub_path = []
        for i in range(0,path_len_1):
            it = dj_path_1[i]
            print (" ({} : ({} , {}))".format(it[0], it[1], it[2]))
            if (i!=0) and (i!=(path_len_1-1)):
                prev_it = dj_path_1[i-1]
                next_it = dj_path_1[i+1]
                angle = compute_angle(prev_it, it, next_it)
                print ("  angle = {}".format(angle))
                if (angle>110.0):
                    dj_sub_path.append(it)
                else:
                    new_subpath = copy.deepcopy(dj_sub_path)
                    dj_supra_path.append(new_subpath)
                    dj_sub_path = [it]
            else:
                dj_sub_path.append(it)
        new_subpath = copy.deepcopy(dj_sub_path)
        dj_supra_path.append(new_subpath)
        dj_sub_path = []

        if (len(dj_supra_path)>1) and (len(dj_supra_path[0])==1) and (compute_dist(robot_pose, dj_supra_path[0][0])<0.1):
            del(dj_supra_path[0])

        print ("dj_supra_path = {}".format(dj_supra_path))

        self._table_view.addDijkstraPathDebug(dj_path)

    def _get_nearest_dijkstra(self, x, y):
        min_dist = 1e9
        min_k = None
        for k in self._goldo_dijkstra.keys:
            delta_x = self._goldo_dijkstra.wp_graph[k].x - x
            delta_y = self._goldo_dijkstra.wp_graph[k].y - y
            dist = np.sqrt(delta_x*delta_x + delta_y*delta_y)
            if dist < min_dist:
                min_dist = dist
                min_k = k
        return min_k

    # FIXME : TODO
    #def _upload_config(self):
    #    cfg = config.robot_config
    #    cfg.update_config()
    #    #self._table_view.set_strategy(cfg.strategy)
    #    #self._table_view.set_config(cfg)
        
    def _enable_theme_display(self):
        TableViewWidget.g_show_theme = self.showThemeC.isChecked()
        self._table_view.refreshTheme()

    def _update_mouse_dbg(self, x_mm, y_mm, rel_x_mm, rel_y_mm, d_mm):
        self.posXL.setText(" x: {:>6.1f}".format(x_mm))
        self.posYL.setText(" y: {:>6.1f}".format(y_mm))
        self.posXRL.setText(" xr: {:>6.1f}".format(rel_x_mm))
        self.posYRL.setText(" yr: {:>6.1f}".format(rel_y_mm))
        self.posDRL.setText(" dr: {:>6.1f}".format(d_mm))

