import PyQt5.QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QFrame, QPushButton, QSpinBox, QSizePolicy
from PyQt5.QtCore import QObject, pyqtSignal, QSize, QRectF, QPointF, Qt, QTimer
from PyQt5.QtWidgets import QTabWidget, QAction, QDialog, QVBoxLayout, QCheckBox
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QComboBox, QMessageBox, QShortcut
from PyQt5.QtGui import QKeySequence

from goldo_strat_editor.widgets.table_view import TableViewWidget


class Goldo1(QWidget):
    def __init__(self, client, parent, table_view, **kwarg):
        super().__init__(**kwarg)

        self._client = client
        self._table_view = table_view
        self._parent = parent

        self.zoomL = QLabel()
        self.zoomL.setText("Zoom")
        self.zoomL.setDisabled(False)

        self.zoomPlusB = QPushButton()
        self.zoomPlusB.setText("+")
        self.zoomPlusB.setDisabled(False)
        self.zoomPlusB.clicked.connect(self._table_view.zoomPlus)

        self.zoomDefB = QPushButton()
        self.zoomDefB.setText("o")
        self.zoomDefB.setDisabled(False)
        self.zoomDefB.clicked.connect(self._table_view.zoomDef)

        self.zoomMinusB = QPushButton()
        self.zoomMinusB.setText("-")
        self.zoomMinusB.setDisabled(False)
        self.zoomMinusB.clicked.connect(self._table_view.zoomMinus)

        self.showThemeC = QCheckBox()
        self.showThemeC.setText("Show Theme")
        self.showThemeC.setDisabled(False)
        self.showThemeC.setChecked(True)
        self.showThemeC.clicked.connect(self._enable_theme_display)

        self.separator1 = QFrame()
        self.separator1.setFrameShape(QFrame.HLine)

        self.posL = QLabel()
        self.posL.setText("Mouse pointer\n absolute & relative \n positions (mm):")
        self.posL.setDisabled(False)

        self.posXL = QLabel()
        self.posXL.setText(" x:")
        self.posXL.setDisabled(False)

        self.posYL = QLabel()
        self.posYL.setText(" y:")
        self.posYL.setDisabled(False)

        self.posXRL = QLabel()
        self.posXRL.setText(" xr:")
        self.posXRL.setDisabled(False)

        self.posYRL = QLabel()
        self.posYRL.setText(" yr:")
        self.posYRL.setDisabled(False)

        self.posDRL = QLabel()
        self.posDRL.setText(" dr:")
        self.posDRL.setDisabled(False)

        self.separator2 = QFrame()
        self.separator2.setFrameShape(QFrame.HLine)

        self.posRobotL = QLabel()
        self.posRobotL.setText("Robot pose (mm & deg):")
        self.posRobotL.setDisabled(False)

        self.posRobotXL = QLabel()
        self.posRobotXL.setText(" x:")
        self.posRobotXL.setDisabled(False)
        self.posRobotX = QLineEdit()
        self.posRobotX.setText("0.0")
        self.posRobotX.setDisabled(False)

        self.posRobotYL = QLabel()
        self.posRobotYL.setText(" y:")
        self.posRobotYL.setDisabled(False)
        self.posRobotY = QLineEdit()
        self.posRobotY.setText("0.0")
        self.posRobotY.setDisabled(False)

        self.posRobotYawL = QLabel()
        self.posRobotYawL.setText(" yaw:")
        self.posRobotYawL.setDisabled(False)
        self.posRobotYaw = QLineEdit()
        self.posRobotYaw.setText("0.0")
        self.posRobotYaw.setDisabled(False)

        self.setRobotPoseB = QPushButton()
        self.setRobotPoseB.setText("Set robot pose")
        self.setRobotPoseB.setDisabled(False)
        self.setRobotPoseB.clicked.connect(self._set_robot_pose)

        self.separator3 = QFrame()
        self.separator3.setFrameShape(QFrame.HLine)

        self.testDijkstraL = QLabel()
        self.testDijkstraL.setText("Test Dijkstra:")
        self.testDijkstraL.setDisabled(False)

        self.djSrcL = QLabel()
        self.djSrcL.setText(" Start:")
        self.djSrcL.setDisabled(False)
        self.djSrc = QLineEdit()
        self.djSrc.setText("")
        self.djSrc.setDisabled(False)

        self.djDstL = QLabel()
        self.djDstL.setText(" Target:")
        self.djDstL.setDisabled(False)
        self.djDst = QLineEdit()
        self.djDst.setText("")
        self.djDst.setDisabled(False)

        self.getPathDijkstraB = QPushButton()
        self.getPathDijkstraB.setText("Get path")
        self.getPathDijkstraB.setDisabled(False)
        self.getPathDijkstraB.clicked.connect(self._get_path_dijkstra)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.zoomL)
        right_layout.addWidget(self.zoomPlusB)
        right_layout.addWidget(self.zoomDefB)
        right_layout.addWidget(self.zoomMinusB)
        right_layout.addWidget(self.showThemeC)
        right_layout.addWidget(self.separator1)
        right_layout.addWidget(self.posL)
        right_layout.addWidget(self.posXL)
        right_layout.addWidget(self.posYL)
        right_layout.addWidget(self.posXRL)
        right_layout.addWidget(self.posYRL)
        right_layout.addWidget(self.posDRL)
        right_layout.addWidget(self.separator2)
        right_layout.addWidget(self.posRobotL)
        right_layout.addWidget(self.posRobotXL)
        right_layout.addWidget(self.posRobotX)
        right_layout.addWidget(self.posRobotYL)
        right_layout.addWidget(self.posRobotY)
        right_layout.addWidget(self.posRobotYawL)
        right_layout.addWidget(self.posRobotYaw)
        right_layout.addWidget(self.setRobotPoseB)
        right_layout.addWidget(self.separator3)
        right_layout.addWidget(self.testDijkstraL)
        right_layout.addWidget(self.djSrcL)
        right_layout.addWidget(self.djSrc)
        right_layout.addWidget(self.djDstL)
        right_layout.addWidget(self.djDst)
        right_layout.addWidget(self.getPathDijkstraB)
        right_layout.addStretch(16)
        self.setLayout(right_layout)

        self._table_view._scene.dbg_mouse_info.connect(self._update_mouse_dbg)
        self._table_view._scene.dbg_robot_info.connect(self._update_robot_dbg)
        self._table_view._scene.dbg_arrow_info.connect(self._update_arrow_dbg)

    def _enable_theme_display(self):
        TableViewWidget.g_show_theme = self.showThemeC.isChecked()
        self._table_view.refreshTheme()

    def _update_mouse_dbg(self, x_mm, y_mm, rel_x_mm, rel_y_mm, d_mm):
        self.posXL.setText(" x: {:>6.1f}".format(x_mm))
        self.posYL.setText(" y: {:>6.1f}".format(y_mm))
        self.posXRL.setText(" xr: {:>6.1f}".format(rel_x_mm))
        self.posYRL.setText(" yr: {:>6.1f}".format(rel_y_mm))
        self.posDRL.setText(" dr: {:>6.1f}".format(d_mm))

    def _update_robot_dbg(self, x_mm, y_mm, yaw_deg):
        self.posRobotX.setText("{:>6.1f}".format(x_mm))
        self.posRobotY.setText("{:>6.1f}".format(y_mm))
        self.posRobotYaw.setText("{:>4.1f}".format(yaw_deg))

    def _update_arrow_dbg(self, x_mm, y_mm, yaw_deg):
        self._parent._arrow_x = x_mm / 1000.0
        self._parent._arrow_y = y_mm / 1000.0

    def _set_robot_pose(self):
        x_mm = float(self.posRobotX.text())
        y_mm = float(self.posRobotY.text())
        yaw_deg = float(self.posRobotYaw.text())
        print (" Set robot pose : ({}, {}, {})".format(x_mm, y_mm, yaw_deg))
        self._table_view.setRobotPose(x_mm, y_mm, yaw_deg)

    def _get_path_dijkstra(self):
        dj_src_text = self.djSrc.text()
        if ("robot" in dj_src_text) or (dj_src_text.strip(' ') == ""):
            x = float(self.posRobotX.text()) / 1000.0
            y = float(self.posRobotY.text()) / 1000.0
            self._parent._robot_x = x
            self._parent._robot_y = y
            dj_src = self._parent._get_nearest_dijkstra(x,y)
        else:
            dj_src = int(dj_src_text)
        dj_dst = int(self.djDst.text())
        print (" Test Dijkstra : dj_src = {}, dj_dst = {})".format(dj_src, dj_dst))
        self._parent._get_path_dijkstra(dj_src, dj_dst)

