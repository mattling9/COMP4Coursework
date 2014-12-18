from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    def __init__(self):
        self.button = QtGui.QPushButton(self)
        self.button.clicked.connect(self.handleButton)
        self.button.setIcon(QtGui.QIcon('troll.png'))
        self.button.setIconSize(QtCore.QSize(300,300))
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)

    def handleButton(self):
        pass


if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
