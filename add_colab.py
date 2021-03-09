from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, QTime, Qt, QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database import MyCursor
from edit_col import EditCollab
from delt_acc import DeleteAcc
from collab import Ui_AddColab_


class AddCollab(QtWidgets.QWidget, Ui_AddColab_):
    def __init__(self):
        super(AddCollab, self).__init__()

        self.setupUi(self)
        self.setWindowTitle('Ajouter un collaborateur')
        self.time = self.findChild(QLabel, "l_time")
        self.date = self.findChild(QLabel, "l_date")
        self.add = self.findChild(QPushButton, "btn_add")
        self.remove = self.findChild(QPushButton, "btn_remove")
        self.first_name = self.findChild(QLineEdit, "first_name")
        self.last_name = self.findChild(QLineEdit, "last_name")
        self.password_ = self.findChild(QLineEdit, "pass_")
        self.list_ = self.findChild(QTableWidget, 'tableWidget')
        self.wrong = self.findChild(QLabel, "wrong1")
        self.edit = self.findChild(QPushButton, 'btn_edit')
        self.user = self.findChild(QLabel, 'user')

        now = QDate.currentDate()
        self.date.setText(now.toString(Qt.ISODate))
        timer = QTimer(self)
        timer.timeout.connect(self.displaytime)
        timer.start(1000)

        self.add.clicked.connect(self.add_col)
        self.edit.clicked.connect(self.edit_col)
        self.remove.clicked.connect(self.remove_coll)

        m = MyCursor()
        m.mycursor.execute('SELECT * FROM User')
        f = m.mycursor.fetchall()
        self.tableWidget.setRowCount(0)
        for column_number, row_data in enumerate(f):
            self.tableWidget.insertRow(column_number)
            for row_number, data in enumerate(row_data):
                self.tableWidget.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))

    def displaytime(self):
        time = QTime.currentTime()
        self.time.setText(time.toString(Qt.DefaultLocaleLongDate))

    def add_col(self):
        self.f_text = self.first_name.text()
        self.l_text = self.last_name.text()
        self.password = self.password_.text()
        if len(self.f_text) > 0 and len(self.l_text) > 0 and len(self.password) > 0:
            if self.f_text != 'Jamal':
                self.p = DeleteAcc()
                self.p.b_log.clicked.connect(self.add_coll)
                self.p.show()
            else:
                self.wrong.setText("Ce prenom est pour l'administrateur")
        else:
            self.wrong.setText('Entrer tout vous informations')

    def add_coll(self):
        self.f_text = self.first_name.text()
        self.l_text = self.last_name.text()
        self.password = self.password_.text()
        self.password1 = self.p.line_ed_pass.text()
        self.combo = str(self.p.combo.currentText())
        o = MyCursor()
        o.mycursor.execute("SELECT * FROM User WHERE password=%s", (self.password1,))
        if self.combo == 'Jamal' and len(o.mycursor.fetchall()) > 0:

            m = MyCursor()
            m.mycursor.execute("""SELECT firstName FROM User WHERE firstName=%s""", (self.f_text,))
            msg = m.mycursor.fetchone()
            if msg is not None:
                self.wrong.setText('Ce collaborateur déja existe!')
                self.p.close()
            else:
                m = MyCursor()
                m.mycursor.execute('INSERT INTO User (firstName, lastName, password) VALUES (%s,%s,%s)',
                                   (self.f_text, self.l_text, self.password))
                m.db.commit()

                se = m.mycursor.execute('SELECT * FROM User')
                f = m.mycursor.fetchall()
                self.list_.setRowCount(0)
                for column_number, row_data in enumerate(f):
                    self.list_.insertRow(column_number)
                    for row_number, data in enumerate(row_data):
                        self.list_.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
                self.wrong.setText("")
                self.p.close()

        elif self.combo != "Jamal" and len(o.mycursor.fetchall()) > 0:
            self.p.wrong1.setText("Vous n'etes pas un adminstrateur!")
            self.p.line_ed_pass.setText("")

        elif self.password1 == '':
            self.p.wrong1.setText("Entrer un password")
        else:
            self.p.wrong1.setText("Password incorrect!")
            self.p.line_ed_pass.setText("")

    def edit_col(self):
        rows = self.list_.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi0 = self.list_.item(row, 0)
            self.p = DeleteAcc()
            self.p.b_log.clicked.connect(self.edit_coll)

            self.p.show()

        else:
            self.wrong.setText('Selectionnez un collaborateurs')

    def edit_coll(self):
        self.password = self.p.line_ed_pass.text()
        self.combo = str(self.p.combo.currentText())
        m = MyCursor()
        m.mycursor.execute("SELECT * FROM User WHERE password=%s", (self.password,))
        if self.combo == 'Jamal' and len(m.mycursor.fetchall()) > 0:

            rows = self.list_.selectionModel().selectedRows()
            for self.index in sorted(rows):
                pass
            if len(rows) > 0:
                for row in range(self.index.row(), self.index.row() + 1):
                    self.twi0 = self.list_.item(row, 0)
                    self.twi1 = self.list_.item(row, 1)
                    self.twi2 = self.list_.item(row, 2)

                self.e = EditCollab()
                self.e.pre.setText(self.twi0.text())
                self.e.nom.setText(self.twi1.text())
                self.e.password_e.setText(self.twi2.text())
                self.e.wrong1.clicked.connect(self.update_db)
                self.e.show()
            else:
                self.wrong.setText('Selectionnez un collaborateurs')
        elif self.combo != "Jamal" and len(m.mycursor.fetchall()) > 0:
            self.p.wrong1.setText("Vous n'etes pas un adminstrateur!")
            self.p.line_ed_pass.setText("")

        elif self.password == '':
            self.p.wrong1.setText("Entrer un password")
        else:
            self.p.wrong1.setText("Password incorrect!")
            self.p.line_ed_pass.setText("")

    def update_db(self):
        def edit():
            rows = self.list_.selectionModel().selectedRows()
            for self.index in sorted(rows):
                pass
            if len(rows) > 0:
                for row in range(self.index.row(), self.index.row() + 1):
                    self.twi0 = self.list_.item(row, 0)
            m = MyCursor()
            uptade_query = "UPDATE User SET  firstName=%s  WHERE  firstName=%s "
            uptade_query1 = "UPDATE User SET  lastName=%s  WHERE  firstName=%s "
            uptade_query2 = "UPDATE User SET  password=%s  WHERE  firstName=%s "
            up = (updt_pre, self.twi0.text())
            up1 = (updt_nom, self.twi0.text())
            up2 = (updt_pass, self.twi0.text())
            m.mycursor.execute(uptade_query, up)
            m.mycursor.execute(uptade_query1, up1)
            m.mycursor.execute(uptade_query2, up2)
            m.db.commit()
            m = MyCursor()
            se = m.mycursor.execute('SELECT * FROM User')
            f = m.mycursor.fetchall()
            self.list_.setRowCount(0)
            for column_number, row_data in enumerate(f):
                self.list_.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    self.list_.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))

        updt_pre = self.e.pre.text()

        updt_nom = self.e.nom.text()
        updt_pass = self.e.password_e.text()
        if updt_pre != self.twi0.text() and updt_nom != self.twi1.text() and updt_pass != self.twi2.text():
            edit()
        elif updt_pre != self.twi0.text() and updt_nom != self.twi1.text():
            edit()
        elif updt_pre != self.twi0.text() and updt_pass != self.twi2.text():
            edit()
        elif updt_nom != self.twi1.text() and updt_pass != self.twi2.text():
            edit()
        elif updt_pre != self.twi0.text():
            edit()
        elif updt_pass != self.twi2.text():
            edit()
        elif updt_nom != self.twi1.text():
            edit()

        else:
            self.e.wrg.setText("Vous avez entré les memes informations")

        self.e.close()
        self.p.close()

    def remove_coll(self):
        rows = self.list_.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi0 = self.list_.item(row, 0)
            self.p = DeleteAcc()
            self.p.b_log.clicked.connect(self.clicked_remove)
            self.p.show()

        else:
            self.wrong.setText('Selectionnez un collaborateurs')

    def clicked_remove(self):
        self.password = self.p.line_ed_pass.text()
        self.combo = str(self.p.combo.currentText())
        m = MyCursor()
        m.mycursor.execute("SELECT * FROM User WHERE password=%s", (self.password,))
        if self.combo == 'Jamal' and len(m.mycursor.fetchall()) > 0:
            query = "DELETE FROM User WHERE firstName = %s"
            m = MyCursor()
            m.mycursor.execute(query, (self.twi0.text(),))
            m.db.commit()

            m = MyCursor()
            se = m.mycursor.execute('SELECT * FROM User')
            f = m.mycursor.fetchall()
            self.list_.setRowCount(0)
            for column_number, row_data in enumerate(f):
                self.list_.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    self.list_.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
            self.p.close()
        elif self.combo != "Jamal" and len(m.mycursor.fetchall()) > 0:
            self.p.wrong1.setText("Vous n'etes pas un adminstrateur!")
            self.p.line_ed_pass.setText("")

        elif self.password == '':
            self.p.wrong1.setText("Entrer un password")
        else:
            self.p.wrong1.setText("Password incorrect!")
            self.p.line_ed_pass.setText("")


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = AddCollab()
    window.show()
    sys.exit(app.exec())
