from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QObject, pyqtSignal, QSize, QRectF, QPointF, Qt

from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtWidgets import QGraphicsItemGroup 
from PyQt5.QtWidgets import QGraphicsEllipseItem
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtWidgets import QGraphicsPathItem 

from PyQt5.QtGui import QPolygonF, QPen, QBrush, QColor, QFont, QTransform
from PyQt5.QtGui import QImage, QImageReader, QPixmap, QPainterPath

import math

little_robot_poly = QPolygonF([
            QPointF(  50,   0),
            QPointF( 100,  85),
            QPointF(  65, 115),
            QPointF( -65, 115),
            QPointF(-100,  85),
            QPointF(-100, -85),
            QPointF( -65,-115),
            QPointF(  65,-115),
            QPointF( 100, -85)
            ])
            
near_poly = QPolygonF([
            QPointF(  10, 10),
            QPointF(  10, -10),
            QPointF(  30, -30),
            QPointF(  30, 30),
            QPointF(  10, 10),            
            ])
            
far_poly = QPolygonF([
            QPointF(  30, 30),
            QPointF(  30, -30),
            QPointF(  50, -50),
            QPointF(  50, 50),
            QPointF(  30, 30),            
            ])


class Robot(QGraphicsItemGroup):
    def __init__(self):
        super().__init__()
        
        path = QPainterPath()
        path.addPolygon(little_robot_poly)
        #p = little_robot_poly[0}
        #path.moveTo(p.x * 1000, p.y * 1000)
        
        outline = QGraphicsPathItem(path, self)
        outline.setPen(QPen())
        outline.setBrush(QBrush(QColor('red')))
        
        path = QPainterPath()
        path.addPolygon(near_poly)
        self._near_front = QGraphicsPathItem(path, self)
        self._near_front.setPen(QPen())
        self._near_front.setBrush(QBrush(QColor('green')))
        
        path = QPainterPath()
        path.addPolygon(far_poly)
        self._far_front = QGraphicsPathItem(path, self)
        self._far_front.setPen(QPen())
        self._far_front.setBrush(QBrush(QColor('green')))
        
        path = QPainterPath()
        path.addPolygon(near_poly)
        self._near_back = QGraphicsPathItem(path, self)
        self._near_back.setPen(QPen())
        self._near_back.setBrush(QBrush(QColor('green')))
        self._near_back.setRotation(180)
        
        path = QPainterPath()
        path.addPolygon(far_poly)
        self._far_back = QGraphicsPathItem(path, self)
        self._far_back.setPen(QPen())
        self._far_back.setBrush(QBrush(QColor('green')))
        self._far_back.setRotation(180)
        
    def onTelemetry(self, msg):
        self.setPos(msg.pose.position.x * 1000, msg.pose.position.y * 1000)
        self.setRotation(msg.pose.yaw * 180 / math.pi)
