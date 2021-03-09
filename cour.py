from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Cour_D import Ui_efed


class Cour(QWidget, Ui_efed):
    def __init__(self, parent=None):
        super(Cour, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Cour')
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowIcon(QIcon('Untitled-2-01.ico'))
        self.minimize = self.findChild(QPushButton, 'mini')
        self.btn_cls = self.findChild(QPushButton, 'close_btn1')
        self.title = self.findChild(QFrame, 'title_bar')
        self.val = self.findChild(QPushButton, 'val')
        self.cour = self.findChild(QLineEdit, 'l50')
        self.info = self.findChild(QLabel, 'label_3')

        self.minimize.clicked.connect(lambda: self.showMinimized())
        self.btn_cls.clicked.connect(lambda: self.close())
        self.cour.textChanged.connect(self.courChanged)

        self.cour.mousePressEvent = lambda _: self.cour.selectAll()

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title_bar.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def courChanged(self):
        if self.cour.text() == '':
            self.cour.setText('0')
            self.cour.selectAll()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Cour()
    window.show()
    sys.exit(app.exec())
