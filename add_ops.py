from PyQt5 import QtWidgets, QtCore, QtPrintSupport
from PyQt5.QtCore import QDate, QTime, Qt, QTimer, QRectF
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import QPrinter
from database import MyCursor
from PyQt5 import QtGui
from datetime import datetime, timedelta
from annulation import Annulation, RemEntry
from ops import Ui_zd

#GLOBALS
SWITCH = 0 



class AddOps(QWidget, Ui_zd):
    def __init__(self, parent=None):
        super(AddOps, self).__init__(parent)
        self.setWindowModality(Qt.ApplicationModal)
        self.setupUi(self)
        self.setWindowTitle('Opérations')

        self.m = MyCursor()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowIcon(QIcon('MJDB_ICON.ico'))
        self.acc_list = self.findChild(QComboBox, 'acc_combo')
        self.sacc_list = self.findChild(QComboBox, 'acc_combo2')
        self.debit = self.findChild(QLineEdit, 'debit')
        self.credit = self.findChild(QLineEdit, 'credit')
        self.insert = self.findChild(QPushButton, 'new_op')
        self.con = self.findChild(QRadioButton, 'con')
        self.non_con = self.findChild(QRadioButton, 'non_con')
        self.w_debit = self.findChild(QLabel, 'w_debit')
        self.w_credit = self.findChild(QLabel, 'w_credit')
        self.date = self.findChild(QLabel, 'date')
        self.time = self.findChild(QLabel, 'time')

        self.ops_table = self.findChild(QTableWidget, 'ops_table')
        self.user = self.findChild(QLabel, 'user')
        self.wrong = self.findChild(QLabel, 'wrong')
        self.g_ballance = self.findChild(QLineEdit, 'b_sc')
        self.g_ballance_ = self.findChild(QLineEdit, 'b_g')
        self.general = self.findChild(QLineEdit, 'general_b')
        self.title = self.findChild(QFrame, 'title_bar')
        self.colse_btn = self.findChild(QPushButton, 'close_btn')
        self.minimize = self.findChild(QPushButton, 'mini')
        self.date_label = self.findChild(QLabel, 'today')
        self.annulation = self.findChild(QCheckBox, 'annulation')

        
        self.insert.clicked.connect(self.add_ops)

        self.colse_btn.clicked.connect(lambda: self.close())
        self.minimize.clicked.connect(lambda: self.showMinimized())
        self.remarque_btn.clicked.connect(self.handlePrint)
        self.ops_table.setSortingEnabled(False)

        now = QDate.currentDate()
        self.date.setText(now.toString(Qt.ISODate))
        timer = QTimer(self)
        timer.timeout.connect(self.displaytime)
        timer.start(1000)

        self.m = MyCursor()
        self.m.mycursor.execute('SELECT name FROM Accounts')

        for x in self.m.mycursor.fetchall():
            self.acc_list.addItems(x)
        self.acc_list.currentIndexChanged.connect(self.repeat)
        self.sacc_list.currentIndexChanged.connect(self.repeat1)

        self.con.setChecked(True)
        self.general_()

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title_bar.mouseMoveEvent = moveWindow

        self.debit.textChanged.connect(self.debitChanged)
        self.credit.textChanged.connect(self.creditChanged)

        self.debit.mousePressEvent = lambda _: self.debit.selectAll()
        self.credit.mousePressEvent = lambda _: self.credit.selectAll()

        # CELL CLICKED
        self.ops_table.cellClicked.connect(self.cellOpClicked)

    def handlePrint(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QtPrintSupport.QPrintDialog(printer, self)

        if dialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:
            self.handlePaintRequest()
            

    def handlePaintRequest(self):

        rows = self.ops_table.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi0 = self.ops_table.item(row, 0)
                self.twi8 = self.ops_table.item(row, 1)
                self.twi16 = self.ops_table.item(row, 2)
                self.twi32 = self.ops_table.item(row, 3)
                self.twi64 = self.ops_table.item(row, 4)
                self.twi128 = self.ops_table.item(row, 5)
                self.twi256 = self.ops_table.item(row, 6)

        
        datetime2 = datetime.now().date().strftime('%d/%m/%Y')
        datetime1 = datetime.now().strftime('%H:%M:%S')

        printer = QPrinter()
        printer.setOrientation(getattr(QPrinter, "Landscape"))
        printer.setPaperSize(QPrinter.A5)
        painter = QtGui.QPainter()
        # Start painter
        painter.begin(printer)
        # Grab a widget you want to print
        printer.setFullPage(True)
        # Draw grabbed pixmap
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawImage(0, 0, QImage('recus-01.jpg'))
        painter.setPen(QColor('black'))
        font = QFont('Mongolian Baiti')
        font1 = QFont('Mongolian Baiti')
        font.setPointSize(15)
        font1.setPointSize(12)
        
        painter.setFont(QFont(font1))
        painter.drawText(170, 50, datetime2)
        painter.drawText(170, 77, datetime1)
        painter.drawText(140, 102, self.user.text())
        painter.drawText(15, 320, self.acc_combo.currentText())
        painter.drawText(15, 375, self.twi0.text())
        painter.drawText(500, 330, self.twi8.text())
        painter.drawText(560, 372, self.twi32.text())
        painter.drawText(455, 417, self.twi64.text())
        painter.drawText(850, 417, self.twi16.text())
        painter.setFont(QFont(font))
        painter.drawText(405, 525, self.twi128.text())
        painter.drawText(705, 525, self.twi256.text())
        
        painter.end()

    def cellOpClicked(self):
        self.stackedWidget.setCurrentIndex(0)
    def general_(self):
        self.m = MyCursor()
        self.m.mycursor.execute("SELECT SUM(debit) FROM Ops WHERE type IN ('C', 'C / Annulation')")
        result4 = self.m.mycursor.fetchone()[0]

        self.o = MyCursor()
        self.o.mycursor.execute("SELECT SUM(credit) FROM Ops WHERE type IN ('C', 'C / Annulation')")
        result5 = self.o.mycursor.fetchone()[0]
        if result4 is None and result5 is None:
            pass
        else:
            re = result4 + result5
            formatted_re = "{:,.2f}".format(re)
            if re < 0:
                self.general.setStyleSheet("""QLineEdit{border-radius:10px;
                                                                      color: rgb(255, 0, 0);}""")
                self.general.setText(formatted_re + ' DH')
            elif re > 0:
                self.general.setStyleSheet("""QLineEdit{border-radius:10px;
                                                                      color: rgb(0, 170, 0);}""")
                self.general.setText(formatted_re + ' DH')
            elif re == 0:
                self.general.setStyleSheet("""QLineEdit{border-radius:10px;
                                                                      color: rgb(0, 0, 0);}""")
                self.general.setText(formatted_re + ' DH')

    def debitChanged(self):
        if self.debit.text() == '':
            self.debit.setText('0')
            self.debit.selectAll()

    def creditChanged(self):
        if self.credit.text() == '':
            self.credit.setText('0')
            self.credit.selectAll()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def displaytime(self):
        time = QTime.currentTime()
        self.time.setText(time.toString(Qt.DefaultLocaleLongDate))

    def style_table(self):
        for x in range(self.ops_table.rowCount()):
            g = float(self.ops_table.item(x, 6).text())
            y = float(self.ops_table.item(x, 5).text())
            if g < 0:
                formatted_float_debit = "{:,.2f}".format(g)
                self.ops_table.setItem(x, 6, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH')))
                self.ops_table.item(x, 6).setForeground(QtGui.QColor(255, 0, 0))
            elif y > 0:
                formatted_float_debit1 = "{:,.2f}".format(y)
                self.ops_table.setItem(x, 5, QtWidgets.QTableWidgetItem(str(formatted_float_debit1 + ' DH')))
                self.ops_table.item(x, 5).setForeground(QtGui.QColor(0, 170, 0))
            elif g == 0 or y == 0:
                formatted_float_debit = "{:,.2f}".format(g)
                formatted_float_debit1 = "{:,.2f}".format(y)
                self.ops_table.setItem(x, 6, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH')))
                self.ops_table.item(x, 6).setForeground(QtGui.QColor(0, 0, 0))
                self.ops_table.setItem(x, 5, QtWidgets.QTableWidgetItem(str(formatted_float_debit1 + ' DH')))
                self.ops_table.item(x, 5).setForeground(QtGui.QColor(0, 0, 0))

    def fill_table(self):
        if self.sacc_list.currentText() == 'Tout':
            time_r = datetime.now().strftime('%H-%M-%S')
            r = " ".join([self.date_label.text(), str(time_r)])
            date = datetime.strptime(r, '%d/%m/%Y %H-%M-%S')

            self.m.mycursor.execute("""SELECT opID, reference, userID, created, type ,debit, credit FROM Ops
                                    WHERE acc = %s and created between %s and %s""",
                                    (self.acc_list.currentText(), date - timedelta(1), datetime.now()))
            f = self.m.mycursor.fetchall()
            self.ops_table.setRowCount(0)
            for column_number, row_data in enumerate(f):
                self.ops_table.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    self.ops_table.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
            self.style_table()
        elif self.sacc_list.currentText() == 'Selectionnez un sous-compte...':
            time_r = datetime.now().strftime('%H-%M-%S')
            r = " ".join([self.date_label.text(), str(time_r)])
            date = datetime.strptime(r, '%d/%m/%Y %H-%M-%S')

            self.m.mycursor.execute("""SELECT opID, reference, userID, created, type ,debit, credit FROM Ops
                                                WHERE acc = %s and created between %s and %s""",
                                    (self.acc_list.currentText(), date - timedelta(1), datetime.now()))
            f = self.m.mycursor.fetchall()
            self.ops_table.setRowCount(0)
            for column_number, row_data in enumerate(f):
                self.ops_table.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    self.ops_table.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
            self.style_table()
        else:
            time_r = datetime.now().strftime('%H-%M-%S')
            r = " ".join([self.date_label.text(), str(time_r)])
            date = datetime.strptime(r, '%d/%m/%Y %H-%M-%S')

            self.m.mycursor.execute("""SELECT opID, reference, userID, created, type ,debit, credit FROM Ops
                     WHERE opID = %s and acc=%s and created between %s and %s""",
                                    (self.sacc_list.currentText(), self.acc_list.currentText(), date - timedelta(1), datetime.now()))
            f = self.m.mycursor.fetchall()
            self.ops_table.setRowCount(0)
            for column_number, row_data in enumerate(f):
                self.ops_table.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    self.ops_table.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
            self.style_table()
        time_r = datetime.now().strftime('%H-%M-%S')
        r = " ".join([self.date_label.text(), str(time_r)])
        date = datetime.strptime(r, '%d/%m/%Y %H-%M-%S')

        self.m = MyCursor()
        self.m.mycursor.execute("SELECT SUM(debit) FROM Ops WHERE opID=%s and acc=%s and created between %s and %s", (self.sacc_list.currentText(), self.acc_list.currentText(),
         date - timedelta(1), datetime.now().date(),))
        result = self.m.mycursor.fetchone()[0]

        self.o = MyCursor()
        self.o.mycursor.execute("SELECT SUM(credit) FROM Ops WHERE opID=%s and acc=%s and created between %s and %s", (self.sacc_list.currentText(), self.acc_list.currentText(),
         date - timedelta(1), datetime.now().date(),))
        result1 = self.o.mycursor.fetchone()[0]
 
        if result is None and result1 is None:
            l_sc = 0
            self.g_ballance.setStyleSheet("""border-radius:10px;
                           color: rgb(0, 0, 0);""")
            formatted_float_debit = "{:,.2f}".format(l_sc)
            self.g_ballance.setText(str(formatted_float_debit) + ' DH')

        else:
            l_sc = result + result1
            if l_sc < 0:
                self.g_ballance.setStyleSheet("""border-radius:10px;
                           color: rgb(255, 0, 0);""")
                formatted_float_debit = "{:,.2f}".format(l_sc)
                self.g_ballance.setText(str(formatted_float_debit) + ' DH')
            elif l_sc > 0:
                self.g_ballance.setStyleSheet("""border-radius:10px;
                           color: rgb(0, 170, 0);""")
                formatted_float_debit = "{:,.2f}".format(l_sc)
                self.g_ballance.setText(str(formatted_float_debit) + ' DH')

    def repeat1(self):
        self.fill_table()
    def soldeSCompte(self):
        time_r = datetime.now().strftime('%H-%M-%S')
        r = " ".join([self.date_label.text(), str(time_r)])
        date = datetime.strptime(r, '%d/%m/%Y %H-%M-%S')


        self.m = MyCursor()
        self.m.mycursor.execute("SELECT SUM(debit) FROM Ops WHERE opID=%s and acc=%s and created between %s and %s", (self.sacc_list.currentText(), self.acc_list.currentText(), datetime.now().date() - timedelta(1), datetime.now().date(),))
        result = self.m.mycursor.fetchone()[0]

        self.m.mycursor.execute("SELECT SUM(credit) FROM Ops WHERE opID=%s and acc=%s and created between %s and %s", (self.sacc_list.currentText(), self.acc_list.currentText(), datetime.now().date() - timedelta(1), datetime.now().date(),))
        result1 = self.m.mycursor.fetchone()[0]
        
        if result is None and result1 is None:
            self.g_ballance.setStyleSheet("color: rbg(0, 0, 0);")
            fr1 = 0
            formatted_float_debit = "{:,.2f}".format(fr1)
            self.g_ballance.setText(str(formatted_float_debit) + ' DH')
        else:
            self.fr12 = result + result1
            if self.fr12 < 0:
                self.g_ballance.setStyleSheet("color: rgb(255, 0, 0);")
                formatted_float_debit = "{:,.2f}".format(self.fr12)
                self.g_ballance.setText(str(formatted_float_debit) + ' DH')
            elif self.fr12 > 0:
                self.g_ballance.setStyleSheet("color: rgb(0, 170, 0);")
                formatted_float_debit = "{:,.2f}".format(self.fr12)
                self.g_ballance.setText(str(formatted_float_debit) + ' DH')
            return self.fr12
            

        
    def soldeCompte(self):
        self.m.mycursor.execute("SELECT SUM(debit) FROM Ops WHERE acc=%s", (self.acc_list.currentText(),))
        result2 = self.m.mycursor.fetchone()[0]

        self.m.mycursor.execute("SELECT SUM(credit) FROM Ops WHERE acc=%s", (self.acc_list.currentText(),))
        result3 = self.m.mycursor.fetchone()[0]

        if result2 is None and result3 is None:
            pass
        else:
            self.fr = result2 + result3
            self.m.mycursor.execute("UPDATE Accounts SET balance=%s WHERE name=%s", (self.fr, self.acc_list.currentText(),))
            self.m.db.commit()
            
            return self.fr
  
    def keyPressEvent(self, event):
        r = RemEntry()
        switch_rem = r.switch
        if event.key() == Qt.Key_Return:
            self.add_ops()
        
        elif event.key() == Qt.Key_Return and SWITCH == 2:
            self.anul()
    def addfunc(self, sacc, user, debit1, credit1, anul, motif):
        
            time_r = datetime.now().strftime('%H-%M-%S')
            r = " ".join([self.date_label.text(), str(time_r)])
            date = datetime.strptime(r, '%d/%m/%Y %H-%M-%S')

            debit1 = float(self.debit.text())
            credit1 = (float(self.credit.text()) * (-1))
            if self.soldeCompte() is None and self.soldeSCompte() is None:
                
                m = MyCursor()
                m.mycursor.execute(
                "INSERT INTO Ops (opID, userID, created, type, debit, credit, soldeCompte, soldeSCompte, acc, motif) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (sacc, user, date, self.type + anul, debit1, credit1, debit1+credit1, debit1+credit1,
                 str(self.acc_list.currentText()), motif,))
                m.db.commit()
            else:
                if self.soldeSCompte() is None:
                    m = MyCursor()
                    m.mycursor.execute(
                        "INSERT INTO Ops (opID, userID, created, type, debit, credit, soldeCompte, soldeSCompte, acc, motif) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (sacc, user, date, self.type + anul, debit1, credit1, self.soldeCompte()+debit1+credit1, debit1+credit1,
                        str(self.acc_list.currentText()), motif,))
                    m.db.commit()
                else:
                    m = MyCursor()
                    m.mycursor.execute(
                        "INSERT INTO Ops (opID, userID, created, type, debit, credit, soldeCompte, soldeSCompte, acc, motif) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (sacc, user, date, self.type + anul, debit1, credit1, self.soldeCompte()+debit1+credit1, self.soldeSCompte()+debit1+credit1,
                        str(self.acc_list.currentText()), motif,))
                    m.db.commit()
            
            self.soldeSCompte()
            self.soldeCompte()

            m = MyCursor()
            m.mycursor.execute('SELECT opID, reference, userID, created, type ,debit, credit FROM ops WHERE opID = %s',
                               (self.sacc_list.currentText(),))
            f = m.mycursor.fetchall()
            self.ops_table.setRowCount(0)
            for column_number, row_data in enumerate(f):
                self.ops_table.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    self.ops_table.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
            for x in range(self.ops_table.rowCount()):
                self.ops_table.item(x, 6).setForeground(QtGui.QColor(255, 0, 0))
                self.ops_table.item(x, 5).setForeground(QtGui.QColor(0, 170, 0))
            self.account_fill()
            self.fill_table()
            self.debit.selectAll()

    def anul(self):
        debit1 = float(self.debit.text())
        credit1 = (float(self.credit.text()) * (-1))
        sacc = self.sacc_list.currentText()
        user = self.user.text()
        motif = self.a.motif.toPlainText()
        if motif == '':
            self.a.wrong.setText('*')
        else:
            self.addfunc(sacc, user, debit1, credit1, ' / Annulation', motif)
            self.general_()
            self.a.close()
            self.fill_ops()

    def remarque_op(self):
            debit1 = float(self.debit.text())
            credit1 = (float(self.credit.text()) * (-1))
            sacc = self.sacc_list.currentText()
            user = self.user.text()
            motif = self.rem.motif.toPlainText()

            self.m = MyCursor()
            self.m.mycursor.execute("SELECT Obl FROM Accounts WHERE name=%s", (self.acc_list.currentText(),))

            r = ''.join(map(str, self.m.mycursor.fetchone()))

            if r == 'None':
                self.addfunc(sacc, user, debit1, credit1, '', motif)
                self.general_()
                self.rem.close()
                self.fill_ops()
            elif r == '0':
                self.addfunc(sacc, user, debit1, credit1, '', motif)
                self.general_()
                self.rem.close()
                self.fill_ops()
            else:
                if motif == '':
                    self.rem.wrong.setText("*")
                else:
                    self.addfunc(sacc, user, debit1, credit1, '', motif)
                    self.general_()
                    self.rem.close()
                    self.fill_ops()
     
    def fill_ops(self):
        self.fill_table()
        self.debit.selectAll()
        self.debit.clear()
        self.credit.clear()
        self.debit.setFocus()

    def add_ops(self):
        global SWITCH
        
        try:
            self.debit.setFocus()
            self.debit.selectAll()

            test = self.debit.text().lower()
            test_char = test.islower()

            test2 = self.credit.text().lower()
            test_char2 = test2.islower()

            if self.con.isChecked():
                self.type = self.con.text()
            elif self.non_con.isChecked():
                self.type = self.non_con.text()
            if self.sacc_list.currentText() != 'Tout':
                if self.debit.text() != '0' and self.credit.text() == '0' and self.sacc_list.currentText() != 'Selectionnez un sous-compte...' and test_char is False and test_char2 is False:
                    if self.annulation.isChecked():
                        self.a = Annulation()
                        self.a.show()
                        self.a.val.clicked.connect(self.anul)
                        SWITCH = 2
                    else:
                        self.rem = RemEntry()
                        self.rem.show()
                        self.rem.val.clicked.connect(self.remarque_op)
                        SWITCH = 1 

                elif self.debit.text() == '0' and self.credit.text() != '0' and test_char is False and test_char2 is False:
                    if self.annulation.isChecked():
                        self.a = Annulation()
                        self.a.show()
                        self.a.val.clicked.connect(self.anul)
                        SWITCH = 2

                    else:
                        self.rem = RemEntry()
                        self.rem.show()
                        self.rem.val.clicked.connect(self.remarque_op)
                        SWITCH = 1
                else:
                    pass
                
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Erreur')
            msg.setText("Erreur Inconnu! CODE D'ERREUR (0001)")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
    def account_fill(self):

        if self.acc_list.currentText() == 'Selectionnez un compte...':
            self.g_ballance.clear()
            self.g_ballance_.clear()
        else:
            self.m.mycursor.execute('SELECT balance FROM Accounts WHERE name=%s',
                                    (self.acc_list.currentText(),))
            l_ = self.m.mycursor.fetchone()[0]

            if l_ is None:
                pass
            else:
                if l_ < 0:
                    self.g_ballance_.setStyleSheet("""border-radius:10px;
                            color: rgb(255, 0, 0);""")
                    formatted_float_debit = "{:,.2f}".format(l_)
                    self.g_ballance_.setText(str(formatted_float_debit) + ' DH')
                elif l_ > 0:
                    self.g_ballance_.setStyleSheet("""border-radius:10px;
                            color: rgb(0, 170, 0);""")
                    formatted_float_debit = "{:,.2f}".format(l_)
                    self.g_ballance_.setText(str(formatted_float_debit) + ' DH')
                elif l_ == 0:
                    self.g_ballance_.setStyleSheet("""border-radius:10px;
                            color: rgb(0, 0, 0);""")
                    formatted_float_debit = "{:,.2f}".format(l_)
                    self.g_ballance_.setText(str(formatted_float_debit) + ' DH')

    def repeat(self):
        self.sacc_list.clear()
        self.m.mycursor.execute('SELECT name FROM SAccounts WHERE accountID=%s', (self.acc_list.currentText(),))
        for x in self.m.mycursor.fetchall():
            self.sacc_list.addItems(x)
        self.sacc_list.insertItem(0, 'Tout')

        self.account_fill()
        time_r = datetime.now().strftime('%H-%M-%S')
        r = " ".join([self.date_label.text(), str(time_r)])
        date = datetime.strptime(r, '%d/%m/%Y %H-%M-%S')

        self.m.mycursor.execute("""SELECT opID, reference, userID, created, type ,debit, credit FROM Ops
                        WHERE acc = %s and created between %s and %s""",
                                (self.acc_list.currentText(), date, datetime.now()))
        f = self.m.mycursor.fetchall()
        self.ops_table.setRowCount(0)
        for column_number, row_data in enumerate(f):
            self.ops_table.insertRow(column_number)
            for row_number, data in enumerate(row_data):
                self.ops_table.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
        self.style_table()
        self.fill_table()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = AddOps()
    window.show()
    sys.exit(app.exec())
