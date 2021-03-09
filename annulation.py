from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from motif import Ui_efed
from motif_ import Ui_efed as motif_detail
from motif_ops import Ui_efed as rem_ops
from remarque_ops import Ui_efed as rem_entry


class Annulation(QWidget, Ui_efed):
    def __init__(self, parent=None):
        super(Annulation, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle('Motif')
        self.setWindowIcon(QIcon('Untitled-2-01.ico'))
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowModality(Qt.ApplicationModal)

        self.motif = self.findChild(QTextEdit, 'motif')
        self.minimize = self.findChild(QPushButton, 'mini')
        self.title = self.findChild(QFrame, 'title_bar')
        self.val = self.findChild(QPushButton, 'val')
        self.wrong = self.findChild(QLabel, 'wrong')
        self.close_btn = self.findChild(QPushButton, 'close_btn')

        self.minimize.clicked.connect(lambda: self.showMinimized())
        self.close_btn.clicked.connect(lambda: self.close())

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title_bar.mouseMoveEvent = moveWindow
  
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.val.animateClick()


class Motif(QWidget, motif_detail):
    def __init__(self, parent=None):
        super(Motif, self).__init__(parent)

        self.setupUi(self)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        self.motif = self.findChild(QTextEdit, 'motif')
        self.minimize = self.findChild(QPushButton, 'mini')
        self.title = self.findChild(QFrame, 'title_bar')
        self.val = self.findChild(QPushButton, 'val')
        self.close_btn = self.findChild(QPushButton, 'close_btn')

        self.minimize.clicked.connect(lambda: self.showMinimized())
        self.close_btn.clicked.connect(lambda: self.close())

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title_bar.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.val.animateClick()


class MotifOps(QWidget, rem_ops):
    def __init__(self):
        super(MotifOps, self).__init__()
        self.setupUi(self)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        self.close_btn.clicked.connect(lambda: self.close())
        self.mini.clicked.connect(lambda: self.showMinimized())

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title_bar.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


class RemEntry(QWidget, rem_entry):
    def __init__(self):
        super(RemEntry, self).__init__()
        self.setupUi(self)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        self.close_btn.clicked.connect(lambda: self.close())
        self.mini.clicked.connect(lambda: self.showMinimized())

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title_bar.mouseMoveEvent = moveWindow
        self.switch = 0
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.val.animateClick()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MotifOps()
    window.show()

    sys.exit(app.exec())
