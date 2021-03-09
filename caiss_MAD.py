from PyQt5 import QtWidgets, QtCore, QtPrintSupport
from PyQt5.QtCore import QDate, QTime, Qt, QTimer
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import *
from database import MyCursor
from PyQt5 import QtGui
from datetime import datetime
from PyQt5.QtGui import QIntValidator
from Caisse_MAD import Ui_dfgsdx
from MAD_details import Ui_dfgsdx as Ui_Mad


class CaisseMad(QWidget, Ui_dfgsdx):
    def __init__(self, parent=None):
        super(CaisseMad, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle('Caisse MAD')
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowIcon(QIcon('Untitled-2-01.ico'))
        self.setWindowModality(Qt.ApplicationModal)
        self.title = self.findChild(QFrame, 'title_bar')
        self.colse_btn = self.findChild(QPushButton, 'close_btn')
        self.minimize = self.findChild(QPushButton, 'mini')
        self.l200 = self.findChild(QLineEdit, 'l200')
        self.l100 = self.findChild(QLineEdit, 'l100')
        self.l50 = self.findChild(QLineEdit, 'l50')
        self.l20 = self.findChild(QLineEdit, 'l20')
        self.l10 = self.findChild(QLineEdit, 'l10')
        self.l5 = self.findChild(QLineEdit, 'l5')
        self.l2 = self.findChild(QLineEdit, 'l2')
        self.l1 = self.findChild(QLineEdit, 'l1')
        self.l05 = self.findChild(QLineEdit, 'l05')
        self.l02 = self.findChild(QLineEdit, 'l02')
        self.l01 = self.findChild(QLineEdit, 'l01')
        self.l001 = self.findChild(QLineEdit, 'l001')
        self.o200 = self.findChild(QLineEdit, 'o200')
        self.o100 = self.findChild(QLineEdit, 'o100')
        self.o50 = self.findChild(QLineEdit, 'o50')
        self.o20 = self.findChild(QLineEdit, 'o20')
        self.o10 = self.findChild(QLineEdit, 'o10')
        self.o5 = self.findChild(QLineEdit, 'o5')
        self.o2 = self.findChild(QLineEdit, 'o2')
        self.o1 = self.findChild(QLineEdit, 'o1')
        self.o05 = self.findChild(QLineEdit, 'o05')
        self.o02 = self.findChild(QLineEdit, 'o02')
        self.o01 = self.findChild(QLineEdit, 'o01')
        self.o001 = self.findChild(QLineEdit, 'o001')
        self.caisseM = self.findChild(QLineEdit, 'caisseMAD')
        self.general = self.findChild(QLineEdit, 'general')
        self.diff = self.findChild(QLineEdit, 'dif')
        self.dec = self.findChild(QPushButton, 'dec')
        self.val = self.findChild(QPushButton, 'val')
        self.end1 = self.findChild(QPushButton, 'end')
        self.user = self.findChild(QLabel, 'user')
        self.info = self.findChild(QLabel, 'info')
        self.remarque = self.findChild(QTextEdit, 'remarque')
        self.prt_frame = self.findChild(QStackedWidget, 'print_frame')
        self.date_mad = self.findChild(QLabel, 'Date')

        self.onlyInt = QIntValidator()
        self.l200.setValidator(self.onlyInt)
        self.l100.setValidator(self.onlyInt)
        self.l50.setValidator(self.onlyInt)
        self.l20.setValidator(self.onlyInt)
        self.l10.setValidator(self.onlyInt)
        self.l5.setValidator(self.onlyInt)
        self.l2.setValidator(self.onlyInt)
        self.l1.setValidator(self.onlyInt)
        self.l05.setValidator(self.onlyInt)
        self.l02.setValidator(self.onlyInt)
        self.l01.setValidator(self.onlyInt)
        self.l001.setValidator(self.onlyInt)

        self.l200.textChanged.connect(lambda: self.calculate(self.l200, self.o200, 200))
        self.l100.textChanged.connect(lambda: self.calculate(self.l100, self.o100, 100))
        self.l50.textChanged.connect(lambda: self.calculate(self.l50, self.o50, 50))
        self.l20.textChanged.connect(lambda: self.calculate(self.l20, self.o20, 20))
        self.l10.textChanged.connect(lambda: self.calculate(self.l10, self.o10, 10))
        self.l5.textChanged.connect(lambda: self.calculate(self.l5, self.o5, 5))
        self.l2.textChanged.connect(lambda: self.calculate(self.l2, self.o2, 2))
        self.l1.textChanged.connect(lambda: self.calculate(self.l1, self.o1, 1))
        self.l05.textChanged.connect(lambda: self.calculate(self.l05, self.o05, 0.5))
        self.l02.textChanged.connect(lambda: self.calculate(self.l02, self.o02, 0.2))
        self.l01.textChanged.connect(lambda: self.calculate(self.l01, self.o01, 0.1))
        self.l001.textChanged.connect(lambda: self.calculate(self.l001, self.o001, 0.01))

        self.colse_btn.clicked.connect(lambda: self.close())
        self.minimize.clicked.connect(lambda: self.showMinimized())
        self.dec.clicked.connect(self.clear1)
        self.val.clicked.connect(self.valider)

        self.user.setText('Farouk')

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title_bar.mouseMoveEvent = moveWindow

        self.l200.mousePressEvent = lambda _: self.l200.selectAll()
        self.l100.mousePressEvent = lambda _: self.l100.selectAll()
        self.l50.mousePressEvent = lambda _: self.l50.selectAll()
        self.l20.mousePressEvent = lambda _: self.l20.selectAll()
        self.l10.mousePressEvent = lambda _: self.l10.selectAll()
        self.l5.mousePressEvent = lambda _: self.l5.selectAll()
        self.l2.mousePressEvent = lambda _: self.l2.selectAll()
        self.l1.mousePressEvent = lambda _: self.l1.selectAll()
        self.l05.mousePressEvent = lambda _: self.l05.selectAll()
        self.l02.mousePressEvent = lambda _: self.l02.selectAll()
        self.l01.mousePressEvent = lambda _: self.l01.selectAll()
        self.l001.mousePressEvent = lambda _: self.l001.selectAll()

        self.m = MyCursor()
        self.m.mycursor.execute("SELECT SUM(debit) FROM Ops WHERE type IN ('C', 'C / Annulation')")
        self.result4 = self.m.mycursor.fetchone()[0]

        self.o = MyCursor()
        self.o.mycursor.execute("SELECT SUM(credit) FROM Ops WHERE type IN ('C', 'C / Annulation')")
        self.result5 = self.o.mycursor.fetchone()[0]
        if self.result4 is None and self.result5 is None:
            pass
        else:
            self.re = self.result4 + self.result5

            formatted_re = "{:,.2f}".format(self.re)
            if self.re < 0:
                self.general.setStyleSheet("""QLineEdit{border-radius:10px;
                                                              color: rgb(255, 0, 0);}""")
                self.general.setText(formatted_re + ' DH')
            elif self.re > 0:
                self.general.setStyleSheet("""QLineEdit{border-radius:10px;
                                                              color: rgb(0, 170, 0);}""")
                self.general.setText(formatted_re + ' DH')
            elif self.re == 0:
                self.general.setStyleSheet("""QLineEdit{border-radius:10px;
                                                              color: rgb(0, 0, 0);}""")
                self.general.setText(formatted_re + ' DH')
        now = QDate.currentDate()
        self.date.setText(now.toString(Qt.ISODate))

        timer = QTimer(self)
        timer.timeout.connect(self.displaytime)
        timer.start(1000)

    #########################################################################################################

    def displaytime(self):
        time = QTime.currentTime()
        self.time.setText(time.toString(Qt.DefaultLocaleLongDate))

    def fade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    def unfade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def clear1(self):
        self.l200.clear()
        self.l100.clear()
        self.l50.clear()
        self.l20.clear()
        self.l10.clear()
        self.l5.clear()
        self.l2.clear()
        self.l1.clear()
        self.l05.clear()
        self.l02.clear()
        self.l01.clear()
        self.l001.clear()
        self.fade(self.info)

    def dif1(self):
        total1 = float(self.l200.text()) * 200 + float(self.l100.text()) * 100 + float(self.l50.text()) * 50
        total2 = float(self.l20.text()) * 20 + float(self.l10.text()) * 10 + float(self.l5.text()) * 5
        total3 = float(self.l2.text()) * 2 + float(self.l1.text()) * 1 + float(self.l05.text()) * 0.5 + float(
            self.l02.text()) * 0.2 + float(self.l01.text()) * 0.1 + float(self.l001.text()) * 0.01
        if self.re < 0:
            self.total12 = total1 + total2 + total3 + self.re
        elif self.re > 0:
            self.total12 = (total1 + total2 + total3) - self.re

        return self.total12

    def valider(self):
        s = self.tot()
        d = self.dif1()
        time_r = datetime.now().strftime('%H-%M-%S')
        r = " ".join([self.date_mad.text(), str(time_r)])
        date = datetime.strptime(r, '%d/%m/%Y %H-%M-%S')
        self.m = MyCursor()
        self.m.mycursor.execute("""INSERT INTO CaisseMad (user, remarque, created, bal, caisse, dif, l200, l100, l50, l20, l10, l5, l2, l1, l05, l02, l01, l001)
                                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                                (
                                    self.user.text(), self.remarque.toPlainText(), date, self.re,
                                    float(s), float(d),
                                    int(self.l200.text()), int(self.l100.text()), int(self.l50.text()),
                                    int(self.l20.text()), int(self.l10.text()), int(self.l5.text()),
                                    int(self.l2.text()), int(self.l1.text()), int(self.l05.text()),
                                    int(self.l02.text()), int(self.l01.text()), int(self.l001.text()),))
        self.m.db.commit()

        self.info.setText('Caisse MAD ajoutée!')
        self.unfade(self.info)

    def tot(self):
        total1 = float(self.l200.text()) * 200 + float(self.l100.text()) * 100 + float(self.l50.text()) * 50
        total2 = float(self.l20.text()) * 20 + float(self.l10.text()) * 10 + float(self.l5.text()) * 5
        total3 = float(self.l2.text()) * 2 + float(self.l1.text()) * 1 + float(self.l05.text()) * 0.5 + float(
            self.l02.text()) * 0.2 + float(self.l01.text()) * 0.1 + float(self.l001.text()) * 0.01
        self.total = total1 + total2 + total3
        return self.total

    def test(self):
        t = self.tot()
        s = self.dif1()

        if s < t and s != 0:
            self.diff.setStyleSheet("""QLineEdit{border-radius:10px; 
            color: rgb(255, 0, 0);}""")
            self.diff.setText(str("{:,.2f}".format(self.dif1())) + ' DH')
        if s > 0:
            self.diff.setStyleSheet("""QLineEdit{border-radius:10px;
            color: rgb(0, 170, 127);}""")
            self.diff.setText(str("{:,.2f}".format(self.dif1())) + ' DH')
        if s == 0:
            self.diff.setText(str("{:,.2f}".format(self.dif1())) + ' DH')
            self.diff.setStyleSheet("""QLineEdit{border-radius:10px;
            color:rgb(0, 170, 0);}""")

        self.caisseM.setText(str("{:,.2f}".format(self.tot())) + ' DH')

    def calculate(self, bill, o, x):
        if bill.text() == '':
            o.setText("0.00 DH")
            bill.setText('0')
            bill.selectAll()
        else:
            self.r = float(bill.text()) * x
            e = "{:,.2f}".format(self.r)
            o.setText(e + ' DH')
            self.test()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


class DetailsCaisseMad(QWidget, Ui_Mad):
    def __init__(self, parent=None):
        super(DetailsCaisseMad, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle('Details MAD')
        self.setWindowIcon(QIcon('Untitled-2-01.ico'))
        self.l200 = self.findChild(QLineEdit, 'l200')
        self.l100 = self.findChild(QLineEdit, 'l100')
        self.l50 = self.findChild(QLineEdit, 'l50')
        self.l20 = self.findChild(QLineEdit, 'l20')
        self.l10 = self.findChild(QLineEdit, 'l10')
        self.l5 = self.findChild(QLineEdit, 'l5')
        self.l2 = self.findChild(QLineEdit, 'l2')
        self.l1 = self.findChild(QLineEdit, 'l1')
        self.l05 = self.findChild(QLineEdit, 'l05')
        self.l02 = self.findChild(QLineEdit, 'l02')
        self.l01 = self.findChild(QLineEdit, 'l01')
        self.l001 = self.findChild(QLineEdit, 'l001')
        self.o200 = self.findChild(QLineEdit, 'o200')
        self.o100 = self.findChild(QLineEdit, 'o100')
        self.o50 = self.findChild(QLineEdit, 'o50')
        self.o20 = self.findChild(QLineEdit, 'o20')
        self.o10 = self.findChild(QLineEdit, 'o10')
        self.o5 = self.findChild(QLineEdit, 'o5')
        self.o2 = self.findChild(QLineEdit, 'o2')
        self.o1 = self.findChild(QLineEdit, 'o1')
        self.o05 = self.findChild(QLineEdit, 'o05')
        self.o02 = self.findChild(QLineEdit, 'o02')
        self.o01 = self.findChild(QLineEdit, 'o01')
        self.o001 = self.findChild(QLineEdit, 'o001')
        self.title = self.findChild(QFrame, 'title_bar')
        self.colse_btn = self.findChild(QPushButton, 'close_btn')
        self.minimize = self.findChild(QPushButton, 'mini')
        self.caisseM = self.findChild(QLineEdit, 'caisseMAD')
        self.general = self.findChild(QLineEdit, 'general')
        self.user = self.findChild(QLabel, 'user')
        self.btn_prnt = self.findChild(QPushButton, 'print')
        self.diff = self.findChild(QLineEdit, 'dif')
        self.date = self.findChild(QLabel, 'date')
        self.time = self.findChild(QLabel, 'time')
        self.frame3 = self.findChild(QFrame, 'frame_3')
        self.info = self.findChild(QLabel, 'info')
        self.remarque = self.findChild(QTextEdit, 'remarque')

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        self.colse_btn.clicked.connect(lambda: self.close())
        self.minimize.clicked.connect(lambda: self.showMinimized())
        self.btn_prnt.clicked.connect(self.handlePrint)

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title.mouseMoveEvent = moveWindow
        self.l200.mousePressEvent = lambda _: self.l200.selectAll()
        self.l100.mousePressEvent = lambda _: self.l100.selectAll()
        self.l50.mousePressEvent = lambda _: self.l50.selectAll()
        self.l20.mousePressEvent = lambda _: self.l20.selectAll()
        self.l10.mousePressEvent = lambda _: self.l10.selectAll()
        self.l5.mousePressEvent = lambda _: self.l5.selectAll()
        self.l2.mousePressEvent = lambda _: self.l2.selectAll()
        self.l1.mousePressEvent = lambda _: self.l1.selectAll()
        self.l05.mousePressEvent = lambda _: self.l05.selectAll()
        self.l02.mousePressEvent = lambda _: self.l02.selectAll()
        self.l01.mousePressEvent = lambda _: self.l01.selectAll()
        self.l001.mousePressEvent = lambda _: self.l001.selectAll()
        now = QDate.currentDate()
        self.date.setText(now.toString(Qt.ISODate))

        timer = QTimer(self)
        timer.timeout.connect(self.displaytime)
        timer.start(1000)

    def displaytime(self):
        time = QTime.currentTime()
        self.time.setText(time.toString(Qt.DefaultLocaleLongDate))

    def handlePrint(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.handlePaintRequest()

    def handlePaintRequest(self):
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
        painter.drawImage(0, 0, QImage('details_c_m-01.jpg'))

        painter.drawPixmap(170, 63, self.date.grab())
        painter.drawPixmap(170, 90, self.time.grab())
        painter.drawPixmap(170, 110, self.user.grab())

        painter.drawPixmap(150, 200, self.l200.grab())
        painter.drawPixmap(150, 250, self.l100.grab())
        painter.drawPixmap(150, 300, self.l50.grab())
        painter.drawPixmap(150, 350, self.l20.grab())
        painter.drawPixmap(150, 400, self.l10.grab())
        painter.drawPixmap(150, 450, self.l5.grab())

        painter.drawPixmap(250, 200, self.o200.grab())
        painter.drawPixmap(250, 250, self.o100.grab())
        painter.drawPixmap(250, 300, self.o50.grab())
        painter.drawPixmap(250, 350, self.o20.grab())
        painter.drawPixmap(250, 400, self.o10.grab())
        painter.drawPixmap(250, 450, self.o5.grab())

        painter.drawPixmap(700, 200, self.l2.grab())
        painter.drawPixmap(700, 250, self.l1.grab())
        painter.drawPixmap(700, 300, self.l05.grab())
        painter.drawPixmap(700, 350, self.l02.grab())
        painter.drawPixmap(700, 400, self.l01.grab())
        painter.drawPixmap(700, 450, self.l001.grab())

        painter.drawPixmap(800, 200, self.o2.grab())
        painter.drawPixmap(800, 250, self.o1.grab())
        painter.drawPixmap(800, 300, self.o05.grab())
        painter.drawPixmap(800, 350, self.o02.grab())
        painter.drawPixmap(800, 400, self.o01.grab())
        painter.drawPixmap(800, 450, self.o001.grab())

        painter.drawPixmap(70, 550, self.caisseMAD.grab())
        painter.drawPixmap(370, 550, self.diff.grab())
        painter.drawPixmap(670, 550, self.general.grab())

        painter.setPen(QColor(0, 0, 0))
        painter.setFont(QFont('Mongolian Baiti', 12))

        painter.drawText(200, 680, self.remarque.toPlainText())
        painter.drawText(710, 720, self.identif.text())

        # End painting
        painter.end()
        self.info.setText('Caisse MAD imprimée!')

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = DetailsCaisseMad()
    window.show()
    sys.exit(app.exec())
