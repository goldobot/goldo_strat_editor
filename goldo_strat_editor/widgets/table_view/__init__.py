import math
import os

from PyQt5.QtCore import QObject, pyqtSignal, QSize, QRectF, QPointF, Qt, QTimer

from PyQt5.QtWidgets import QLabel

from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtWidgets import QGraphicsItemGroup 
from PyQt5.QtWidgets import QGraphicsEllipseItem
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtWidgets import QGraphicsPathItem 

from PyQt5.QtGui import QPolygonF, QPen, QBrush, QColor, QFont, QTransform
from PyQt5.QtGui import QImage, QImageReader, QPixmap, QPainterPath

from .coupe_2025.table_2025 import Table
from .coupe_2025.robot_2025 import Robot
from .editor_objects import Arrow

import numpy as np
import scipy.interpolate

        
class DebugTrajectory:
    def __init__(self, scene):
        self._scene = scene
        self._traj_segm_l = []
        self._spline_segm_l = []
        self._edit_point_l = []
        self.cur_x = 0
        self.cur_y = 0
        self._edit_mode = False

    def onMousePress(self, x, y):
        """"x, y in mm"""        
        print ("pix:<{},{}>".format(event.x(),event.y()))
        # FIXME : TODO : generic code for coordonate system setting
        #realY = 2200.0*(event.x()-30.0)/660.0  # 2023
        #realX = 3200.0*(event.y()-480.0)/960.0 # 2023
        realY = 3200.0*(event.x()-480.0)/960.0
        realX = 2200.0*(event.y()-30.0)/660.0
        print ("real:<{},{}>".format(realX,realY))
        if self._debug_trajectory._edit_mode:
            self._debug_trajectory.line_to(realX, realY)
            
    def onMouseMove(self, x, y):
        """"x, y in mm"""
        return
        
    def onMouseRelease(self, x, y):
        """"x, y in mm"""
        return


class DebugGraphicsScene(QGraphicsScene):
    dbg_mouse_info = pyqtSignal(float,float,float,float,float)
    def mouseMoveEvent(self, event):
        x_mm = event.scenePos().x()
        y_mm = event.scenePos().y()
        rel_x_mm = x_mm - self.parent()._little_robot_x
        rel_y_mm = y_mm - self.parent()._little_robot_y
        d_mm = math.sqrt(rel_x_mm*rel_x_mm + rel_y_mm*rel_y_mm)
        self.dbg_mouse_info.emit(x_mm, y_mm, rel_x_mm, rel_y_mm, d_mm)
        if (event.buttons() & Qt.LeftButton):
            #self.parent()._little_arrow.onMouseMoveTo(x_mm, y_mm)
            self.parent()._little_robot.onMouseMoveTo(x_mm, y_mm)
        if (event.buttons() & Qt.RightButton):
            #self.parent()._little_arrow.onMousePointTo(x_mm, y_mm)
            self.parent()._little_robot.onMousePointTo(x_mm, y_mm)

    def mousePressEvent(self, event):
        x_mm = event.scenePos().x()
        y_mm = event.scenePos().y()
        realX = round(event.scenePos().x(),1)
        realY = round(event.scenePos().y(),1)
        #print ("pix:<{},{}>".format(event.x(),event.y()))
        #print ("real:<{},{}>".format(realX,realY))
        #print ("({: 5.3f}, {: 5.3f}, 0)".format(realX/1000.0,realY/1000.0))
        if (event.buttons() & Qt.LeftButton):
            #self.parent()._little_arrow.onMouseMoveTo(x_mm, y_mm)
            self.parent()._little_robot.onMouseMoveTo(x_mm, y_mm)
        if (event.buttons() & Qt.RightButton):
            #self.parent()._little_arrow.onMousePointTo(x_mm, y_mm)
            self.parent()._little_robot.onMousePointTo(x_mm, y_mm)
        if self.parent()._debug_trajectory._edit_mode:
            self.parent()._debug_trajectory.line_to(realX, realY)


