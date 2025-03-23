from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox

from goldobot import config
import struct

class SequencesDialog(QDialog):
    def __init__(self, parent = None):
        super(SequencesDialog, self).__init__(None)
        self._combobox_sequence_id = QComboBox()
        
        layout = QGridLayout()        
        layout.addWidget(self._combobox_sequence_id, 1, 0)
        self.setLayout(layout)
        self._update_sequence_names()

    def _update_sequence_names(self):
# FIXME : TODO
        #config_proto = config.robot_config.robot_config

        self._combobox_sequence_id.clear()        
# FIXME : TODO
        #for k in config_proto.sequences_names:
        #    self._combobox_sequence_id.addItem(k)
        
