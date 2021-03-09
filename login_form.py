__author__ = "Farouk BEL KHYATE"
__copyright__ = "Copyright (C) 2020 FAROUK BEL KHYATE"
__license__ = "MJDB ESK2 S.A.R.L"
__version__ = "1.0"

from PyQt5.QtCore import QDate, QTime, Qt, QTimer, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Statistics import MainWindow
from database import MyCursor
import sys
from login import Ui_MainWindow
from sign import Ui_edit_colab as Sign_Ui
from loadingScreen import *

# GLOBALS
counter = 0


class loadingScreen(QMainWindow, Ui_deleted_accs):
    def __init__(self, parent=None):
        super(loadingScreen, self).__init__()

        self.setupUi(self)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowIcon(QIcon('MJDB_ICON.ico'))
        self.shadow = QGraphicsDropShadowEffect()
        self.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.timer.singleShot(1500, lambda: self.label_4.setText('Chargement de base de donnés...'))
        self.timer.singleShot(3500, lambda: self.label_4.setText("Chargement de l'interface..."))

        self.l_ = LoginForm()

    def progress(self):
        global counter
        self.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.l_.show()
            self.close()
        counter += 1


class LoginForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(LoginForm, self).__init__()
        self.parent = parent
        self.setupUi(self)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowTitle('Login')
        self.setWindowIcon(QIcon('MJDB_ICON.ico'))

        self.time = self.findChild(QLabel, "l_timer")
        self.date = self.findChild(QLabel, "l_date")
        self.line_ed_pass = self.findChild(QLineEdit, "line_edit_pass")
        self.b_log = self.findChild(QPushButton, "b_login")
        self.wrong = self.findChild(QLabel, "wrong_pass")
        self.combo = self.findChild(QComboBox, "list_colabs")

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title_bar.mouseMoveEvent = moveWindow

        now = QDate.currentDate()
        self.date.setText(now.toString(Qt.ISODate))
        self.close_btn.clicked.connect(lambda: self.close())
        self.mini.clicked.connect(lambda: self.showMinimized())
        self.b_log.clicked.connect(self.clicked)
        self.sign_in.clicked.connect(self.sign_in_clicked)

        timer = QTimer(self)
        timer.timeout.connect(self.displaytime)
        timer.start(1000)

        m = MyCursor()
        m.mycursor.execute('SELECT firstName FROM User')

        for x in m.mycursor.fetchall():
            self.combo.addItems(x)
        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.b_log.animateClick()

    def update_clicked(self):
        if self.s.wrong.text() == 'Inscription effectuée avec succès!':
            self.combo.clear()
            m = MyCursor()
            m.mycursor.execute('SELECT firstName FROM User')

            for x in m.mycursor.fetchall():
                self.combo.addItems(x)
            self.s.close()
        else:
            pass

    def sign_in_clicked(self):
        self.s = SignInForm()
        self.s.show()
        self.s.sign.clicked.connect(self.update_clicked)

    def displaytime(self):
        time = QTime.currentTime()
        self.time.setText(time.toString(Qt.DefaultLocaleLongDate))

    def clicked(self):
        password = self.line_ed_pass.text()
        combo_text = str(self.combo.currentText())
        m = MyCursor()
        m.mycursor.execute("SELECT * FROM User WHERE firstName=%s and password=%s", (combo_text, password))
        if len(m.mycursor.fetchall()) > 0:

            self.wrong.setText("")
            p = MainWindow()
            p.user.setText(self.combo.currentText())
            if self.combo.currentText() != 'Jamal':
                p.add_colab.setEnabled(False)
            p.show()

        elif password == '':
            self.wrong.setText("Entrer un password")
        else:
            self.wrong.setText("Password incorrect")
            self.line_ed_pass.setText("")

        self.line_ed_pass.clear()

class SignInForm(QMainWindow, Sign_Ui):
    clicked = pyqtSignal()

    def __init__(self):
        super(SignInForm, self).__init__()

        self.setupUi(self)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowTitle('Inscription')
        self.setWindowIcon(QIcon('MJDB_ICON.ico'))
        self.sign.clicked.connect(self.sign_clicked)

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
    def sign_clicked(self):
        if self.prenom.text() != '' and self.nom.text() != '' and self.password.text() != '':
            o = MyCursor()
            o.mycursor.execute('INSERT INTO User (firstName, lastName, password) VALUES (%s,%s,%s)',
                               (self.prenom.text(), self.nom.text(), self.password.text()))
            o.db.commit()
            self.wrong.setText('Inscription effectuée avec succès!')

        else:
            self.wrong.setText('Veuillez entrer tout vos informations!')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = loadingScreen()
    window.show()
    sys.exit(app.exec())
