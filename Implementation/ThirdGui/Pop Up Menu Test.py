class PopUpWindow(QMainWindow):
    def __init__(self, title, width, height):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(width, height)
