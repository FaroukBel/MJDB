from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDate, QTime, Qt, QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database import MyCursor
import sys
from datetime import datetime
from delt_acc import DeleteAcc
from edit_accc import EditAcc
from gestion import Ui_add_acc


class AddAcc(QtWidgets.QMainWindow, Ui_add_acc):
    def __init__(self):
        super(AddAcc, self).__init__()

        self.setupUi(self)

        self.setWindowTitle('Gestion des comptes')
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setWindowIcon(QIcon('MJDB_ICON.ico'))

        self.nom = self.findChild(QLineEdit, 'nom')
        self.desc = self.findChild(QTextEdit, "desc")
        self.add = self.findChild(QPushButton, "add")
        self.edit = self.findChild(QPushButton, "edit")
        self.add_sc = self.findChild(QPushButton, "add_sc")
        self.list_acc = self.findChild(QTableWidget, "list_acc")
        self.date = self.findChild(QLabel, "date")
        self.time = self.findChild(QLabel, "time")
        self.delete = self.findChild(QPushButton, "delete_2")
        self.wrong = self.findChild(QLabel, 'wrong')
        self.user = self.findChild(QLabel, 'user')
        self.stack = self.findChild(QStackedWidget, 'stack')
        self.list_sacc = self.findChild(QTableWidget, 'list_acc_2')
        self.sc_nom = self.findChild(QLineEdit, 'nom_2')
        self.desc_sc = self.findChild(QTextEdit, 'desc_2')
        self.add_sc_btn = self.findChild(QPushButton, 'add_2')
        self.edit_sc = self.findChild(QPushButton, 'edit_2')
        self.delete_sc = self.findChild(QPushButton, 'delete_3')
        self.mini = self.findChild(QPushButton, 'mini')
        self.close_btn = self.findChild(QPushButton, 'close_btn')
        self.back_c = self.findChild(QPushButton, 'back')
        self.wrong_sc = self.findChild(QLabel, 'wrong_2')
        self.selected = self.findChild(QLabel, 'selcted_acc')
        self.title_bar = self.findChild(QFrame, 'title_bar')

        self.add.clicked.connect(self.clicked_add)
        self.delete.clicked.connect(self.clicked_delete)
        self.add_sc.clicked.connect(self.clicked_add_sc_)
        self.edit.clicked.connect(self.edit_coll)
        self.close_btn.clicked.connect(lambda: self.close())
        self.mini.clicked.connect(lambda: self.showMinimized())
        self.back_c.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.add_sc_btn.clicked.connect(self.clicked_add_sc)
        self.delete_sc.clicked.connect(self.clicked_delete_sc)
        self.edit_sc.clicked.connect(self.edit_coll_sc)

        now = QDate.currentDate()
        self.date.setText(now.toString(Qt.ISODate))
        timer = QTimer(self)
        timer.timeout.connect(self.displaytime)
        timer.start(1000)

        db1 = MyCursor()
        se = db1.mycursor.execute('SELECT created, name, description FROM Accounts')
        f = db1.mycursor.fetchall()
        self.list_acc.setRowCount(0)
        for column_number, row_data in enumerate(f):
            self.list_acc.insertRow(column_number)
            for row_number, data in enumerate(row_data):
                self.list_acc.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
        self.list_acc.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.list_acc.cellClicked.connect(self.cell_changed_acc)

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title_bar.mouseMoveEvent = moveWindow

    #################################################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def cell_changed_acc(self):
        rows = self.list_acc.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi1 = self.list_acc.item(row, 1)
        self.selected.setText(self.twi1.text())

    def clicked_delete_sc(self):
        rows = self.list_sacc.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.tw = self.list_sacc.item(row, 2)
            self.s = DeleteAcc()
            self.s.b_log.clicked.connect(self.clicked_confirm_sc)
            self.s.show()
            self.wrong_sc.setText('')
        else:
            self.wrong_sc.setText('Selectionnez un compte')

    def clicked_confirm_sc(self):
        self.password = self.s.line_ed_pass.text()
        self.combo = self.s.combo.currentText()
        m = MyCursor()
        m.mycursor.execute("SELECT * FROM User WHERE password=%s", (self.password,))
        if self.combo == 'Jamal' and len(m.mycursor.fetchall()) > 0:
            query_1 = "DELETE FROM Ops WHERE acc=%s and opID=%s"
            query_ = "DELETE FROM SAccounts WHERE name=%s and accountID=%s"

            m = MyCursor()
            m.mycursor.execute(query_1, (self.selected.text(), self.tw.text(),))
            m.mycursor.execute(query_, (self.selected.text(), self.tw.text(),))
            m.db.commit()

            m = MyCursor()
            m.mycursor.execute('SELECT accountID, created, name, description FROM SAccounts WHERE accountID=%s',
                               (self.selected.text(),))
            f = m.mycursor.fetchall()
            self.list_sacc.setRowCount(0)
            for column_number, row_data in enumerate(f):
                self.list_sacc.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    self.list_sacc.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
            self.s.close()

        elif self.combo != "Jamal" and len(m.mycursor.fetchall()) > 0:
            self.s.wrong1.setText("Vous n'etes pas un adminstrateur!")
            self.s.line_ed_pass.setText("")

        elif self.password == '':
            self.s.wrong1.setText("Entrer un password")
        else:
            self.s.wrong1.setText("Password incorrect!")
            self.s.line_ed_pass.setText("")

    def edit_coll_sc(self):
        rows = self.list_sacc.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi0 = self.list_sacc.item(row, 0)
                self.twi1 = self.list_sacc.item(row, 2)
                self.twi2 = self.list_sacc.item(row, 3)
            self.e = EditAcc()
            self.e.pre.setText(self.twi1.text())
            self.e.nom.setText(self.twi2.text())
            self.e.wrong1.clicked.connect(self.update_db_sc)
            self.e.show()
        else:
            self.wrong_sc.setText('Selectionnez un compte')

    def update_db_sc(self):

        updt_pre = self.e.pre.text()
        updt_nom = self.e.nom.toPlainText()

        def edit():
            m = MyCursor()
            uptade_query = "UPDATE SAccounts SET name=%s  WHERE  name=%s "
            uptade_query1 = "UPDATE SAccounts SET  description=%s  WHERE name=%s "
            updt_pre = self.e.pre.text()
            updt_nom = self.e.nom.toPlainText()
            up = (updt_pre, self.twi1.text())
            up1 = (updt_nom, self.twi1.text())

            m.mycursor.execute(uptade_query, up)
            m.mycursor.execute(uptade_query1, up1)

            m.db.commit()
            m = MyCursor()
            m.mycursor.execute('SELECT accountID, created, name, description FROM SAccounts WHERE accountID=%s',
                               (self.twi0.text(),))
            f = m.mycursor.fetchall()
            self.list_sacc.setRowCount(0)
            for column_number, row_data in enumerate(f):
                self.list_sacc.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    self.list_sacc.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))

        if updt_pre != self.twi0.text() and updt_nom != self.twi1.text():
            edit()
            self.e.close()
        elif updt_pre != self.twi0.text() and updt_nom == self.twi1.text():
            edit()
            self.e.close()
        elif updt_pre == self.twi0.text() and updt_nom != self.twi1.text():
            edit()
            self.e.close()

        elif updt_pre == self.twi0.text() and updt_nom == self.twi1.text():
            self.e.wrg.setText("Vous avez entré les memes informations")

    def show_h(self):

        self.acc_id = self.current.text()

        db1 = MyCursor()
        se = db1.mycursor.execute('SELECT accountID, created, name, description FROM SAccounts WHERE accountID=%s',
                                  (self.acc_id,))
        f = db1.mycursor.fetchall()
        self.list_sacc.setRowCount(0)
        for column_number, row_data in enumerate(f):
            self.list_sacc.insertRow(column_number)
            for row_number, data in enumerate(row_data):
                self.list_sacc.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))

    def clicked_add_sc(self):
        nom = self.sc_nom.text()
        desc = self.desc_sc.toPlainText()
        self.id = self.selected.text()
        m = MyCursor()
        m.mycursor.execute("""SELECT name FROM SAccounts WHERE name=%s""", (nom,))

        if nom != '':
            db1 = MyCursor()
            query = "INSERT INTO SAccounts (accountID, created, name, description) VALUES (%s,%s,%s,%s)"
            db1.mycursor.execute(query, (self.id, datetime.now(), nom, desc))
            db1.db.commit()
            self.wrong_sc.clear()

        else:
            self.wrong_sc.setText('Veuillez entrer le nom du compte')

        db1 = MyCursor()
        se = db1.mycursor.execute('SELECT accountID, created, name, description FROM SAccounts WHERE accountID=%s',
                                  (self.id,))
        f = db1.mycursor.fetchall()
        self.list_sacc.setRowCount(0)
        for column_number, row_data in enumerate(f):
            self.list_sacc.insertRow(column_number)
            for row_number, data in enumerate(row_data):
                self.list_sacc.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))

    #################################################################################################
    def edit_coll(self):
        rows = self.list_acc.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi0 = self.list_acc.item(row, 1)
                self.twi1 = self.list_acc.item(row, 2)

            self.e = EditAcc()
            self.e.pre.setText(self.twi0.text())
            self.e.nom.setText(self.twi1.text())
            self.e.wrong1.clicked.connect(self.update_db)
            self.e.show()
        else:
            self.wrong.setText('Selectionnez un compte')

    def update_db(self):
        def edit():
            m = MyCursor()
            uptade_query = "UPDATE Accounts SET name=%s  WHERE  name=%s "
            uptade_query1 = "UPDATE Accounts SET  description=%s  WHERE name=%s "

            up = (updt_pre, self.twi0.text())
            up1 = (updt_nom, self.twi0.text())

            m.mycursor.execute(uptade_query, up)
            m.mycursor.execute(uptade_query1, up1)

            m.db.commit()
            m = MyCursor()
            m.mycursor.execute('SELECT * FROM Accounts')
            f = m.mycursor.fetchall()
            self.list_acc.setRowCount(0)
            for column_number, row_data in enumerate(f):
                self.list_acc.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    self.list_acc.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))

        updt_pre = self.e.pre.text()
        updt_nom = self.e.nom.toPlainText()

        if updt_pre != self.twi0.text() and updt_nom != self.twi1.text():
            edit()
            self.e.close()
        elif updt_pre != self.twi0.text() and updt_nom == self.twi1.text():
            edit()
            self.e.close()
        elif updt_pre == self.twi0.text() and updt_nom != self.twi1.text():
            edit()
            self.e.close()

        elif updt_pre == self.twi0.text() and updt_nom == self.twi1.text():
            self.e.wrg.setText("Vous avez entré les memes informations")

    def displaytime(self):
        time = QTime.currentTime()
        self.time.setText(time.toString(Qt.DefaultLocaleLongDate))

    def clicked_add(self):
        nom = self.nom.text()
        desc = self.desc.toPlainText()

        m = MyCursor()
        m.mycursor.execute("""SELECT name FROM Accounts WHERE name=%s""", (nom,))
        msg = m.mycursor.fetchone()
        if nom != '':

            if msg is not None:
                self.wrong.setText('Ce compte est déja crée!')
            else:
                if self.radioButton.isChecked():
                    db1 = MyCursor()
                    query = "INSERT INTO Accounts (created, name, description, Obl) VALUES (%s,%s,%s,%s)"
                    db1.mycursor.execute(query, (datetime.now(), nom, desc, True))
                    db1.db.commit()
                    self.wrong.clear()
                else:
                    db1 = MyCursor()
                    query = "INSERT INTO Accounts (created, name, description, Obl) VALUES (%s,%s,%s,%s)"
                    db1.mycursor.execute(query, (datetime.now(), nom, desc, False))
                    db1.db.commit()
                    self.wrong.clear()
        else:
            self.wrong.setText('Veuillez entrer le nom du compte')

        db1 = MyCursor()
        se = db1.mycursor.execute('SELECT created, name, description FROM Accounts')
        f = db1.mycursor.fetchall()
        self.list_acc.setRowCount(0)
        for column_number, row_data in enumerate(f):
            self.list_acc.insertRow(column_number)
            for row_number, data in enumerate(row_data):
                self.list_acc.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))

    def clicked_delete(self):
        rows = self.list_acc.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi0 = self.list_acc.item(row, 1)
                self.twit = self.list_acc.item(row, 2)
            self.s = DeleteAcc()
            self.s.b_log.clicked.connect(self.clicked_confirm)
            self.s.show()
            self.wrong.setText('')
        else:
            self.wrong.setText('Selectionnez un compte')

    def clicked_confirm(self):
        self.password = self.s.line_ed_pass.text()
        self.combo = str(self.s.combo.currentText())
        m = MyCursor()
        m.mycursor.execute("SELECT * FROM User WHERE password=%s", (self.password,))
        if self.combo == 'Jamal' and len(m.mycursor.fetchall()) > 0:
            m = MyCursor()
            m.mycursor.execute("""SELECT balance FROM Accounts WHERE name=%s""", (self.twi0.text(),))
            b = m.mycursor.fetchone()[0]

            m.mycursor.execute("SELECT SUM(debit) FROM Ops WHERE type IN ('C', 'C / Annulation')")
            result4 = m.mycursor.fetchone()[0]

            m.mycursor.execute("SELECT SUM(credit) FROM Ops WHERE type IN ('C', 'C / Annulation')")
            result5 = m.mycursor.fetchone()[0]

            if result4 is None and result5 is None:
                bg = 0
                m.mycursor.execute("""INSERT INTO DeletedAccs (created, user, name, soldeAcc, soldeGen, description) 
                                        VALUES(%s,%s,%s,%s,%s,%s)""",
                                   (datetime.now(), self.user.text(), self.twi0.text(), b, bg, self.twit.text()))
                m.db.commit()
            else:
                bg = result4 + result5
                m.mycursor.execute("""INSERT INTO DeletedAccs (created, user, name, soldeAcc, soldeGen, description) 
                            VALUES(%s,%s,%s,%s,%s,%s)""",
                                   (datetime.now(), self.user.text(), self.twi0.text(), b, bg, self.twit.text()))
                m.db.commit()

            query_1 = "DELETE FROM Ops WHERE acc=%s"
            query = "DELETE FROM Accounts WHERE name = %s"
            query_ = "DELETE FROM SAccounts WHERE accountID = %s"

            m = MyCursor()
            m.mycursor.execute(query_1, (self.twi0.text(),))
            m.mycursor.execute(query_, (self.twi0.text(),))
            m.mycursor.execute(query, (self.twi0.text(),))
            m.db.commit()

            m = MyCursor()

            m.mycursor.execute('SELECT created, name, description FROM Accounts')
            f = m.mycursor.fetchall()
            self.list_acc.setRowCount(0)
            for column_number, row_data in enumerate(f):
                self.list_acc.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    self.list_acc.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
            self.s.close()

        elif self.combo != "Jamal" and len(m.mycursor.fetchall()) > 0:
            self.s.wrong1.setText("Vous n'etes pas un adminstrateur!")
            self.s.line_ed_pass.setText("")

        elif self.password == '':
            self.s.wrong1.setText("Entrer un password")
        else:
            self.s.wrong1.setText("Password incorrect!")
            self.s.line_ed_pass.setText("")

    def clicked_add_sc_(self):
        rows = self.list_acc.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi0 = self.list_acc.item(row, 1)
            m = MyCursor()
            m.mycursor.execute('SELECT accountID, created, name, description FROM SAccounts WHERE accountID=%s',
                               (self.twi0.text(),))
            f = m.mycursor.fetchall()
            self.list_sacc.setRowCount(0)
            for column_number, row_data in enumerate(f):
                self.list_sacc.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    self.list_sacc.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
            self.stack.setCurrentIndex(1)

        else:
            self.wrong.setText('Selectionnez un compte')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = AddAcc()
    window.show()
    sys.exit(app.exec())
