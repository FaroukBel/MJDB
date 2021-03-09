from datetime import datetime

from PyQt5 import QtCore, QtGui, QtPrintSupport, QtWidgets
from PyQt5.QtCore import QDate, Qt, QTime, QTimer
from PyQt5.QtGui import *
from PyQt5.QtGui import QIntValidator, QPainter
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import *

from Caisse_D import Ui_dfgsdx
from cour import Cour
from D_details import Ui_dfgsdx as Ui_details_D
from database import MyCursor


class CaisseD(QWidget, Ui_dfgsdx):
    def __init__(self, parent=None):
        super(CaisseD, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle('Caisse DEVISE')
        self.c = Cour()
        self.c.val.clicked.connect(self.CourClose)
        self.c.show()
        self.setWindowIcon(QIcon('Untitled-2-01.ico'))
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        self.title = self.findChild(QFrame, 'title_bar')
        self.colse_btn = self.findChild(QPushButton, 'close_btn')
        self.minimize = self.findChild(QPushButton, 'mini')
        self.e5 = self.findChild(QLineEdit, 'l5_2')
        self.usa = self.findChild(QLineEdit, 'us')
        self.can = self.findChild(QLineEdit, 'canada')
        self.ster = self.findChild(QLineEdit, 'sterling')
        self.suis = self.findChild(QLineEdit, 'suise')
        self.dan = self.findChild(QLineEdit, 'danoi')
        self.devise_label = self.findChild(QLabel, 'devise_ajt')

        self.stacked = self.findChild(QStackedWidget, 'stacked')
        self.add_d = self.findChild(QPushButton, 'add_devise')
        self.back_ = self.findChild(QPushButton, 'back')
        self.o1 = self.findChild(QLineEdit, 'o5_2')

        self.caisseM = self.findChild(QLineEdit, 'caisseMAD')

        self.diff = self.findChild(QLineEdit, 'dif')
        self.end1 = self.findChild(QPushButton, 'end')
        self.courtxt = self.findChild(QLineEdit, 'cour')
        self.up = self.findChild(QPushButton, 'update')
        self.combo = self.findChild(QComboBox, 'devise_combo')
        self.ajouter = self.findChild(QPushButton, 'ajout')
        self.stacked2 = self.findChild(QStackedWidget, 'stacked2')
        self.stacked3 = self.findChild(QStackedWidget, 'stacked3')
        self.val_d_ = self.findChild(QPushButton, 'val_3')
        self.remarque = self.findChild(QTextEdit, 'remarque')
        self.date_d = self.findChild(QLabel, 'info_2')

        self.onlyInt = QIntValidator()
        self.l200.setValidator(self.onlyInt)
        self.l100.setValidator(self.onlyInt)
        self.l50.setValidator(self.onlyInt)
        self.l20.setValidator(self.onlyInt)
        self.l10.setValidator(self.onlyInt)
        self.l5.setValidator(self.onlyInt)
        self.e5.setValidator(self.onlyInt)

        # USD
        self.u1 = self.findChild(QLineEdit, 'us100')
        self.u2 = self.findChild(QLineEdit, 'us50')
        self.u3 = self.findChild(QLineEdit, 'us20')
        self.u4 = self.findChild(QLineEdit, 'us10')
        self.u5 = self.findChild(QLineEdit, 'us5')
        self.u6 = self.findChild(QLineEdit, 'us2')
        self.u7 = self.findChild(QLineEdit, 'us1')

        self.usd1 = self.findChild(QLineEdit, 'uus100')
        self.usd2 = self.findChild(QLineEdit, 'uus100_2')
        self.usd3 = self.findChild(QLineEdit, 'uus100_3')
        self.usd4 = self.findChild(QLineEdit, 'uus100_4')
        self.usd5 = self.findChild(QLineEdit, 'uus100_5')
        self.usd6 = self.findChild(QLineEdit, 'uus100_6')
        self.usd7 = self.findChild(QLineEdit, 'uus100_7')
        # CANADA
        self.c1 = self.findChild(QLineEdit, 'cv')
        self.c2 = self.findChild(QLineEdit, 'cv_2')
        self.c3 = self.findChild(QLineEdit, 'cv_3')
        self.c4 = self.findChild(QLineEdit, 'cv_4')
        self.c5 = self.findChild(QLineEdit, 'cv_5')
        self.c6 = self.findChild(QLineEdit, 'cv_6')
        self.c7 = self.findChild(QLineEdit, 'cv_7')

        self.x1 = self.findChild(QLineEdit, 'cx')
        self.x2 = self.findChild(QLineEdit, 'cx_2')
        self.x3 = self.findChild(QLineEdit, 'cx_3')
        self.x4 = self.findChild(QLineEdit, 'cx_4')
        self.x5 = self.findChild(QLineEdit, 'cx_5')
        self.x6 = self.findChild(QLineEdit, 'cx_6')
        self.x7 = self.findChild(QLineEdit, 'cx_7')
        # STERLING
        self.s1 = self.findChild(QLineEdit, 'ct')
        self.s2 = self.findChild(QLineEdit, 'ct_2')
        self.s3 = self.findChild(QLineEdit, 'ct_3')
        self.s4 = self.findChild(QLineEdit, 'ct_4')
        self.s5 = self.findChild(QLineEdit, 'ct_5')
        self.s6 = self.findChild(QLineEdit, 'ct_6')
        self.s7 = self.findChild(QLineEdit, 'ct_7')

        self.r1 = self.findChild(QLineEdit, 'cr')
        self.r2 = self.findChild(QLineEdit, 'cr_2')
        self.r3 = self.findChild(QLineEdit, 'cr_3')
        self.r4 = self.findChild(QLineEdit, 'cr_4')
        self.r5 = self.findChild(QLineEdit, 'cr_5')
        self.r6 = self.findChild(QLineEdit, 'cr_6')
        self.r7 = self.findChild(QLineEdit, 'cr_7')
        # GIBRALTAR
        self.g1 = self.findChild(QLineEdit, 'cg')
        self.g2 = self.findChild(QLineEdit, 'cg_2')
        self.g3 = self.findChild(QLineEdit, 'cg_3')
        self.g4 = self.findChild(QLineEdit, 'cg_4')
        self.g5 = self.findChild(QLineEdit, 'cg_5')
        self.g6 = self.findChild(QLineEdit, 'cg_6')
        self.g7 = self.findChild(QLineEdit, 'cg_7')

        self.b1 = self.findChild(QLineEdit, 'cb')
        self.b2 = self.findChild(QLineEdit, 'cb_2')
        self.b3 = self.findChild(QLineEdit, 'cb_3')
        self.b4 = self.findChild(QLineEdit, 'cb_4')
        self.b5 = self.findChild(QLineEdit, 'cb_5')
        self.b6 = self.findChild(QLineEdit, 'cb_6')
        self.b7 = self.findChild(QLineEdit, 'cb_7')
        # SUISSE
        self.a1 = self.findChild(QLineEdit, 'ss')
        self.a2 = self.findChild(QLineEdit, 'ss_2')
        self.a3 = self.findChild(QLineEdit, 'ss_3')
        self.a4 = self.findChild(QLineEdit, 'ss_4')
        self.a5 = self.findChild(QLineEdit, 'ss_5')
        self.a6 = self.findChild(QLineEdit, 'ss_6')
        self.a7 = self.findChild(QLineEdit, 'ss_7')

        self.i1 = self.findChild(QLineEdit, 'sa')
        self.i2 = self.findChild(QLineEdit, 'sa_2')
        self.i3 = self.findChild(QLineEdit, 'sa_3')
        self.i4 = self.findChild(QLineEdit, 'sa_4')
        self.i5 = self.findChild(QLineEdit, 'sa_5')
        self.i6 = self.findChild(QLineEdit, 'sa_6')
        self.i7 = self.findChild(QLineEdit, 'sa_7')
        # DENMARK
        self.d1 = self.findChild(QLineEdit, 'dd')
        self.d2 = self.findChild(QLineEdit, 'dd_2')
        self.d3 = self.findChild(QLineEdit, 'dd_3')
        self.d4 = self.findChild(QLineEdit, 'dd_4')
        self.d5 = self.findChild(QLineEdit, 'dd_5')
        self.d6 = self.findChild(QLineEdit, 'dd_6')
        self.d7 = self.findChild(QLineEdit, 'dd_7')

        self.k1 = self.findChild(QLineEdit, 'dn')
        self.k2 = self.findChild(QLineEdit, 'dn_2')
        self.k3 = self.findChild(QLineEdit, 'dn_3')
        self.k4 = self.findChild(QLineEdit, 'dn_4')
        self.k5 = self.findChild(QLineEdit, 'dn_5')
        self.k6 = self.findChild(QLineEdit, 'dn_6')
        self.k7 = self.findChild(QLineEdit, 'dn_7')
        # SWEDEN
        self.sd1 = self.findChild(QLineEdit, 'sd')
        self.sd2 = self.findChild(QLineEdit, 'sd_2')
        self.sd3 = self.findChild(QLineEdit, 'sd_3')
        self.sd4 = self.findChild(QLineEdit, 'sd_4')
        self.sd5 = self.findChild(QLineEdit, 'sd_5')
        self.sd6 = self.findChild(QLineEdit, 'sd_6')

        self.sf1 = self.findChild(QLineEdit, 'sf')
        self.sf2 = self.findChild(QLineEdit, 'sf_2')
        self.sf3 = self.findChild(QLineEdit, 'sf_3')
        self.sf4 = self.findChild(QLineEdit, 'sf_4')
        self.sf5 = self.findChild(QLineEdit, 'sf_5')
        self.sf6 = self.findChild(QLineEdit, 'sf_6')
        # NORWAY
        self.nr1 = self.findChild(QLineEdit, 'nr')
        self.nr2 = self.findChild(QLineEdit, 'nr_2')
        self.nr3 = self.findChild(QLineEdit, 'nr_3')
        self.nr4 = self.findChild(QLineEdit, 'nr_4')
        self.nr5 = self.findChild(QLineEdit, 'nr_5')

        self.nt1 = self.findChild(QLineEdit, 'nt')
        self.nt2 = self.findChild(QLineEdit, 'nt_2')
        self.nt3 = self.findChild(QLineEdit, 'nt_3')
        self.nt4 = self.findChild(QLineEdit, 'nt_4')
        self.nt5 = self.findChild(QLineEdit, 'nt_5')
        # RIYAL SAUDI
        self.ry1 = self.findChild(QLineEdit, 'ry')
        self.ry2 = self.findChild(QLineEdit, 'ry_2')
        self.ry3 = self.findChild(QLineEdit, 'ry_3')
        self.ry4 = self.findChild(QLineEdit, 'ry_4')
        self.ry5 = self.findChild(QLineEdit, 'ry_5')
        self.ry6 = self.findChild(QLineEdit, 'ry_6')
        self.ry7 = self.findChild(QLineEdit, 'ry_7')

        self.re1 = self.findChild(QLineEdit, 're')
        self.re2 = self.findChild(QLineEdit, 're_2')
        self.re3 = self.findChild(QLineEdit, 're_3')
        self.re4 = self.findChild(QLineEdit, 're_4')
        self.re5 = self.findChild(QLineEdit, 're_5')
        self.re6 = self.findChild(QLineEdit, 're_6')
        self.re7 = self.findChild(QLineEdit, 're_7')
        # KUWAIT
        self.qw1 = self.findChild(QLineEdit, 'qw')
        self.qw2 = self.findChild(QLineEdit, 'qw_2')
        self.qw3 = self.findChild(QLineEdit, 'qw_3')
        self.qw4 = self.findChild(QLineEdit, 'qw_4')
        self.qw5 = self.findChild(QLineEdit, 'qw_5')
        self.qw6 = self.findChild(QLineEdit, 'qw_6')

        self.qx1 = self.findChild(QLineEdit, 'qx')
        self.qx2 = self.findChild(QLineEdit, 'qx_2')
        self.qx3 = self.findChild(QLineEdit, 'qx_3')
        self.qx4 = self.findChild(QLineEdit, 'qx_4')
        self.qx5 = self.findChild(QLineEdit, 'qx_5')
        self.qx6 = self.findChild(QLineEdit, 'qx_6')
        # QATAR
        self.qt1 = self.findChild(QLineEdit, 'qt')
        self.qt2 = self.findChild(QLineEdit, 'qt_2')
        self.qt3 = self.findChild(QLineEdit, 'qt_3')
        self.qt4 = self.findChild(QLineEdit, 'qt_4')
        self.qt5 = self.findChild(QLineEdit, 'qt_5')
        self.qt6 = self.findChild(QLineEdit, 'qt_6')

        self.qr1 = self.findChild(QLineEdit, 'qr')
        self.qr2 = self.findChild(QLineEdit, 'qr_2')
        self.qr3 = self.findChild(QLineEdit, 'qr_3')
        self.qr4 = self.findChild(QLineEdit, 'qr_4')
        self.qr5 = self.findChild(QLineEdit, 'qr_5')
        self.qr6 = self.findChild(QLineEdit, 'qr_6')
        # BAHRAIN
        self.bh1 = self.findChild(QLineEdit, 'bh')
        self.bh2 = self.findChild(QLineEdit, 'bh_2')
        self.bh3 = self.findChild(QLineEdit, 'bh_3')
        self.bh4 = self.findChild(QLineEdit, 'bh_4')
        self.bh5 = self.findChild(QLineEdit, 'bh_5')
        self.bh6 = self.findChild(QLineEdit, 'bh_6')

        self.bn1 = self.findChild(QLineEdit, 'bn')
        self.bn2 = self.findChild(QLineEdit, 'bn_2')
        self.bn3 = self.findChild(QLineEdit, 'bn_3')
        self.bn4 = self.findChild(QLineEdit, 'bn_4')
        self.bn5 = self.findChild(QLineEdit, 'bn_5')
        self.bn6 = self.findChild(QLineEdit, 'bn_6')
        # YENS
        self.yn1 = self.findChild(QLineEdit, 'yn')
        self.yn2 = self.findChild(QLineEdit, 'yn_2')
        self.yn3 = self.findChild(QLineEdit, 'yn_3')
        self.yn4 = self.findChild(QLineEdit, 'yn_4')
        self.yn5 = self.findChild(QLineEdit, 'yn_5')
        self.yn6 = self.findChild(QLineEdit, 'yn_6')
        self.yn7 = self.findChild(QLineEdit, 'yn_7')

        self.yj1 = self.findChild(QLineEdit, 'yj')
        self.yj2 = self.findChild(QLineEdit, 'yj_2')
        self.yj3 = self.findChild(QLineEdit, 'yj_3')
        self.yj4 = self.findChild(QLineEdit, 'yj_4')
        self.yj5 = self.findChild(QLineEdit, 'yj_5')
        self.yj6 = self.findChild(QLineEdit, 'yj_6')
        self.yj7 = self.findChild(QLineEdit, 'yj_7')
        # AED
        self.aed1 = self.findChild(QLineEdit, 'aed')
        self.aed2 = self.findChild(QLineEdit, 'aed_2')
        self.aed3 = self.findChild(QLineEdit, 'aed_3')
        self.aed4 = self.findChild(QLineEdit, 'aed_4')
        self.aed5 = self.findChild(QLineEdit, 'aed_5')
        self.aed6 = self.findChild(QLineEdit, 'aed_6')
        self.aed7 = self.findChild(QLineEdit, 'aed_7')
        self.aed8 = self.findChild(QLineEdit, 'aed_8')

        self.azd1 = self.findChild(QLineEdit, 'azd')
        self.azd2 = self.findChild(QLineEdit, 'azd_2')
        self.azd3 = self.findChild(QLineEdit, 'azd_3')
        self.azd4 = self.findChild(QLineEdit, 'azd_4')
        self.azd5 = self.findChild(QLineEdit, 'azd_5')
        self.azd6 = self.findChild(QLineEdit, 'azd_6')
        self.azd7 = self.findChild(QLineEdit, 'azd_7')
        self.azd8 = self.findChild(QLineEdit, 'azd_8')
        # EURO TEXT CHANGED
        self.l200.textChanged.connect(lambda: self.calculate_euro(self.l200, self.o200, 500))
        self.l100.textChanged.connect(lambda: self.calculate_euro(self.l100, self.o100, 200))
        self.l50.textChanged.connect(lambda: self.calculate_euro(self.l50, self.o50, 100))
        self.l20.textChanged.connect(lambda: self.calculate_euro(self.l20, self.o20, 50))
        self.l10.textChanged.connect(lambda: self.calculate_euro(self.l10, self.o10, 20))
        self.l5.textChanged.connect(lambda: self.calculate_euro(self.l5, self.o5, 10))
        self.e5.textChanged.connect(lambda: self.calculate_euro(self.e5, self.o1, 5))

        self.combo.currentIndexChanged.connect(self.devise__)

        self.colse_btn.clicked.connect(lambda: self.close())
        self.minimize.clicked.connect(lambda: self.showMinimized())
        self.dec.clicked.connect(self.clear1)
        self.val.clicked.connect(self.val_db_d)
        self.up.clicked.connect(self.updateCour)
        self.add_d.clicked.connect(self.add_dev)
        self.back_.clicked.connect(lambda: self.stacked.setCurrentIndex(0))
        self.val_d_.clicked.connect(lambda: self.val_d_clicked())

        self.user.setText('Farouk')

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title_bar.mouseMoveEvent = moveWindow
        # EURO MOUSEPRESS
        self.l200.mousePressEvent = lambda _: self.showEuro(self.l200, 1)
        self.l100.mousePressEvent = lambda _: self.showEuro(self.l100, 2)
        self.l50.mousePressEvent = lambda _: self.showEuro(self.l50, 3)
        self.l20.mousePressEvent = lambda _: self.showEuro(self.l20, 4)
        self.l10.mousePressEvent = lambda _: self.showEuro(self.l10, 5)
        self.l5.mousePressEvent = lambda _: self.showEuro(self.l5, 6)
        self.e5.mousePressEvent = lambda _: self.showEuro(self.e5, 7)
        # AED
        self.testtt(self.aed1, self.azd1, 1000, ' AED')
        self.testtt(self.aed2, self.azd2, 500, ' AED')
        self.testtt(self.aed3, self.azd3, 200, ' AED')
        self.testtt(self.aed4, self.azd4, 100, ' AED')
        self.testtt(self.aed5, self.azd5, 50, ' AED')
        self.testtt(self.aed6, self.azd6, 20, ' AED')
        self.testtt(self.aed7, self.azd7, 10, ' AED')
        self.testtt(self.aed8, self.azd8, 5, ' AED')
        # YENS
        self.testtt(self.yn1, self.yj1, 10000, ' ¥')
        self.testtt(self.yn2, self.yj2, 5000, ' ¥')
        self.testtt(self.yn3, self.yj3, 2000, ' ¥')
        self.testtt(self.yn4, self.yj4, 1000, ' ¥')
        self.testtt(self.yn5, self.yj5, 500, ' ¥')
        self.testtt(self.yn6, self.yj6, 100, ' ¥')
        self.testtt(self.yn7, self.yj7, 50, ' ¥')
        # BAHRAIN
        self.testtt(self.bh1, self.bn1, 20, ' BD')
        self.testtt(self.bh2, self.bn2, 10, ' BD')
        self.testtt(self.bh3, self.bn3, 5, ' BD')
        self.testtt(self.bh4, self.bn4, 1, ' BD')
        self.testtt(self.bh5, self.bn5, 1 / 2, ' BD')
        # QATAR
        self.testtt(self.qt1, self.qr1, 500, ' QR')
        self.testtt(self.qt2, self.qr2, 100, ' QR')
        self.testtt(self.qt3, self.qr3, 50, ' QR')
        self.testtt(self.qt4, self.qr4, 10, ' QR')
        self.testtt(self.qt5, self.qr5, 5, ' QR')
        self.testtt(self.qt6, self.qr6, 1, ' QR')
        # KUWAIT
        self.testtt(self.qw1, self.qx1, 20, ' KWD')
        self.testtt(self.qw2, self.qx2, 10, ' KWD')
        self.testtt(self.qw3, self.qx3, 5, ' KWD')
        self.testtt(self.qw4, self.qx4, 1, ' KWD')
        self.testtt(self.qw5, self.qx5, 1 / 2, ' KWD')
        self.testtt(self.qw6, self.qx6, 1 / 4, ' KWD')
        # RIYAL SAUDI
        self.testtt(self.ry1, self.re1, 500, ' SAR')
        self.testtt(self.ry2, self.re2, 200, ' SAR')
        self.testtt(self.ry3, self.re3, 100, ' SAR')
        self.testtt(self.ry4, self.re4, 50, ' SAR')
        self.testtt(self.ry5, self.re5, 20, ' SAR')
        self.testtt(self.ry6, self.re6, 10, ' SAR')
        self.testtt(self.ry7, self.re7, 5, ' SAR')
        # NORWAY
        self.testtt(self.nr1, self.nt1, 1000, ' KRONES')
        self.testtt(self.nr2, self.nt2, 500, ' KRONES')
        self.testtt(self.nr3, self.nt3, 200, ' KRONES')
        self.testtt(self.nr4, self.nt4, 100, ' KRONES')
        self.testtt(self.nr5, self.nt5, 50, ' KRONES')
        # SWEDEN
        self.testtt(self.sd1, self.sf1, 1000, ' KR')
        self.testtt(self.sd2, self.sf2, 500, ' KR')
        self.testtt(self.sd3, self.sf3, 200, ' KR')
        self.testtt(self.sd4, self.sf4, 100, ' KR')
        self.testtt(self.sd5, self.sf5, 50, ' KR')
        self.testtt(self.sd6, self.sf6, 20, ' KR')
        # DENMARK
        self.testtt(self.d1, self.k1, 1000, ' DKK')
        self.testtt(self.d2, self.k2, 500, ' DKK')
        self.testtt(self.d3, self.k3, 200, ' DKK')
        self.testtt(self.d4, self.k4, 100, ' DKK')
        self.testtt(self.d5, self.k5, 50, ' DKK')
        self.testtt(self.d6, self.k6, 20, ' DKK')
        self.testtt(self.d7, self.k7, 10, ' DKK')
        # SWISS
        self.testtt(self.a1, self.i1, 1000, ' CHF')
        self.testtt(self.a2, self.i2, 500, ' CHF')
        self.testtt(self.a3, self.i3, 200, ' CHF')
        self.testtt(self.a4, self.i4, 100, ' CHF')
        self.testtt(self.a5, self.i5, 50, ' CHF')
        self.testtt(self.a6, self.i6, 20, ' CHF')
        self.testtt(self.a7, self.i7, 10, ' CHF')
        # GIBRALTAR
        self.testtt(self.g1, self.b1, 100, ' £')
        self.testtt(self.g2, self.b2, 50, ' £')
        self.testtt(self.g3, self.b3, 20, ' £')
        self.testtt(self.g4, self.b4, 10, ' £')
        self.testtt(self.g5, self.b5, 5, ' £')
        self.testtt(self.g6, self.b6, 2, ' £')
        self.testtt(self.g7, self.b7, 1, ' £')
        # STERLING
        self.testtt(self.s1, self.r1, 100, ' £')
        self.testtt(self.s2, self.r2, 50, ' £')
        self.testtt(self.s3, self.r3, 20, ' £')
        self.testtt(self.s4, self.r4, 10, ' £')
        self.testtt(self.s5, self.r5, 5, ' £')
        self.testtt(self.s6, self.r6, 2, ' £')
        self.testtt(self.s7, self.r7, 1, ' £')
        # CANADA
        self.testtt(self.c1, self.x1, 100, ' $')
        self.testtt(self.c2, self.x2, 50, ' $')
        self.testtt(self.c3, self.x3, 20, ' $')
        self.testtt(self.c4, self.x4, 10, ' $')
        self.testtt(self.c5, self.x5, 5, ' $')
        self.testtt(self.c6, self.x6, 2, ' $')
        self.testtt(self.c7, self.x7, 1, ' $')
        # USA
        self.testtt(self.u1, self.usd1, 100, ' $')
        self.testtt(self.u2, self.usd2, 50, ' $')
        self.testtt(self.u3, self.usd3, 20, ' $')
        self.testtt(self.u4, self.usd4, 10, ' $')
        self.testtt(self.u5, self.usd5, 5, ' $')
        self.testtt(self.u6, self.usd6, 2, ' $')
        self.testtt(self.u7, self.usd7, 1, ' $')
        # self.m = MyCursor()
        # self.m.mycursor.execute('SELECT name FROM Accounts')
        #
        # for x in self.m.mycursor.fetchall():
        #     self.acc_box.addItems(x)

        # self.usa
        # self.can
        # self.ster
        # self.gibra
        # self.suis
        # self.dan
        # self.sued
        # self.norv
        # self.riyal
        # self.eru
        # self.qatar
        # self.yens
        # self.bahr

        self.courtxt.setText('0')

        self.usa1 = 0.0
        self.can1 = 0.0
        self.ster1 = 0.0
        self.gibra1 = 0.0
        self.suis1 = 0.0
        self.dan1 = 0.0
        self.sued1 = 0.0
        self.norv1 = 0.0
        self.riyal1 = 0.0
        self.dinar1 = 0.0
        self.qatar1 = 0.0
        self.yens1 = 0.0
        self.bahr1 = 0.0
        self.aedd1 = 0.0
        self.c.btn_cls.clicked.connect(self.rrl)
        self.date = self.findChild(QLabel, 'date')
        self.time = self.findChild(QLabel, 'time')

        now = QDate.currentDate()
        self.date.setText(now.toString(Qt.ISODate))
        timer = QTimer(self)
        timer.timeout.connect(self.displaytime)
        timer.start(1000)

    #########################################################################################################
    def add_dev(self):
        self.stacked.setCurrentIndex(1)
        self.u1.setFocus()
        self.u1.selectAll()
    def displaytime(self):
        time = QTime.currentTime()
        self.time.setText(time.toString(Qt.DefaultLocaleLongDate))

    def rrl(self):
        self.cour = 0.0

    def testtt(self, y, x, m, t):
        y.textChanged.connect(lambda: self.cal_d(y, x, m, t))
        y.mousePressEvent = lambda _: y.selectAll()

    def val_d_clicked(self):
        self.usa1 = ((float(self.u1.text()) * 100) +
                     (float(self.u2.text()) * 50) +
                     (float(self.u3.text()) * 20) +
                     (float(self.u4.text()) * 10) +
                     (float(self.u5.text()) * 5) +
                     (float(self.u6.text()) * 2) +
                     (float(self.u7.text()) * 1))
        self.usa.setText(str("{:,.2f}".format(float(self.usa1)) + ' $'))

        self.can1 = ((float(self.c1.text()) * 100) +
                     (float(self.c2.text()) * 50) +
                     (float(self.c3.text()) * 20) +
                     (float(self.c4.text()) * 10) +
                     (float(self.c5.text()) * 5) +
                     (float(self.c6.text()) * 2) +
                     (float(self.c7.text()) * 1))
        self.can.setText(str("{:,.2f}".format(float(self.can1)) + ' $'))

        self.ster1 = (float(self.s1.text()) * 100) + \
                     (float(self.s2.text()) * 50) + \
                     (float(self.s3.text()) * 20) + \
                     (float(self.s4.text()) * 10) + \
                     (float(self.s5.text()) * 5) + \
                     (float(self.s6.text()) * 2) + \
                     (float(self.s7.text()) * 1)
        self.ster.setText(str("{:,.2f}".format(float(self.ster1)) + ' £'))

        self.gibra1 = (float(self.g1.text()) * 100) + \
                      (float(self.g2.text()) * 50) + \
                      (float(self.g3.text()) * 20) + \
                      (float(self.g4.text()) * 10) + \
                      (float(self.g5.text()) * 5) + \
                      (float(self.g6.text()) * 2) + \
                      (float(self.g7.text()) * 1)
        self.gibra.setText(str("{:,.2f}".format(float(self.gibra1)) + ' £'))

        self.suis1 = (float(self.a1.text()) * 100) + \
                     (float(self.a2.text()) * 50) + \
                     (float(self.a3.text()) * 20) + \
                     (float(self.a4.text()) * 10) + \
                     (float(self.a5.text()) * 5) + \
                     (float(self.a6.text()) * 2) + \
                     (float(self.a7.text()) * 1)
        self.suis.setText(str("{:,.2f}".format(float(self.suis1)) + ' franc'))

        self.dan1 = (float(self.d1.text()) * 1000) + \
                    (float(self.d2.text()) * 500) + \
                    (float(self.d3.text()) * 200) + \
                    (float(self.d4.text()) * 100) + \
                    (float(self.d5.text()) * 50) + \
                    (float(self.d6.text()) * 20) + \
                    (float(self.d7.text()) * 10)
        self.dan.setText(str("{:,.2f}".format(float(self.dan1)) + ' DKK'))

        self.sued1 = (float(self.sd1.text()) * 1000) + \
                     (float(self.sd2.text()) * 500) + \
                     (float(self.sd3.text()) * 200) + \
                     (float(self.sd4.text()) * 100) + \
                     (float(self.sd5.text()) * 50) + \
                     (float(self.sd6.text()) * 20)
        self.sued.setText(str("{:,.2f}".format(float(self.sued1)) + ' KR'))

        self.norv1 = (float(self.nr1.text()) * 1000) + \
                     (float(self.nr2.text()) * 500) + \
                     (float(self.nr3.text()) * 200) + \
                     (float(self.nr4.text()) * 100) + \
                     (float(self.nr5.text()) * 50)
        self.norv.setText(str("{:,.2f}".format(float(self.norv1)) + ' KRONE'))

        self.riyal1 = (float(self.ry1.text()) * 500) + \
                      (float(self.ry2.text()) * 200) + \
                      (float(self.ry3.text()) * 100) + \
                      (float(self.ry4.text()) * 50) + \
                      (float(self.ry5.text()) * 20) + \
                      (float(self.ry6.text()) * 10) + \
                      (float(self.ry7.text()) * 5)
        self.riyal.setText(str("{:,.2f}".format(float(self.riyal1)) + ' SAR'))

        self.dinar1 = (float(self.qw1.text()) * 20) + \
                      (float(self.qw2.text()) * 10) + \
                      (float(self.qw3.text()) * 5) + \
                      (float(self.qw4.text()) * 1) + \
                      (float(self.qw5.text()) * 1 / 2) + \
                      (float(self.qw6.text()) * 1 / 4)
        self.dinar.setText(str("{:,.2f}".format(float(self.dinar1)) + ' KWD'))

        self.qatar1 = (float(self.qt1.text()) * 500) + \
                      (float(self.qt2.text()) * 100) + \
                      (float(self.qt3.text()) * 50) + \
                      (float(self.qt4.text()) * 10) + \
                      (float(self.qt5.text()) * 5) + \
                      (float(self.qt6.text()) * 1)
        self.qatar.setText(str("{:,.2f}".format(float(self.qatar1)) + ' QR'))

        self.bahr1 = (float(self.bh1.text()) * 20) + \
                     (float(self.bh2.text()) * 10) + \
                     (float(self.bh3.text()) * 5) + \
                     (float(self.bh4.text()) * 1) + \
                     (float(self.bh5.text()) * 1 / 2)
        self.bahr.setText(str("{:,.2f}".format(float(self.bahr1)) + ' BD'))

        self.yens1 = (float(self.yn1.text()) * 10000) + \
                     (float(self.yn2.text()) * 5000) + \
                     (float(self.yn3.text()) * 2000) + \
                     (float(self.yn4.text()) * 1000) + \
                     (float(self.yn5.text()) * 500) + \
                     (float(self.yn6.text()) * 100) + \
                     (float(self.yn7.text()) * 50)
        self.yens.setText(str("{:,.2f}".format(float(self.yens1)) + ' ¥'))

        self.aedd1 = (float(self.aed1.text()) * 1000) + \
                     (float(self.aed2.text()) * 500) + \
                     (float(self.aed3.text()) * 200) + \
                     (float(self.aed4.text()) * 100) + \
                     (float(self.aed5.text()) * 50) + \
                     (float(self.aed6.text()) * 20) + \
                     (float(self.aed7.text()) * 10) + \
                     (float(self.aed8.text()) * 5)
        self.eru.setText(str("{:,.2f}".format(float(self.aedd1)) + ' AED'))

        self.val_d.setText('Devises ajoutés')
        self.unfade(self.val_d)
        self.fade(self.val_d)

    def cal_d(self, bill, o, x, y):
        if bill.text() == '':
            o.setText(f"0.00 {y}")
            bill.setText('0')
            bill.selectAll()
        else:
            self.r = float(bill.text()) * x
            e = "{:,.2f}".format(self.r)
            o.setText(e + y)

    def showEuro(self, devise, r):
        devise.selectAll()
        self.stacked3.setCurrentIndex(r)

    def devise__(self):
        if self.combo.currentText() == '$ U.S.A':
            self.stacked2.setCurrentIndex(0)
            self.u1.setFocus()
            self.u1.selectAll()
        elif self.combo.currentText() == '$ Canadien':
            self.stacked2.setCurrentIndex(1)
            self.c1.setFocus()
            self.c1.selectAll()
        elif self.combo.currentText() == '£ Sterling':
            self.stacked2.setCurrentIndex(2)
            self.s1.setFocus()
            self.s1.selectAll()
        elif self.combo.currentText() == '£ Gibraltar':
            self.stacked2.setCurrentIndex(3)
            self.g1.setFocus()
            self.g1.selectAll()
        elif self.combo.currentText() == 'Franc Suisse':
            self.stacked2.setCurrentIndex(4)
            self.a1.setFocus()
            self.a1.selectAll()
        elif self.combo.currentText() == 'C.Danoises':
            self.stacked2.setCurrentIndex(5)
            self.d1.setFocus()
            self.d1.selectAll()
        elif self.combo.currentText() == 'C.Suedoises':
            self.stacked2.setCurrentIndex(6)
            self.sd1.setFocus()
            self.sd1.selectAll()
        elif self.combo.currentText() == 'C.Norvegiennes':
            self.stacked2.setCurrentIndex(7)
            self.nr1.setFocus()
            self.nr1.selectAll()
        elif self.combo.currentText() == 'Riyal Saoudien':
            self.stacked2.setCurrentIndex(8)
            self.ry1.setFocus()
            self.ry1.selectAll()
        elif self.combo.currentText() == 'Dinar Koweitien':
            self.stacked2.setCurrentIndex(9)
            self.qw1.setFocus()
            self.qw1.selectAll()
        elif self.combo.currentText() == 'Dirham E.R.U':
            self.stacked2.setCurrentIndex(10)
            self.aed1.setFocus()
            self.aed1.selectAll()
        elif self.combo.currentText() == 'Riyal Qatari':
            self.stacked2.setCurrentIndex(11)
            self.qt1.setFocus()
            self.qt1.selectAll()
        elif self.combo.currentText() == 'Yens Japonais':
            self.stacked2.setCurrentIndex(12)
            self.yn1.setFocus()
            self.yn1.selectAll()
        elif self.combo.currentText() == 'Dinar Bahreini':
            self.stacked2.setCurrentIndex(13)
            self.bh1.setFocus()
            self.bh1.selectAll()

    def updateCour(self):
        self.c.show()

    def CourClose(self):
        if float(self.c.cour.text()) == 0:
            self.c.info.setText('Enter un cour valide!')

            self.cour = 0
        else:
            self.cour = float(self.c.cour.text())
            self.courtxt.setText(str("{:,.2f}".format(float(self.cour)) + ' DH'))
            self.c.info.clear()
            self.c.close()
            self.euro_cour()
            self.total_euro()
            self.exectute_euro()

    def fade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(10000)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    def unfade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(10000)
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
        self.e5.clear()

        self.usa.clear()
        self.can.clear()
        self.ster.clear()
        self.gibra.clear()
        self.suis.clear()
        self.dan.clear()
        self.sued.clear()
        self.norv.clear()
        self.riyal.clear()
        self.eru.clear()
        self.qatar.clear()
        self.yens.clear()
        self.bahr.clear()
        self.dinar.clear()

        self.fade(self.info)

    def euro_cour(self):
        total1 = float(self.l200.text()) * 500 + float(self.l100.text()) * 200 + float(self.l50.text()) * 100
        total2 = float(self.l20.text()) * 50 + float(self.l10.text()) * 20 + float(self.l5.text()) * 10
        total3 = float(self.e5.text()) * 5

        self.total12 = (total1 + total2 + total3) * float(self.cour)

        return self.total12

    def devise_total(self):
        self.devise = (float(self.usa.text()) +
                       float(self.can.text()) +
                       float(self.ster.text()) +
                       float(self.gibra.text()) +
                       float(self.suis.text()) +
                       float(self.dan.text()) +
                       float(self.sued.text()) +
                       float(self.norv.text()) +
                       float(self.riyal.text()) +
                       float(self.eru.text()) +
                       float(self.qatar.text()) +
                       float(self.yens.text()) +
                       float(self.bahr.text()) +
                       float(self.dinar.text()))

        return self.devise

    # 26
    def valider(self, date):

        s = self.total_euro()
        d = self.euro_cour()
        self.m = MyCursor()
        self.m.mycursor.execute("""INSERT INTO CaisseD (user,remarque,created,totalE,ExC,Cour,l500,l200,l100,l50,l20,
        l10,l5,us,can,ster,gib,suise,dan,sued,norv,riyal,dinar,eru,qatar,bahr,yens)
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                                (self.user.text(), self.remarque.toPlainText(), date,
                                 float(s), float(d), float(self.cour),
                                 int(self.l200.text()), int(self.l100.text()), int(self.l50.text()),
                                 int(self.l20.text()), int(self.l10.text()), int(self.l5.text()),
                                 int(self.e5.text()), int(self.usa1), int(self.can1), int(self.ster1), int(self.gibra1),
                                 int(self.suis1),
                                 int(self.dan1), int(self.sued1), int(self.norv1), int(self.riyal1), int(self.dinar1),
                                 int(self.aedd1), int(self.qatar1),
                                 int(self.bahr1), int(self.yens1),))

        self.m.db.commit()
        self.info.setText('Caisse ajouté!')
        self.unfade(self.info)
        self.fade(self.info)

    def val_db_d(self):
        time_r = datetime.now().strftime('%H-%M-%S')
        r = " ".join([self.date_d.text(), str(time_r)])
        date = datetime.strptime(r, '%d/%m/%Y %H-%M-%S')
        self.valider(date)

    def total_euro(self):
        total1 = float(self.l200.text()) * 500 + float(self.l100.text()) * 200 + float(self.l50.text()) * 100
        total2 = float(self.l20.text()) * 50 + float(self.l10.text()) * 20 + float(self.l5.text()) * 10
        total3 = float(self.e5.text()) * 5
        self.total = total1 + total2 + total3
        return self.total

    def exectute_euro(self):
        s = self.euro_cour()
        self.diff.setStyleSheet("""QLineEdit{border-radius:10px;
        color: rgb(0, 0, 0);}""")
        self.diff.setText(str("{:,.2f}".format(self.euro_cour())) + ' DH')

        self.caisseM.setText(str("{:,.2f}".format(self.total_euro())) + ' €')

    def calculate_euro(self, le, oe, x):
        if le.text() == '':
            oe.setText("0.00 €")
            le.setText('0')
            le.selectAll()
        else:
            self.r = float(le.text()) * x
            e = "{:,.2f}".format(self.r)
            oe.setText(e + ' €')
            self.exectute_euro()

    #
    def calculate_devise(self, lr):
        if lr.text() == '':
            lr.setText('0')
            lr.selectAll()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


class DetailsCaisseD(QWidget, Ui_details_D):
    def __init__(self, parent=None):
        super(DetailsCaisseD, self).__init__(parent)

        self.setupUi(self)
        self.setWindowIcon(QIcon("Untitled-2-01.ico"))
        self.setWindowTitle('Details DEVISE')
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        self.title = self.findChild(QFrame, 'title_bar')
        self.colse_btn = self.findChild(QPushButton, 'close_btn')
        self.minimize = self.findChild(QPushButton, 'mini')
        self.l200 = self.findChild(QLineEdit, 'l200')
        self.l100 = self.findChild(QLineEdit, 'l100')
        self.l50 = self.findChild(QLineEdit, 'l50')
        self.l20 = self.findChild(QLineEdit, 'l20')
        self.l10 = self.findChild(QLineEdit, 'l10')
        self.l5 = self.findChild(QLineEdit, 'l5')
        self.e5 = self.findChild(QLineEdit, 'l5_2')
        self.usa = self.findChild(QLineEdit, 'us')
        self.can = self.findChild(QLineEdit, 'canada')
        self.ster = self.findChild(QLineEdit, 'sterling')
        self.gibra = self.findChild(QLineEdit, 'gibra')
        self.suis = self.findChild(QLineEdit, 'suise')
        self.dan = self.findChild(QLineEdit, 'danoi')
        self.sued = self.findChild(QLineEdit, 'sued')
        self.norv = self.findChild(QLineEdit, 'norv')
        self.riyal = self.findChild(QLineEdit, 'riyal')
        self.dinar = self.findChild(QLineEdit, 'dinar')
        self.eru = self.findChild(QLineEdit, 'eru')
        self.qatar = self.findChild(QLineEdit, 'qatar')
        self.yens = self.findChild(QLineEdit, 'yens')
        self.bahr = self.findChild(QLineEdit, 'bahr')
        self.info = self.findChild(QLabel, 'info')
        self.frame3 = self.findChild(QFrame, 'frame_3')

        self.o200 = self.findChild(QLineEdit, 'o200')
        self.o100 = self.findChild(QLineEdit, 'o100')
        self.o50 = self.findChild(QLineEdit, 'o50')
        self.o20 = self.findChild(QLineEdit, 'o20')
        self.o10 = self.findChild(QLineEdit, 'o10')
        self.o5 = self.findChild(QLineEdit, 'o5')
        self.o1 = self.findChild(QLineEdit, 'o5_2')
        self.btn_prnt = self.findChild(QPushButton, 'print')

        self.caisseM = self.findChild(QLineEdit, 'caisseMAD')

        self.diff = self.findChild(QLineEdit, 'dif')
        self.val = self.findChild(QPushButton, 'val')
        self.user = self.findChild(QLabel, 'user')
        self.courtxt = self.findChild(QLineEdit, 'cour')
        self.remarque = self.findChild(QTextEdit, 'remarque')
        self.onlyInt = QIntValidator()
        self.l200.setValidator(self.onlyInt)
        self.l100.setValidator(self.onlyInt)
        self.l50.setValidator(self.onlyInt)
        self.l20.setValidator(self.onlyInt)
        self.l10.setValidator(self.onlyInt)
        self.l5.setValidator(self.onlyInt)
        self.e5.setValidator(self.onlyInt)
        self.colse_btn.clicked.connect(lambda: self.close())
        self.minimize.clicked.connect(lambda: self.showMinimized())
        self.user.setText('Farouk')

        self.btn_prnt.clicked.connect(self.handlePrint)

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title_bar.mouseMoveEvent = moveWindow
        self.l200.mousePressEvent = lambda _: self.showEuro(self.l200, 1)
        self.l100.mousePressEvent = lambda _: self.showEuro(self.l100, 2)
        self.l50.mousePressEvent = lambda _: self.showEuro(self.l50, 3)
        self.l20.mousePressEvent = lambda _: self.showEuro(self.l20, 4)
        self.l10.mousePressEvent = lambda _: self.showEuro(self.l10, 5)
        self.l5.mousePressEvent = lambda _: self.showEuro(self.l5, 6)
        self.e5.mousePressEvent = lambda _: self.showEuro(self.e5, 7)
        self.date = self.findChild(QLabel, 'date')
        self.time = self.findChild(QLabel, 'time')

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
        # Draw grabbed pixmap
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawImage(0, 0, QImage('details_c_d-01.jpg'))

        painter.setPen(QColor(0, 0, 0))
        painter.setFont(QFont('Mongolian Baiti', 12))

        rem = self.remarque.toPlainText()

        painter.drawPixmap(170, 30, self.date.grab())
        painter.drawPixmap(170, 60, self.time.grab())
        painter.drawPixmap(170, 85, self.user.grab())

        painter.drawPixmap(120, 170, self.l200.grab())
        painter.drawPixmap(120, 220, self.l100.grab())
        painter.drawPixmap(120, 270, self.l50.grab())
        painter.drawPixmap(120, 320, self.l20.grab())
        painter.drawPixmap(120, 370, self.l10.grab())
        painter.drawPixmap(120, 420, self.l5.grab())
        painter.drawPixmap(120, 470, self.l5_2.grab())

        painter.drawPixmap(220, 170, self.o200.grab())
        painter.drawPixmap(220, 220, self.o100.grab())
        painter.drawPixmap(220, 270, self.o50.grab())
        painter.drawPixmap(220, 320, self.o20.grab())
        painter.drawPixmap(220, 370, self.o10.grab())
        painter.drawPixmap(220, 420, self.o5.grab())
        painter.drawPixmap(220, 470, self.o5_2.grab())

        painter.drawPixmap(550, 190, self.us.grab())
        painter.drawPixmap(550, 240, self.canada.grab())
        painter.drawPixmap(550, 290, self.sterling.grab())
        painter.drawPixmap(550, 340, self.gibra.grab())
        painter.drawPixmap(550, 390, self.suis.grab())
        painter.drawPixmap(550, 440, self.sued.grab())
        painter.drawPixmap(550, 490, self.danoi.grab())

        painter.drawPixmap(820, 190, self.norv.grab())
        painter.drawPixmap(820, 240, self.riyal.grab())
        painter.drawPixmap(820, 290, self.dinar.grab())
        painter.drawPixmap(820, 340, self.eru.grab())
        painter.drawPixmap(820, 390, self.qatar.grab())
        painter.drawPixmap(820, 440, self.bahr.grab())
        painter.drawPixmap(820, 490, self.yens.grab())

        painter.drawPixmap(90, 600, self.caisseMAD.grab())
        painter.drawPixmap(390, 600, self.dif.grab())
        painter.drawPixmap(690, 590, self.cour.grab())

        painter.drawText(195, 680, str(rem))
        painter.drawText(710, 720, self.identif.text())

        # End painting
        painter.end()
        self.info.setText('Caisse Devise imprimée!')

    def showEuro(self, devise, r):
        devise.selectAll()
        self.stacked3.setCurrentIndex(r)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = CaisseD()
    window.show()
    sys.exit(app.exec())
