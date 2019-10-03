from DragAndDropWindow import DragAndDropWindow
from PyQt5.QtWidgets import QApplication, QLabel, QSizePolicy, QDialog
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPixmap

class DND(DragAndDropWindow):
    def __init__(self):
        super().__init__()
        self.pic = QLabel()
        self.pic.setScaledContents( True );
        self.pic.setSizePolicy( QSizePolicy.Ignored, QSizePolicy.Ignored );
        self.setCentralWidget(self.pic)
        self.oldPos = self.pos()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def processUrls(self, i):
        print(dir(i))
        self.pic.setPixmap(QPixmap(i.toLocalFile()))
        popup = QDialog(self)
        pic = QLabel(popup)
        pic.setScaledContents( True );
        pixmap = QPixmap(i.toLocalFile())
        w = 1000
        h = 1000
        pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio)

        popup.setMinimumWidth(pixmap.width())
        popup.setMinimumHeight(pixmap.height())
        pic.setPixmap(pixmap)
        popup.show()

app = QApplication([])
m = DND()
m.show()
app.exec_()