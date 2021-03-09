from PyQt5.QtCore import QDate, QTime, Qt, QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database import MyCursor
from deleted_accs_history import *
import sys
from login import Ui_MainWindow


class DeleteAcc(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(DeleteAcc, self).__init__()
        self.setupUi(self)
        self.show()
        self.time = self.findChild(QLabel, "l_timer")
        self.date = self.findChild(QLabel, "l_date")
        self.line_ed_pass = self.findChild(QLineEdit, "line_edit_pass")
        self.b_log = self.findChild(QPushButton, "b_login")
        self.wrong1 = self.findChild(QLabel, "wrong_pass")
        self.combo = self.findChild(QComboBox, "list_colabs")
        self.setWindowIcon(QIcon('MJDB_ICON.ico'))
        now = QDate.currentDate()
        self.date.setText(now.toString(Qt.ISODate))

        self.setWindowModality(Qt.ApplicationModal)

        timer = QTimer(self)
        timer.timeout.connect(self.displaytime)
        timer.start(1000)

        m = MyCursor()
        m.mycursor.execute("SELECT firstName FROM User WHERE firstName='Jamal'")

        for x in m.mycursor.fetchall():
            self.combo.addItems(x)

    def displaytime(self):
        time = QTime.currentTime()
        self.time.setText(time.toString(Qt.DefaultLocaleLongDate))


class DeletedAccs(QtWidgets.QMainWindow, Ui_add_acc):
    def __init__(self):
        super(DeletedAccs, self).__init__()
        self.setupUi(self)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)

        self.close_btn.clicked.connect(lambda: self.close())
        self.mini.clicked.connect(lambda: self.showMinimized())

        now = QDate.currentDate()
        self.date.setText(now.toString(Qt.ISODate))
        timer = QTimer(self)
        timer.timeout.connect(self.displaytime)
        timer.start(1000)

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title_bar.mouseMoveEvent = moveWindow

        self.m = MyCursor()
        self.m.mycursor.execute("""SELECT created, user, name, soldeAcc, soldeGen, description FROM DeletedAccs""")
        f = self.m.mycursor.fetchall()
        self.list_acc.setRowCount(0)
        for column_number, row_data in enumerate(f):
            self.list_acc.insertRow(column_number)
            for row_number, data in enumerate(row_data):
                self.list_acc.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
        for x in range(self.list_acc.rowCount()):
            g = float(self.list_acc.item(x, 3).text())
            y = float(self.list_acc.item(x, 4).text())
            if g < 0:
                formatted_float_debit = "{:,.2f}".format(g)
                self.list_acc.setItem(x, 3, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH')))
                self.list_acc.item(x, 3).setForeground(QtGui.QColor(255, 0, 0))
            if g > 0:
                formatted_float_debit = "{:,.2f}".format(g)
                self.list_acc.setItem(x, 3, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH')))
                self.list_acc.item(x, 3).setForeground(QtGui.QColor(0, 170, 0))
            if y > 0:
                formatted_float_debit1 = "{:,.2f}".format(y)
                self.list_acc.setItem(x, 4, QtWidgets.QTableWidgetItem(str(formatted_float_debit1 + ' DH')))
                self.list_acc.item(x, 4).setForeground(QtGui.QColor(0, 170, 0))
            elif y < 0:
                formatted_float_debit1 = "{:,.2f}".format(y)
                self.list_acc.setItem(x, 4, QtWidgets.QTableWidgetItem(str(formatted_float_debit1 + ' DH')))
                self.list_acc.item(x, 4).setForeground(QtGui.QColor(255, 0, 0))
            if g == 0 or y == 0:
                formatted_float_debit = "{:,.2f}".format(g)
                formatted_float_debit1 = "{:,.2f}".format(y)
                self.list_acc.setItem(x, 3, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH')))
                self.list_acc.item(x, 3).setForeground(QtGui.QColor(0, 0, 0))
                self.list_acc.setItem(x, 4, QtWidgets.QTableWidgetItem(str(formatted_float_debit1 + ' DH')))
                self.list_acc.item(x, 4).setForeground(QtGui.QColor(0, 0, 0))

    def displaytime(self):
        time = QTime.currentTime()
        self.time.setText(time.toString(Qt.DefaultLocaleLongDate))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = DeleteAcc()
    window.show()
    sys.exit(app.exec())
