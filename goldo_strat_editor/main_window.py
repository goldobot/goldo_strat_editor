import sys
import signal
import math
import struct
import config

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

dialogs = [
    ("Test sequences", SequencesDialog)
 ]

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

        self.setCentralWidget(self._main_widget)

        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        # FIXME : TODO
        #left_layout.addWidget(self._widget_robot_status)

        table_layout = QVBoxLayout()
        table_layout.addWidget(self._table_view)
        table_layout.addStretch(1)
        
        self._widget_goldo1 = Goldo1(None, table_view=self._table_view, parent=self)
        self._table_view._scene.dbg_mouse_info.connect(self._widget_goldo1._update_mouse_dbg)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(table_layout)
        main_layout.addWidget(self._widget_goldo1)

        self._main_widget.setLayout(main_layout)

        # FIXME : TODO
        #self._action_upload_config.triggered.connect(self._upload_config)


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

