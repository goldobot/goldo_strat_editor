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

arrow_poly = QPolygonF([
            QPointF( 100,   0),
            QPointF(  80,  10),
            QPointF( -10,  10),
            QPointF( -10, -10),
            QPointF(  80, -10),
            ])

little_square = QPolygonF([
            QPointF(  10,  10),
            QPointF( -10,  10),
            QPointF( -10, -10),
            QPointF(  10, -10),
            ])

def cart2pol(x, y):
    rho = math.sqrt(x**2 + y**2)
    phi = math.atan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * math.cos(phi)
    y = rho * math.sin(phi)
    return(x, y)


class Arrow(QGraphicsItemGroup):
    def __init__(self):
        super().__init__()
        
        path = QPainterPath()
        path.addPolygon(arrow_poly)
        
        outline = QGraphicsPathItem(path, self)
        outline.setPen(QPen())
        outline.setBrush(QBrush(QColor('red')))
        
        path = QPainterPath()
        path.addPolygon(little_square)
        self._little_square = QGraphicsPathItem(path, self)
        self._little_square.setPen(QPen())
        self._little_square.setBrush(QBrush(QColor('yellow')))


    def onMouseMoveTo(self, m_x_mm, m_y_mm):
        self.setPos(m_x_mm, m_y_mm)
        
        
    def onMousePointTo(self, m_x_mm, m_y_mm):
        delta_x_mm = m_x_mm - self.x()
        delta_y_mm = m_y_mm - self.y()
        (r, yaw) = cart2pol(delta_x_mm, delta_y_mm)
        self.setRotation(yaw * 180 / math.pi)
