import sys
import signal

from optparse import OptionParser
from goldo_strat_editor.main_window import MainWindow

import PyQt5.QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    parser = OptionParser()
    #parser.add_option('--robot-ip', default='192.168.1.222')
    parser.add_option('--config-path', default='petit_robot')
    (options, args) = parser.parse_args(sys.argv)
        
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    

    main_window = MainWindow(options)
    main_window.show()

    # Ensure that the application quits using CTRL-C
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    sys.exit(app.exec_())
