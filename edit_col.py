from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from edit_colab import Ui_edit_colab


class EditCollab(QtWidgets.QWidget, Ui_edit_colab):
    def __init__(self):
        super(EditCollab, self).__init__()

        self.setupUi(self)
        self.setWindowTitle('Editeur collaborateur')
        self.setWindowIcon(QIcon('Untitled-2-01.ico'))
        self.pre = self.findChild(QLineEdit, 'prenom')
        self.nom = self.findChild(QLineEdit, 'nom')
        self.password_e = self.findChild(QLineEdit, 'password')
        self.btn_edit = self.findChild(QPushButton, 'edit_btn')
        self.wrong1 = self.findChild(QPushButton, 'wrong1')
        self.wrg = self.findChild(QLabel, 'label_4')


if __name__ == '__main__':
    import sys

    app2 = QtWidgets.QApplication(sys.argv)
    window = EditCollab()
    window.show()
    sys.exit(app2.exec())
