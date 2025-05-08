import PyQt5.QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QFrame, QPushButton, QSpinBox, QSizePolicy
from PyQt5.QtCore import QObject, pyqtSignal, QSize, QRectF, QPointF, Qt, QTimer
from PyQt5.QtWidgets import QTabWidget, QAction, QDialog, QVBoxLayout, QCheckBox
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QComboBox, QMessageBox, QShortcut
from PyQt5.QtGui import QKeySequence

from goldo_strat_editor.widgets.table_view import TableViewWidget

class Goldo1(QWidget):
    def __init__(self, client, table_view, **kwarg):
        super().__init__(**kwarg)

        self._client = client
        self._table_view = table_view

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

        self.posL = QLabel()
        self.posL.setText("Pos & dist (mm):")
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

        self.posRobotXL = QLabel()
        self.posRobotXL.setText(" robot.x (mm):")
        self.posRobotXL.setDisabled(False)
        self.posRobotX = QLineEdit()
        self.posRobotX.setText("0.0")
        self.posRobotX.setDisabled(False)

        self.posRobotYL = QLabel()
        self.posRobotYL.setText(" robot.y (mm):")
        self.posRobotYL.setDisabled(False)
        self.posRobotY = QLineEdit()
        self.posRobotY.setText("0.0")
        self.posRobotY.setDisabled(False)

        self.posRobotYawL = QLabel()
        self.posRobotYawL.setText(" robot.yaw (deg):")
        self.posRobotYawL.setDisabled(False)
        self.posRobotYaw = QLineEdit()
        self.posRobotYaw.setText("0.0")
        self.posRobotYaw.setDisabled(False)

        self.setRobotPoseB = QPushButton()
        self.setRobotPoseB.setText("Set robot pose")
        self.setRobotPoseB.setDisabled(False)
        self.setRobotPoseB.clicked.connect(self._set_robot_pose)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.zoomL)
        right_layout.addWidget(self.zoomPlusB)
        right_layout.addWidget(self.zoomDefB)
        right_layout.addWidget(self.zoomMinusB)
        right_layout.addWidget(self.showThemeC)
        right_layout.addWidget(self.posL)
        right_layout.addWidget(self.posXL)
        right_layout.addWidget(self.posYL)
        right_layout.addWidget(self.posXRL)
        right_layout.addWidget(self.posYRL)
        right_layout.addWidget(self.posDRL)
        right_layout.addWidget(self.posRobotXL)
        right_layout.addWidget(self.posRobotX)
        right_layout.addWidget(self.posRobotYL)
        right_layout.addWidget(self.posRobotY)
        right_layout.addWidget(self.posRobotYawL)
        right_layout.addWidget(self.posRobotYaw)
        right_layout.addWidget(self.setRobotPoseB)
        right_layout.addStretch(16)
        self.setLayout(right_layout)

        self._table_view._scene.dbg_mouse_info.connect(self._update_mouse_dbg)
        self._table_view._scene.dbg_robot_info.connect(self._update_robot_dbg)

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

    def _set_robot_pose(self):
        x_mm = float(self.posRobotX.text())
        y_mm = float(self.posRobotY.text())
        yaw_deg = float(self.posRobotYaw.text())
        print ("Set robot pose : ({}, {}, {})".format(x_mm, y_mm, yaw_deg))
        self._table_view.setRobotPose(x_mm, y_mm, yaw_deg)
