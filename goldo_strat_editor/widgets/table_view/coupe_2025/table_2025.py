import math
import os

from PyQt5.QtCore import QObject, pyqtSignal, QSize, QRectF, QPointF, Qt

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

import importlib.resources as pkg_resources

class Table:
    def __init__(self, scene):
        self._scene = scene
        my_buff=pkg_resources.read_binary(__package__, 'table_2025.png')
        test_img_pixmap2 = QPixmap()
        test_img_pixmap2.loadFromData(my_buff)

        self._bg_img = QGraphicsPixmapItem(test_img_pixmap2.scaled(1200,800))
        self._bg_img.setTransform(QTransform(0.5, 0.0, 0.0,  0.0, -0.5, 0.0,   0.0, 0.0, 0.2))
        self._bg_img.setRotation(-90)
        self._bg_img.setPos(0, -1500)


