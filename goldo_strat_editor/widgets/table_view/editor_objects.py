from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QObject, pyqtSignal, QSize, QRectF, QPointF, Qt

from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtWidgets import QGraphicsItemGroup 
from PyQt5.QtWidgets import QGraphicsEllipseItem
from PyQt5.QtWidgets import QGraphicsTextItem
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


class EditorObject(QGraphicsItemGroup):
    def __init__(self):
        super().__init__()

        self.move_grab = False
        self.turn_grab = False


    def onMouseMoveTo(self, m_x_mm, m_y_mm):
        self.setPos(m_x_mm, m_y_mm)
        
        
    def onMousePointTo(self, m_x_mm, m_y_mm):
        delta_x_mm = m_x_mm - self.x()
        delta_y_mm = m_y_mm - self.y()
        (r, yaw) = cart2pol(delta_x_mm, delta_y_mm)
        self.setRotation(yaw * 180 / math.pi)


class Arrow(EditorObject):
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


class StratPoint(EditorObject):
    def __init__(self, _label):
        super().__init__()
        
        self._strat_point_circle = QGraphicsEllipseItem( -30, -30, 60, 60 )
        self._strat_point_circle.setPen(QPen())
        self._strat_point_circle.setBrush(QBrush(QColor('yellow')))
        self.addToGroup(self._strat_point_circle)

        self._strat_point_text = QGraphicsTextItem(_label);
        self._strat_point_text.setFont(QFont("System",40))
        self._strat_point_text.setRotation(-90)
        self._strat_point_text.setTransform(QTransform(1.0, 0.0, 0.0,  0.0, -1.0, 0.0,   0.0, 0.0, 1.0))
        self._strat_point_text.setPos( -35, -23 )
        #self._strat_point_text.setDefaultTextColor(QColor('black'))
        self.addToGroup(self._strat_point_text)


class RefPoint(EditorObject):
    def __init__(self, _label):
        super().__init__()
        
        path = QPainterPath()
        path.addPolygon(little_square)
        self._little_square = QGraphicsPathItem(path, self)
        self._little_square.setPen(QPen())
        self._little_square.setBrush(QBrush(QColor('red')))

        self._strat_point_text = QGraphicsTextItem(_label);
        self._strat_point_text.setFont(QFont("System",20))
        self._strat_point_text.setRotation(-90)
        self._strat_point_text.setTransform(QTransform(1.0, 0.0, 0.0,  0.0, -1.0, 0.0,   0.0, 0.0, 1.0))
        self._strat_point_text.setDefaultTextColor(QColor('green'))
        self.addToGroup(self._strat_point_text)
