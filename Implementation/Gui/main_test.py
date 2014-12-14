import sys
import MainUi
from PyQt4.QtGui import *
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainUi.MainUI()
    win.show()
    app.exec_()
    sys.exit()
