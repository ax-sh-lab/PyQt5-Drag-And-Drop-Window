from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

class DragAndDropWindow(QMainWindow):
    def __init__(self, title='DND'):
        super().__init__()
        self.setAcceptDrops(True)
        self.setFixedSize(170, 170)
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)

        self.default = self.palette()
        self.default.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(self.default)

        self.setWindowTitle(title)

    def dragEnterEvent(self, e):
        e.accept() if e.mimeData().hasUrls() else e.ignore()

        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.green)
        self.setPalette(palette)

    def dropEvent(self, e):
        urls = e.mimeData().urls()
        for i in urls:
            self.processUrls(i)

        self.setPalette(self.default)

    def dragLeaveEvent(self, e):
        self.setPalette(self.default)

    def processUrls(self, i):
    	print(i)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    m = DragAndDropWindow()
    m.show()
    app.exec_()