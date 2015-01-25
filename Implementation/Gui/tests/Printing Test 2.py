from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle(self.tr('Document Printer'))
        self.editor = QTextEdit(self)
        self.editor.textChanged.connect(self.handleTextChanged)
        self.buttonOpen = QPushButton('Open', self)
        self.buttonOpen.clicked.connect(self.handleOpen)
        self.buttonPrint = QPushButton('Print', self)
        self.buttonPrint.clicked.connect(self.handlePrint)
        self.buttonPreview = QPushButton('Preview', self)
        self.buttonPreview.clicked.connect(self.handlePreview)
        layout = QGridLayout(self)
        layout.addWidget(self.editor, 0, 0, 1, 3)
        layout.addWidget(self.buttonOpen, 1, 0)
        layout.addWidget(self.buttonPrint, 1, 1)
        layout.addWidget(self.buttonPreview, 1, 2)
        self.handleTextChanged()

    def handleOpen(self):
        path = QFileDialog.getOpenFileName(self, self.tr('Open file'), '', self.tr('HTML files (*.html);;Text files (*.txt)'))
        if path != "":
            stream = QFile(path)
            if stream.open(QIODevice.ReadOnly):
                info = QFileInfo(path)
                text = QString(stream.readAll())
                if info.completeSuffix() == 'html':
                    self.editor.setHtml(text)
                else:
                    self.editor.setPlainText(text)
            stream.close()

    def handlePrint(self):
        dialog = QPrintDialog()
        if dialog.exec_() == QDialog.Accepted:
            self.editor.document().print_(dialog.printer())

    def handlePreview(self):
        dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()

    def handlePaintRequest(self, printer):
        self.view.render(QPainter(printer))

    def handleTextChanged(self):
        enable = not self.editor.document().isEmpty()
        self.buttonPrint.setEnabled(enable)
        self.buttonPreview.setEnabled(enable)

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())
