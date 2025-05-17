import sys
import signal
import math
import struct
import config
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
        (dj_dist, dj_prev) = self._goldo_dijkstra.do_dijkstra(dj_src)
        dj_path = self._goldo_dijkstra.get_path(dj_dst)
        print()
        print ("dijkstra_dist:")
        for k in self._goldo_dijkstra.keys:
            print (" k={} : dist[k]={} ; prev[k]={}".format(k,dj_dist[k],dj_prev[k]))
        print()
        print ("dijkstra_path({} -> {}):".format(dj_src, dj_dst))
        path_len = len (dj_path)
        for i in range(0,path_len):
            it = dj_path[i]
            print (" ({} : ({} , {}))".format(it[0], it[1], it[2]))
            if (i!=0) and (i!=(path_len-1)):
                prev_it = dj_path[i-1]
                next_it = dj_path[i+1]
                angle = compute_angle(prev_it, it, next_it)
                print ("  angle = {}".format(angle))
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

