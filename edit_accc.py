from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from edit_acc import Ui_edit_colab

class EditAcc(QtWidgets.QWidget, Ui_edit_colab):
    def __init__(self):
        super(EditAcc, self).__init__()

        self.setupUi(self)
        self.setWindowTitle('Editeur compte')
        self.pre = self.findChild(QLineEdit, 'nom1')
        self.nom = self.findChild(QTextEdit, 'desc')
        self.setWindowIcon(QIcon('Untitled-2-01.ico'))
        self.btn_edit = self.findChild(QPushButton, 'edit_btn')
        self.wrong1 = self.findChild(QPushButton, 'wrong1')
        self.wrg = self.findChild(QLabel, 'label_4')