class TableViewWidget(QGraphicsView):
    g_table_view = None
    g_show_theme = True
    g_debug = True
    g_dbg_plt_sz = 1.2
    g_dbg_pen_sz = 0.8

    def __init__(self, parent = None, ihm_type='pc'):
        super(TableViewWidget, self).__init__(parent)
        if ihm_type=='pc':
            #self.setFixedSize(900,600)
            self.setFixedSize(960,660)
        elif ihm_type=='pc-mini':
            #self.setFixedSize(600,400)
            self.setFixedSize(640,440)
        else:
            #self.setFixedSize(225,150)
            self.setFixedSize(240,165)
        # FIXME : TODO : generic code for coordonate system setting
        #self.setSceneRect(QRectF(-500,-1500,4000,3000)) # 2023
        self.setSceneRect(QRectF(-100,-1600,2200,3200))
        #self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        yellow = QColor.fromCmykF(0,0.25,1,0)
        purple = QColor.fromCmykF(0.5,0.9,0,0.05)
        background = QColor(40,40,40)
        darker = QColor(20,20,20)

        # FIXME : TODO : generic code for coordonate system setting
        #self._scene = DebugGraphicsScene(QRectF(-100,-1600,2200,3200),self) # 2023
        self._scene = DebugGraphicsScene(QRectF(-100,-1100,3200,2200),self)
        
        self._table = Table(self._scene)
        self._bg_img = self._table._bg_img
        self._bg_img.setZValue(-10)
        self.refreshTheme()

        self._little_robot = Robot()
        self._little_robot.setZValue(1)
        
        self._little_arrow = Arrow()
        self._little_arrow.setZValue(1)
        
        self._scene.addItem(self._little_robot)
        if TableViewWidget.g_debug:
            dbg_plt_sz = TableViewWidget.g_dbg_plt_sz
            dbg_pen_sz = TableViewWidget.g_dbg_pen_sz
            self._little_robot_center = self._scene.addEllipse(1000.0 - dbg_plt_sz, -1397.0 - dbg_plt_sz, 2*dbg_plt_sz, 2*dbg_plt_sz, QPen(QBrush(QColor('black')),dbg_pen_sz), QBrush(QColor('yellow')))
            self._little_robot_center.setZValue(100)
            new_p = self._scene.addEllipse(1000.0 - dbg_plt_sz, -1397.0 - dbg_plt_sz, 2*dbg_plt_sz, 2*dbg_plt_sz, QPen(QBrush(QColor('black')),dbg_pen_sz), QBrush(QColor('yellow')))
            new_p.setZValue(100)

        self._scene.addItem(self._little_arrow)

        self._little_arrow.onMouseMoveTo(1000, 0)

        self._fsck_text = self._scene.addText("0", QFont("System",40));
        self.setScene(self._scene)
        
        self._debug_trajectory = DebugTrajectory(self._scene)

        # FIXME : TODO : generic code for coordonate system setting
        #self.rotate(0) # 2023
        self.rotate(90)
        if ihm_type=='pc':
            self.scale(0.3, -0.3)
        elif ihm_type=='pc-mini':
            self.scale(0.2, -0.2)
        else:
            self.scale(0.075, -0.075)

        # FIXME : TODO : generic code for coordonate system setting
        #self._scene.addRect(QRectF(0,-1000,3000,2000)) # 2023
        self._scene.addRect(QRectF(0,-1500,2000,3000))

        self._traj_segm_l = []

        self._little_robot_x = 0
        self._little_robot_y = 0

        self._dbg_x_mm = 0
        self._dbg_y_mm = 0
        self._dbg_l = []
        self._dbg_target_x_mm = 0
        self._dbg_target_y_mm = 0
        self._dbg_target_l = []

        TableViewWidget.g_table_view = self
        
    def refreshTheme(self):
        if TableViewWidget.g_show_theme:
            self._scene.addItem(self._bg_img)
        else:
            self._scene.removeItem(self._bg_img)

    def sizeHint(self):
        return QSize(600,400)

    def debug_set_start(self, _new_x, _new_y):
        self._debug_trajectory.set_start(_new_x, _new_y)        

    def debug_line_to(self, _new_x, _new_y):
        my_segm = self._scene.addLine(self.debug_cur_x, self.debug_cur_y, _new_x, _new_y, QPen(QColor(128,128,128)));
        self._traj_segm_l.append(my_segm)
        self.debug_cur_x = _new_x
        self.debug_cur_y = _new_y

    def debug_clear_lines(self):
        self._debug_trajectory.clear()

    def debug_start_edit(self, _new_x, _new_y):
        self._debug_trajectory.start_edit(_new_x, _new_y)

    def debug_start_edit_rel(self):
        self._debug_trajectory.start_edit(self._little_robot_x, self._little_robot_y)

    def debug_stop_edit(self):
        return self._debug_trajectory.stop_edit()

    def zoomPlus(self):
        self._my_scale = 2.0
        self.scale(self._my_scale, self._my_scale)

    def zoomDef(self):
        self.resetTransform()
        # FIXME : TODO : generic code for coordonate system setting
        #self.rotate(0) # 2023
        self.rotate(90)
        self._my_scale = 0.3
        self.scale(self._my_scale, -self._my_scale)

    def zoomMinus(self):
        self._my_scale = 0.5
        self.scale(self._my_scale, self._my_scale)


