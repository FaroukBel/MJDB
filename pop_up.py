from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PopupDate import Ui_efed
from datetime import datetime, timedelta


class Date(QWidget, Ui_efed):
    def __init__(self, parent=None, *args, **kwargs):
        super(Date, self).__init__(parent, *args, **kwargs)

        self.setupUi(self)
        self.setWindowTitle('Date')
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowIcon(QIcon('Untitled-2-01.ico'))
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowModality(Qt.ApplicationModal)
        self.minimize = self.findChild(QPushButton, 'mini')
        self.title = self.findChild(QFrame, 'title_bar')
        self.minimize.clicked.connect(lambda: self.showMinimized())
        
        now1 = datetime.now().date()
        self.dateEdit.setDate(now1 - timedelta(1))
        # self.dateEdit.setMinimumDate(now1 - timedelta(6))

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title_bar.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Date()
    window.show()
    sys.exit(app.exec())
