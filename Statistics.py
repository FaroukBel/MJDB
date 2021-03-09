__author__ = "Farouk BEL KHYATE"
__copyright__ = "Copyright (C) 2020 FAROUK BEL KHYATE"
__license__ = "MJDB ESK2 S.A.R.L"
__version__ = "1.0"

from PyQt5 import QtWidgets, QtGui, QtCore, QtPrintSupport
from PyQt5.QtCore import QTime, Qt, QTimer
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from datetime import datetime, timedelta
from add_colab import AddCollab
from add_acc import AddAcc
from database import MyCursor
from add_ops import AddOps
from graph import MplCanvas
from caiss_MAD import CaisseMad, DetailsCaisseMad
from caiss_D import CaisseD, DetailsCaisseD
from annulation import Motif, MotifOps
from delt_acc import DeletedAccs
from pop_up import Date
from statis import Ui_MainWindow
from operator import add, sub
import mpld3
import xlsxwriter

# GLOBALS
GLOBAL_STATE = 0
DEFAULT_STATE1 = 0
DEFAULT_STATE2 = 0
DEFAULT_STATE3 = 0
DEFAULT_STATE4 = 0
SWITCH = 0
SWITCH_2 = 0


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)
        self.setWindowIcon(QIcon('MJDB_ICON.ico'))
        self.setWindowTitle('Statistiques')
        self.a = AddOps()
        self.d = Date()
        self.d.new_op.clicked.connect(lambda: self.val_date_today())

        self.d.show()
        self.m = MyCursor()

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)

        self.set_max = self.findChild(QPushButton, 'mini_2')
        self.add_colab = self.findChild(QAction, 'actionCollaborateurs')
        self.add_acc = self.findChild(QAction, "actionComptes")
        self.time = self.findChild(QLabel, "time")
        self.date = self.findChild(QLabel, "date")
        self.acc_box = self.findChild(QComboBox, "acc_box")
        self.acc_box2 = self.findChild(QComboBox, 'acc_box_2')
        self.dateedit = self.findChild(QDateEdit, 'dateEdit')
        self.dateedit_2 = self.findChild(QDateEdit, 'dateEdit_2')
        self.pr = self.findChild(QAction, 'actionEnregisterer')
        self.g_ballance = self.findChild(QLineEdit, 'b_sc')
        self.g_ballance_ = self.findChild(QLineEdit, 'b_g')
        self.general = self.findChild(QLineEdit, 'general_b')
        self.b_table = self.findChild(QTableWidget, 'acc_balance')
        self.graph = self.findChild(QRadioButton, 'graph')
        self.table = self.findChild(QRadioButton, 'table')
        self.stack = self.findChild(QStackedWidget, 'stackedWidget')
        self.title_bar = self.findChild(QFrame, 'title_bar')
        self.close_btn = self.findChild(QPushButton, 'close_btn')
        self.minimize = self.findChild(QPushButton, 'mini')
        self.c_MAD = self.findChild(QAction, 'actionCaisse_DH')
        self.a_D = self.findChild(QAction, 'actionCaisse_DEVISE')
        self.cM = self.findChild(QRadioButton, 'cM')
        self.cBox = self.findChild(QRadioButton, 'cBox')
        self.c_table = self.findChild(QTableWidget, 'ops_table_2')
        self.central_ = self.findChild(QWidget, 'centralwidget')
        self.deletedOps = self.findChild(QRadioButton, 'deletedops')
        self.stacked2 = self.findChild(QStackedWidget, 'stacked2')
        self.motif = self.findChild(QPushButton, 'new_op_2')
        self.caisse_details = self.findChild(QPushButton, 'details')
        self.stacked3 = self.findChild(QStackedWidget, 'stacked3')
        self.devise_table = self.findChild(QTableWidget, 'devise_table')
        self.cR = self.findChild(QRadioButton, 'cR')
        self.details_D = self.findChild(QPushButton, 'details_D')

        self.add_colab.triggered.connect(self.clicked_add)
        self.add_acc.triggered.connect(self.clicked_add_acc)
        self.actionImprimer.triggered.connect(self.handlePrint)
        self.actionExporter_2.triggered.connect(self.savefile)
        self.actionComptes_supprim.triggered.connect(self.deleted_acc_clicked)
        self.actionChanger_la_date.triggered.connect(self.change_date_trigger)

        self.new_op.clicked.connect(self.clicked_add_ops)
        self.pr.triggered.connect(self.prii)
        self.close_btn.clicked.connect(lambda: self.close())
        self.minimize.clicked.connect(lambda: self.showMinimized())
        self.c_MAD.triggered.connect(self.caisse_M)
        self.a_D.triggered.connect(self.caisseD)
        self.set_max.clicked.connect(self.maximize_restored)
        self.motif.clicked.connect(self.motif_clicked)
        self.caisse_details.clicked.connect(self.details_clicked_c)
        self.details_D.clicked.connect(self.details_D_pop)
        self.remarque_btn.clicked.connect(self.remarque_ops)
        self.remarque_btn_3.clicked.connect(self.handlePrint_recus)

        self.user.setText('Farouk')

        now = datetime.now().date()
        self.date.setText(datetime.now().date().strftime('%d/%m/%Y'))
        timer = QTimer(self)
        timer.timeout.connect(self.displaytime)
        timer.start(1000)

        self.dateedit.setDate(now - timedelta(1))
        self.dateedit_2.setDate(now + timedelta(1))
        self.dateedit.setMaximumDate(now)
        self.dateedit_2.setMaximumDate(now + timedelta(1))

        self.m.mycursor.execute('SELECT name FROM Accounts')

        for x in self.m.mycursor.fetchall():
            self.acc_box.addItems(x)
        self.acc_box.insertItem(0, 'Tout')

        self.a = AddAcc()
        self.acc_box.currentIndexChanged.connect(self.repeat)
        self.acc_box2.currentIndexChanged.connect(self.repeat_)
        self.dateedit.dateChanged.connect(self.date_changed)
        self.dateedit_2.dateChanged.connect(self.date_changed)

        self.con.toggled.connect(self.con_)
        self.non_con.toggled.connect(self.non_con_)
        self.con_non_con.toggled.connect(self.con_non_con_)
        self.graph.toggled.connect(self.graph_)
        self.table.toggled.connect(self.table_)
        self.cBox.toggled.connect(self.cBox_)
        self.cM.toggled.connect(self.rCaisseM)
        self.deletedOps.toggled.connect(self.deletedOps_)
        self.cR.toggled.connect(self.caisse_devise_check)
        self.graph_day.toggled.connect(self.year_m_d)
        self.graph_month.toggled.connect(self.year_m_d)
        self.graph_year.toggled.connect(self.year_m_d)

        self.con_non_con.setChecked(True)
        self.table.setChecked(True)
        self.cBox.setChecked(True)
        self.graph_day.setChecked(True)

        self.b_table.setSortingEnabled(False)
        self.ops_table.setSortingEnabled(False)
        self.c_table.setSortingEnabled(False)
        self.devise_table.setSortingEnabled(False)

        self.m.mycursor.execute("SELECT SUM(debit) FROM Ops WHERE type IN ('C', 'C / Annulation')")
        result4 = self.m.mycursor.fetchone()[0]

        self.m.mycursor.execute("SELECT SUM(credit) FROM Ops WHERE type IN ('C', 'C / Annulation')")
        result5 = self.m.mycursor.fetchone()[0]
        if result4 is None and result5 is None:
            pass
        else:
            re = result4 + result5
            formatted_re = "{:,.2f}".format(re)
            if re < 0:
                self.general.setStyleSheet("""QLineEdit{border-radius:10px;
                                                       color:rgb(255, 0, 0);}""")
                self.general.setText(formatted_re + ' DH')
            elif re > 0:
                self.general.setStyleSheet("""QLineEdit{border-radius:10px;
                                                       color:rgb(0, 170, 0);}""")
                self.general.setText(formatted_re + ' DH')
            elif re == 0:
                self.general.setStyleSheet("""QLineEdit{border-radius:10px;
                                                       color:rgb(0, 0, 0);}""")
                self.general.setText(formatted_re + ' DH')

        self.m.mycursor.execute(
            """SELECT name, balance FROM Accounts ORDER BY balance ASC""")
        f = self.m.mycursor.fetchall()
        self.b_table.setRowCount(0)
        for column_number, row_data in enumerate(f):
            self.b_table.insertRow(column_number)
            for row_number, data in enumerate(row_data):
                self.b_table.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
        for x in range(self.b_table.rowCount()):
            g = float(self.b_table.item(x, 1).text())
            if g < 0:
                formatted_float_debit = "{:,.2f}".format(g)
                self.b_table.setItem(x, 1, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH')))
                self.b_table.item(x, 1).setForeground(QtGui.QColor(255, 0, 0))
            elif g > 0:
                formatted_float_debit = "{:,.2f}".format(g)
                self.b_table.setItem(x, 1, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH')))
                self.b_table.item(x, 1).setForeground(QtGui.QColor(0, 170, 0))
            elif g == 0:
                formatted_float_debit = "{:,.2f}".format(g)
                self.b_table.setItem(x, 1, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH')))
                self.b_table.item(x, 1).setForeground(QtGui.QColor(0, 0, 0))

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton and not self.isMaximized():
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title_bar.mouseMoveEvent = moveWindow

        self.b_table.horizontalHeader().sortIndicatorChanged.connect(lambda: self.BalSorted(self.b_table, num=1))
        self.ops_table.horizontalHeader().sectionClicked.connect(self.onHeaderClicked)
        self.c_table.horizontalHeader().sectionClicked.connect(self.onHeaderClicked2)
        self.devise_table.horizontalHeader().sectionClicked.connect(self.onHeaderClicked3)

        self.stacked3.setCurrentIndex(2)
        # TOOL TIPS
        self.close_btn.setToolTip("Fermer")
        self.set_max.setToolTip("Agrandir")
        self.minimize.setToolTip("Réduire")
        # CELL CLICKED
        self.ops_table.cellClicked.connect(self.cell_is_clicked)
        self.c_table.cellClicked.connect(self.cell_clicked_c)
        self.devise_table.cellClicked.connect(self.cell_clicked_d)
        self.b_table.cellClicked.connect(self.cell_ballance_clicked)
        # TABLE FILL
        global SWITCH
        SWITCH = 2
        self.fill_all_ops()

        self.title_bar.installEventFilter(self)
        self.filedig = QFileDialog()
        self._opt = QStyleOptionViewItem()

        self.reference.textChanged.connect(self.reference_text_changed)
        self.colab.textChanged.connect(self.collab_text_changed)

    ####################################################################################################################
    def year_m_d(self):
        if self.cR.isChecked():
            if self.graph_year.isChecked():
                self.devise_graph('year(created)')
            elif self.graph_month.isChecked():
                self.devise_graph('year(created),month(created)')
            elif self.graph_day.isChecked():
                self.devise_graph('DATE(created)')
        elif self.cBox.isChecked():
            if self.graph_year.isChecked():
                self.BalGraph('year(created)')
            elif self.graph_month.isChecked():
                self.BalGraph('year(created),month(created)')
            elif self.graph_day.isChecked():
                self.BalGraph('DATE(created)')

    def change_date_trigger(self):
        self.d = Date()
        self.d.show()
        self.d.new_op.clicked.connect(lambda: self.val_date_today())
    
    def collab_text_changed(self):
        if self.table.isChecked() and self.cBox.isChecked():
            date_text = self.dateedit.text()
            date_text2 = self.dateedit_2.text()
            self.m.mycursor.execute(
                f"""SELECT  created, acc, opID, reference, userID, type ,debit, credit, motif FROM Ops WHERE
                        userID=%s and created between %s and %s""", (self.colab.text(), date_text, date_text2))
            f = self.m.mycursor.fetchall()

            self.ops_table.setRowCount(0)
            for column_number, row_data in enumerate(f):
                self.ops_table.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.ops_table.setItem(column_number, row_number, item)

            self.style_opTable()

            self.stack.insertWidget(0, self.ops_table)
            self.stack.setCurrentIndex(0)

    def reference_text_changed(self):
        if self.table.isChecked() and self.cBox.isChecked():
            self.m.mycursor.execute(
                f"""SELECT  created, acc, opID, reference, userID, type ,debit, credit, motif FROM Ops WHERE
                    reference=%s""", (self.reference.text(),))
            f = self.m.mycursor.fetchall()

            self.ops_table.setRowCount(0)
            for column_number, row_data in enumerate(f):
                self.ops_table.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.ops_table.setItem(column_number, row_number, item)
            self.style_opTable()
            self.stack.insertWidget(0, self.ops_table)
            self.stack.setCurrentIndex(0)

    def handlePrint_recus(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QtPrintSupport.QPrintDialog(printer, self)

        if dialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:
            self.handlePaintRequest_recus()

    def handlePaintRequest_recus(self):

        rows = self.ops_table.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi0 = self.ops_table.item(row, 1)
                self.twi8 = self.ops_table.item(row, 3)
                self.twi16 = self.ops_table.item(row, 4)
                self.twi32 = self.ops_table.item(row, 0)
                self.twi64 = self.ops_table.item(row, 5)
                self.twi128 = self.ops_table.item(row, 6)
                self.twi256 = self.ops_table.item(row, 7)
                self.soldecom = self.ops_table.item(row, 8)
                self.soldescom = self.ops_table.item(row, 9)

        datetime2 = datetime.now().date().strftime('%d/%m/%Y')
        datetime1 = datetime.now().strftime('%H:%M:%S')

        self.m.mycursor.execute("""SELECT acc FROM Ops WHERE reference=%s""", (self.twi8.text(),))
        acc_name = self.m.mycursor.fetchone()[0]

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
        painter.drawText(15, 320, acc_name)
        painter.drawText(15, 425, self.twi0.text())
        painter.drawText(500, 330, self.twi8.text())
        painter.drawText(560, 372, self.twi32.text())
        painter.drawText(455, 417, self.twi64.text())
        painter.drawText(850, 417, self.twi16.text())
        painter.drawText(15, 375, self.soldecom.text())
        painter.drawText(15, 485, self.soldescom.text())
        painter.setFont(QFont(font))
        painter.drawText(405, 525, self.twi128.text())
        painter.drawText(705, 525, self.twi256.text())

        painter.end()

    def deleted_acc_clicked(self):
        self.d = DeletedAccs()
        self.d.show()
        self.d.user.setText(self.user.text())

    def fill_all_ops(self, t1="C / Annulation", t2="C/NC / Annulation", t3="C", t4="NC", col='debit', order='DESC'):
        date_text = self.dateedit.text()
        date_text2 = self.dateedit_2.text()
        self.m.mycursor.execute(
            f"""SELECT  created, acc, opID, reference, userID, type ,debit, credit, soldeCompte, soldeSCompte, motif FROM Ops WHERE
                                    type IN(%s,%s,%s,%s) and created between %s and %s ORDER BY {col} {order}""",
            (t1, t2, t3, t4, date_text, date_text2))
        f = self.m.mycursor.fetchall()

        self.ops_table.setRowCount(0)
        for column_number, row_data in enumerate(f):
            self.ops_table.insertRow(column_number)
            for row_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                self.ops_table.setItem(column_number, row_number, item)
        self.style_opTable()

    def resume2_(self):
        rows = self.b_table.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi7 = self.b_table.item(row, 0)
        if self.deletedOps.isChecked():
            self.Op_checked((self.con.text() + ' / Annulation'), (self.non_con.text() + ' / Annulation'), '', '',
                            '',
                            'acc', self.twi7.text())
        else:
            self.Op_checked((self.con.text() + ' / Annulation'), (self.non_con.text() + ' / Annulation'),
                            self.con.text(), self.non_con.text(),
                            '',
                            'acc', self.twi7.text())

    def resume2_c(self):
        rows = self.b_table.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi7 = self.b_table.item(row, 0)
        if self.deletedOps.isChecked():
            self.Op_checked('', (self.con.text() + ' / Annulation'), '', '', '', 'acc', self.twi7.text())

        else:
            self.type = self.con.text()
            self.Op_checked(self.type, (self.con.text() + ' / Annulation'), '', '', '', 'acc',
                            self.twi7.text())

    def resume2_nc(self):
        rows = self.b_table.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi7 = self.b_table.item(row, 0)
        if self.deletedOps.isChecked():
            self.Op_checked('', (self.non_con.text() + ' / Annulation'), '', '', '', 'acc', self.twi7.text())
        else:
            self.type = self.non_con.text()
            self.Op_checked(self.type, (self.non_con.text() + ' / Annulation'), '', '', '', 'acc',
                            self.twi7.text())

    def Op_checked(self, OpType, Optyp, stype, thtype, type_, all_, all_type):
        if self.table.isChecked() and self.cBox.isChecked():
            date_text = self.dateedit.text()
            date_text2 = self.dateedit_2.text()
            self.m = MyCursor()
            self.m.mycursor.execute(
                f"""SELECT  created, acc, opID, reference, userID, type ,debit, credit, soldeCompte, soldeSCompte, motif FROM Ops WHERE
                 {all_}=%s and type IN (%s, %s, %s, %s) and created between %s and %s {type_}""",
                (all_type, OpType, Optyp, stype, thtype, date_text, date_text2))
            f = self.m.mycursor.fetchall()

            self.ops_table.setRowCount(0)
            for column_number, row_data in enumerate(f):
                self.ops_table.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.ops_table.setItem(column_number, row_number, item)

            self.style_opTable()

            self.stack.insertWidget(0, self.ops_table)
            self.stack.setCurrentIndex(0)

    def cell_ballance_clicked(self):
        global SWITCH
        SWITCH = 1
        if self.con.isChecked():
            self.resume2_c()
        elif self.non_con.isChecked():
            self.resume2_nc()
        elif self.con_non_con.isChecked():
            self.resume2_()

    def handlePrint(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QtPrintSupport.QPrintDialog(printer, self)

        if dialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:
            if self.cBox.isChecked():
                self.handlePaintRequest(self.ops_table)
            elif self.cR.isChecked():
                self.handlePaintRequest(self.devise_table)
            elif self.cM.isChecked():
                self.handlePaintRequest(self.c_table)

    def handlePaintRequest(self, table):
        if table.item(0, 0) is not None:
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOrientation(getattr(QPrinter, "Landscape"))
            printer.setPaperSize(QPrinter.A4)
            printer.setFullPage(True)
            printer.setPageMargins(1, 1, 1, 1, QPrinter.Millimeter)

            document = QtGui.QTextDocument()
            font = QFont('Mongolian Baiti')
            font.setPointSize(11)
            document.setDocumentMargin(0)
            document.setDefaultFont(QFont(font))
            cursor = QtGui.QTextCursor(document)

            centerAlignment = QtGui.QTextBlockFormat()
            centerAlignment.setAlignment(QtCore.Qt.AlignHCenter)
            centerAlignment.setAlignment(QtCore.Qt.AlignVCenter)

            table_format = QTextTableFormat()
            table_format.setAlignment(Qt.AlignHCenter)
            table_format.setCellPadding(10)
            table_format.setCellSpacing(0)
            table_format.setBorderBrush(QBrush(Qt.SolidPattern))

            table1 = cursor.insertTable(table.rowCount() + 1, table.columnCount(), table_format)

            fmt = table1.format()
            fmt.setWidth(QtGui.QTextLength(QtGui.QTextLength.PercentageLength, 100))
            table1.setFormat(fmt)

            try:

                headers = []
                for column in range(table.columnCount()):
                    header = table.horizontalHeaderItem(column)
                    if header is not None:
                        headers.append(header.text())
                    else:
                        headers.append("Column " + str(column))
                    cursor.insertText(header.text())
                    backgroundFormat = QTextBlockFormat()
                    backgroundFormat.setBackground(QColor("lightGreen"))
                    cursor.setBlockFormat(backgroundFormat)
                    cursor.movePosition(QtGui.QTextCursor.NextCell)
                for row in range(0, table1.rows()):
                    for col in range(table1.columns()):

                        it = table.item(row, col)
                        if it is not None:
                            cursor.insertText(it.text())
                        cursor.setBlockFormat(centerAlignment)
                        cursor.movePosition(QtGui.QTextCursor.NextCell)

                document.print_(printer)
                painter = QPainter()
                painter.setPen(QColor('black'))
                document.drawContents(painter)
                painter.save()
                document.adjustSize()

            except Exception:
                msg = QMessageBox()
                msg.setWindowTitle('Erreur')
                msg.setText("Erreur inconnu!")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Erreur')
            msg.setText("Veillez selectionnez un compte")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

    def prii(self):
        date = datetime.now()
        filename = date.strftime('%d-%m-%Y  %H-%M-%S')
        screen1 = QScreen.grabWindow(QApplication.primaryScreen(), QApplication.activeWindow().winId())
        img, _ = QFileDialog.getSaveFileName(self, "Enregistre-sous...", filename,
                                             filter="PNG(*.png);; JPEG(*.jpg)")
        if img[-3:] == "png":
            screen1.save(img, "png")
        elif img[-3:] == "jpg":
            screen1.save(img, "jpg")

    def export_xlsx_CaisseM(self):
        self.xlsx_export(self.c_table)

    def xlsx_export(self, table):
        if table.item(0, 0) is not None:
            try:
                date = datetime.now()
                filename1 = date.strftime('%d-%m-%Y  %H-%M-%S')
                filename, _ = QFileDialog.getSaveFileName(self, 'Exporter...', filename1,
                                                          filter=".xlsx(*.xlsx)")
                workbook = xlsxwriter.Workbook(filename)

                worksheet = workbook.add_worksheet()
                model = table.model()
                data1 = []
                data2 = []
                for c in range(model.columnCount()):
                    text = model.headerData(c, QtCore.Qt.Horizontal)
                    data1.append(text)

                for row in range(table.rowCount()):
                    newrow = []
                    for col in range(table.columnCount()):
                        item = table.item(row, col)
                        newrow.append(item.text())
                    data2.append(newrow)
                data = [data1] + data2

                bold = workbook.add_format({'bold': 1})
                bold.set_align('center')
                bold.set_bg_color('lime')

                worksheet.write_row(f'A1', data[0], bold)

                bold1 = workbook.add_format()
                bold1.set_align('center')

                for row in range(table.rowCount()):
                    worksheet.write_row(f'A{row + 2}', data[row + 1], bold1)

                worksheet.set_column('A:K', 18)
                workbook.close()
            except Exception:
                pass
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Erreur')
            msg.setText("Veillez remplir un tableau!")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

    def savefile(self):
        if self.table.isChecked() and self.cBox.isChecked():
            self.xlsx_export(self.ops_table)
        elif self.table.isChecked() and self.cM.isChecked():
            self.xlsx_export(self.c_table)
        elif self.table.isChecked() and self.cR.isChecked():
            self.xlsx_export(self.devise_table)

    def eventFilter(self, object, event):
        global GLOBAL_STATE
        if event.type() == QtCore.QEvent.MouseButtonDblClick:
            if self.isMaximized():
                self.showNormal()
                GLOBAL_STATE = 0
            else:
                self.showMaximized()
                GLOBAL_STATE = 1
            return True
        return False

    def cell_clicked_d(self):
        self.stacked3.setCurrentIndex(1)

    def details_D_pop(self):
        self.d = DetailsCaisseD()
        self.d.show()

        self.devise_details(self.d.usa, 'us', self.devise_table, ' $')
        self.devise_details(self.d.can, 'can', self.devise_table, ' $')
        self.devise_details(self.d.ster, 'ster', self.devise_table, ' £')
        self.devise_details(self.d.gibra, 'gib', self.devise_table, ' £')
        self.devise_details(self.d.suis, 'suise', self.devise_table, ' CHF')
        self.devise_details(self.d.dan, 'dan', self.devise_table, ' DKK')
        self.devise_details(self.d.sued, 'sued', self.devise_table, ' KR')
        self.devise_details(self.d.norv, 'norv', self.devise_table, ' KRONE')
        self.devise_details(self.d.riyal, 'riyal', self.devise_table, ' SAR')
        self.devise_details(self.d.dinar, 'dinar', self.devise_table, ' KWD')
        self.devise_details(self.d.eru, 'eru', self.devise_table, ' AED')
        self.devise_details(self.d.qatar, 'qatar', self.devise_table, ' QR')
        self.devise_details(self.d.bahr, 'bahr', self.devise_table, ' ¥')
        self.devise_details(self.d.yens, 'yens', self.devise_table, ' BD')

        self.seting_details(self.d.l200, self.d.o200, 500, 'CaisseD',
                            self.devise_table, ' €', 'l500')
        self.seting_details(self.d.l100, self.d.o100, 200, 'CaisseD', self.devise_table,
                            ' €', 'l200')
        self.seting_details(self.d.l50, self.d.o50, 100, 'CaisseD', self.devise_table,
                            ' €', 'l100')
        self.seting_details(self.d.l20, self.d.o20, 50, 'CaisseD', self.devise_table,
                            ' €', 'l50')
        self.seting_details(self.d.l10, self.d.o10, 20, 'CaisseD', self.devise_table,
                            ' €', 'l20')
        self.seting_details(self.d.l5, self.d.o5, 10, 'CaisseD', self.devise_table,
                            ' €', 'l10')
        self.seting_details(self.d.e5, self.d.o1, 5, 'CaisseD', self.devise_table,
                            ' €', 'l5')

        self.pulling_devise_data('totalE', 'CaisseD', self.d.caisseM, ' €', self.devise_table)
        self.pulling_devise_data('ExC', 'CaisseD', self.d.diff, ' DH', self.devise_table)
        self.pulling_devise_data('Cour', 'CaisseD', self.d.courtxt, ' DH', self.devise_table)

        rows = self.devise_table.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi1 = self.devise_table.item(row, 2)

        self.m.mycursor.execute(f"""SELECT remarque FROM CaisseD WHERE reference=%s""", (self.twi1.text(),))
        motif = ''.join([str(elem) for elem in self.m.mycursor.fetchone()])
        self.d.remarque.setText(motif)

    def devise_details(self, r, t, u, h):
        r.setText(str(self.pulling_data(f'{t}', u, 'CaisseD') + h))

    def pulling_devise_data(self, a, z, where, g, b):
        rows = b.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi1 = b.item(row, 2)

        self.m.mycursor.execute(f"""SELECT {a} FROM {z} WHERE reference=%s""", (self.twi1.text(),))
        motif = ''.join([str(elem) for elem in self.m.mycursor.fetchone()])

        re = float(motif)
        formatted_re = "{:,.2f}".format(re)
        if re < 0:
            where.setStyleSheet("""QLineEdit{background-color:transparent;border-radius:5px;
border-bottom:2px solid rgb(0, 0, 0);}""")
            where.setText(formatted_re + g)
        elif re > 0:
            where.setStyleSheet("""QLineEdit{background-color:transparent;border-radius:5px;
border-bottom:2px solid rgb(0, 0, 0);}""")
            where.setText(formatted_re + g)
        elif re == 0:
            where.setStyleSheet("""QLineEdit{background-color:transparent;border-radius:5px;
border-bottom:2px solid rgb(0, 0, 0);}""")
            where.setText(formatted_re + g)

    def caisse_devise_check(self):
        if self.table.isChecked():
            date_text = self.dateedit.text()
            date_text2 = self.dateedit_2.text()
            m = MyCursor()
            m.mycursor.execute("""SELECT created, user, reference, totalE, ExC, Cour FROM CaisseD 
            WHERE created between %s and %s""", (date_text, date_text2,))
            f = m.mycursor.fetchall()
            self.devise_table.setRowCount(0)
            for column_number, row_data in enumerate(f):
                self.devise_table.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    self.devise_table.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
            self.stylesheet_tables(self.devise_table, ' €')
            self.stack.insertWidget(2, self.devise_table)
            self.stack.setCurrentIndex(2)
            self.stacked3.setCurrentIndex(2)
            self.stacked2.setCurrentIndex(0)
            self.stackedWidget_2.setCurrentIndex(0)
            self.y_m_d.setCurrentIndex(1)

        elif self.graph.isChecked():
            self.y_m_d.setCurrentIndex(0)
            self.year_m_d()

    def seting_details(self, r, o, l, z, u, g, t=''):
        r.setText(str(self.pulling_data(f'{t}', u, z)))

        formatted_re2 = "{:,.2f}".format(float(r.text()) * l) + g
        o.setText(formatted_re2)

    def pulling_data(self, a, b, z):
        rows = b.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi1 = b.item(row, 2)

        self.m.mycursor.execute(f"""SELECT {a}
                                         FROM {z} WHERE reference=%s""", (self.twi1.text(),))
        motif = ''.join([str(elem) for elem in self.m.mycursor.fetchone()])
        return motif

    def details_clicked_c(self):
        self.de = DetailsCaisseMad()
        self.pulling_devise_data('dif', 'CaisseMad', self.de.diff, ' DH', self.c_table)
        self.pulling_devise_data('bal', 'CaisseMad', self.de.general, ' DH', self.c_table)
        self.pulling_devise_data('caisse', 'CaisseMad', self.de.caisseM, ' DH', self.c_table)

        self.seting_details(self.de.l200, self.de.o200, 200, 'CaisseMad', self.c_table,
                            ' DH', 'l200')
        self.seting_details(self.de.l100, self.de.o100, 100, 'CaisseMad',
                            self.c_table, ' DH', 'l100')
        self.seting_details(self.de.l50, self.de.o50, 50, 'CaisseMad', self.c_table, ' DH', 'l50')
        self.seting_details(self.de.l20, self.de.o20, 20, 'CaisseMad', self.c_table,
                            ' DH', 'l20')
        self.seting_details(self.de.l10, self.de.o10, 10, 'CaisseMad', self.c_table,
                            ' DH', 'l10')
        self.seting_details(self.de.l5, self.de.o5, 5, 'CaisseMad', self.c_table, ' DH', 'l5')
        self.seting_details(self.de.l2, self.de.o2, 2, 'CaisseMad', self.c_table, ' DH', 'l2')
        self.seting_details(self.de.l1, self.de.o1, 1, 'CaisseMad', self.c_table, ' DH', 'l1')
        self.seting_details(self.de.l05, self.de.o05, 0.5, 'CaisseMad', self.c_table,
                            ' DH', 'l05')
        self.seting_details(self.de.l02, self.de.o02, 0.2, 'CaisseMad', self.c_table,
                            ' DH', 'l02')
        self.seting_details(self.de.l01, self.de.o01, 0.1, 'CaisseMad', self.c_table,
                            ' DH', 'l01')
        self.seting_details(self.de.l001, self.de.o001, 0.01, 'CaisseMad', self.c_table,
                            ' DH', 'l001')

        rows = self.c_table.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi1 = self.c_table.item(row, 2)

        self.m.mycursor.execute(f"""SELECT remarque FROM CaisseMad WHERE reference=%s""", (self.twi1.text(),))
        motif = ''.join([str(elem) for elem in self.m.mycursor.fetchone()])
        self.de.remarque.setText(motif)
        self.de.user.setText(self.user.text())
        self.de.show()

    def cell_clicked_c(self):
        self.stacked3.setCurrentIndex(0)

    def motif_clicked(self):
        self.u = Motif()
        self.u.show()
        rows = self.ops_table.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi5 = self.ops_table.item(row, 2)

        self.m.mycursor.execute("""SELECT motif FROM Ops WHERE reference=%s""", (int(self.twi5.text()),))
        motif = ''.join(self.m.mycursor.fetchone())
        self.u.motif.setText(str(motif))

    def cell_is_clicked(self):

        rows = self.ops_table.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi0 = self.ops_table.item(row, 4)
        if self.twi0.text() == 'C / Annulation' or self.twi0.text() == 'NC / Annulation':
            self.stacked2.setCurrentIndex(2)
        else:
            self.stacked2.setCurrentIndex(1)

        self.stackedWidget_2.setCurrentIndex(1)

    def deletedOps_(self):
        global SWITCH
        if self.table.isChecked() and self.cBox.isChecked():
            if self.con.isChecked():
                if SWITCH == 1:
                    self.resume2_c()
                elif SWITCH == 0:
                    self.resume_c()
                elif SWITCH == 2:
                    self.fill_all_ops(t1='C / Annulation', t2='', t3='', t4='')
            elif self.non_con.isChecked():
                if SWITCH == 1:
                    self.resume2_nc()
                elif SWITCH == 0:
                    self.resume_nc()
                elif SWITCH == 2:
                    self.fill_all_ops(t1='NC / Annulation', t2='', t3='', t4='')
            elif self.con_non_con.isChecked():
                if SWITCH == 1:
                    self.resume2_()
                elif SWITCH == 0:
                    self.resume_()
                elif SWITCH == 2:
                    self.fill_all_ops(t1='C / Annulation', t2='NC / Annulation', t3='', t4='')
        self.stacked2.setCurrentIndex(0)

    def val_date_today(self):
        self.date = self.d.dateEdit.text()
        self.d.close()

    def onHeaderClicked(self, logicalIndex):
        if logicalIndex == 0:
            self.OpSorted('created')
        elif logicalIndex == 3:
            self.OpSorted('reference')
        elif logicalIndex == 6:
            self.OpSorted('debit')
        elif logicalIndex == 7:
            self.OpSorted('credit')
        elif logicalIndex == 8:
            self.OpSorted('soldeCompte')
        elif logicalIndex == 9:
            self.OpSorted('soldeSCompte')

    def onHeaderClicked2(self, logicalIndex):
        if logicalIndex == 0:
            self.caisseSort('created')
        elif logicalIndex == 2:
            self.caisseSort('reference')
        elif logicalIndex == 3:
            self.caisseSort('bal')
        elif logicalIndex == 4:
            self.caisseSort('caisse')
        elif logicalIndex == 5:
            self.caisseSort('dif')

    def onHeaderClicked3(self, logicalIndex):
        if logicalIndex == 0:
            self.DcaissSorted('created')
        elif logicalIndex == 2:
            self.DcaissSorted('reference')
        elif logicalIndex == 3:
            self.DcaissSorted('totalE')
        elif logicalIndex == 4:
            self.DcaissSorted('ExC')
        elif logicalIndex == 5:
            self.DcaissSorted('Cour')

    def maximize_restored(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.central_.setContentsMargins(0, 0, 0, 0)
        else:
            GLOBAL_STATE = 0
            self.showNormal()

            self.central_.setContentsMargins(0, 0, 0, 0)

    def caisseD(self):
        self.d = CaisseD()
        self.d.show()
        self.d.user.setText(self.user.text())
        self.d.date_d.setText(self.date)
        self.d.colse_btn.clicked.connect(self.clicked_update)

    def cBox_(self):
        self.stacked3.setCurrentIndex(2)
        if self.graph.isChecked():
            self.y_m_d.setCurrentIndex(0)
            self.year_m_d()
            
        if self.table.isChecked() and self.cBox.isChecked():
            if self.con.isChecked():
                if SWITCH == 0:
                    self.resume_c()
                elif SWITCH == 1:
                    self.resume2_c()
                elif SWITCH == 2:
                    self.fill_all_ops()
            elif self.non_con.isChecked():
                if SWITCH == 0:
                    self.resume_c()
                elif SWITCH == 1:
                    self.resume2_nc()
                elif SWITCH == 2:
                    self.fill_all_ops()
            elif self.con_non_con.isChecked():
                if SWITCH == 0:
                    self.resume_()
                elif SWITCH == 1:
                    self.resume2_()
                elif SWITCH == 2:
                    self.fill_all_ops()
            self.g_ballance_func()

            self.stack.insertWidget(0, self.ops_table)
            self.stack.setCurrentIndex(0)

    def CaisseMGraph(self):
        date_text = self.dateedit.text()
        date_text2 = self.dateedit_2.text()

        self.w = MplCanvas()

        self.m.mycursor.execute(
            """SELECT caisse FROM CaisseMad WHERE created between %s and %s""",
            (date_text, date_text2,))
        f = self.m.mycursor.fetchall()

        self.m.mycursor.execute(
            """SELECT created FROM CaisseMad WHERE created between %s and %s""",
            (date_text, date_text2,))
        p = self.m.mycursor.fetchall()

        self.w.figure.suptitle(f"Graphique CAISSE MAD  de {date_text} à {date_text2}")
        self.w.x.xlabel('Date/Heure')
        self.w.x.ylabel('Caisse en DH')
        line, = self.w.x.plot(p, f, marker="o", label="Débit")
        annot = self.w.ax.annotate("", xy=(0, 0), xytext=(-20, 20), textcoords="offset points",
                                   bbox=dict(boxstyle="round", fc="w"),
                                   arrowprops=dict(arrowstyle="->"))
        annot.set_visible(False)

        def update_annot(ind):
            x, y = line.get_data()
            annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
            text = "{}, {}".format(" ".join([str("{:,.2f}".format(y[n])) + ' DH' for n in ind["ind"]]),
                                   " ".join([str(x[n]) for n in ind["ind"]]))
            annot.set_text(text)
            annot.get_bbox_patch().set_alpha(0.4)

        def hover(event):
            vis = annot.get_visible()
            if event.inaxes == self.w.ax:
                cont, ind = line.contains(event)
                if cont:
                    update_annot(ind)
                    annot.set_visible(True)
                    self.w.figure.canvas.draw_idle()
                else:
                    if vis:
                        annot.set_visible(False)
                        self.w.figure.canvas.draw_idle()

        self.w.figure.canvas.mpl_connect("motion_notify_event", hover)

        self.w.ax.grid()
        self.stack.insertWidget(2, self.w)
        if self.graph.isChecked():
            self.stack.setCurrentIndex(2)

    def stylesheet_tables(self, table, devise):
        for x in range(table.rowCount()):
            g = float(table.item(x, 5).text())
            y = float(table.item(x, 4).text())
            t = float(table.item(x, 3).text())
            if g < 0:
                formatted_float_debit = "{:,.2f}".format(g)
                table.setItem(x, 5, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH')))
                table.item(x, 5).setForeground(QtGui.QColor(255, 0, 0))
            elif g > 0:
                formatted_float_debit = "{:,.2f}".format(g)
                table.setItem(x, 5, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH')))
                table.item(x, 5).setForeground(QtGui.QColor(0, 170, 0))
            if y < 0:
                formatted_float_debit1 = "{:,.2f}".format(y)
                table.setItem(x, 4, QtWidgets.QTableWidgetItem(str(formatted_float_debit1 + ' DH')))
                table.item(x, 4).setForeground(QtGui.QColor(255, 0, 0))
            elif y > 0:
                formatted_float_debit1 = "{:,.2f}".format(y)
                table.setItem(x, 4, QtWidgets.QTableWidgetItem(str(formatted_float_debit1 + ' DH')))
                table.item(x, 4).setForeground(QtGui.QColor(0, 170, 0))
            if t < 0:
                formatted_float_debit2 = "{:,.2f}".format(t)
                table.setItem(x, 3, QtWidgets.QTableWidgetItem(str(formatted_float_debit2 + devise)))
                table.item(x, 3).setForeground(QtGui.QColor(255, 0, 0))
            elif t > 0:
                formatted_float_debit2 = "{:,.2f}".format(t)
                table.setItem(x, 3, QtWidgets.QTableWidgetItem(str(formatted_float_debit2 + devise)))
                table.item(x, 3).setForeground(QtGui.QColor(0, 170, 0))
            elif g == 0 or y == 0 or t == 0:
                formatted_float_debit = "{:,.2f}".format(g)
                formatted_float_debit1 = "{:,.2f}".format(y)
                formatted_float_debit2 = "{:,.2f}".format(t)
                table.setItem(x, 5, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH')))
                table.item(x, 5).setForeground(QtGui.QColor(0, 0, 0))
                table.setItem(x, 4, QtWidgets.QTableWidgetItem(str(formatted_float_debit1 + ' DH')))
                table.item(x, 4).setForeground(QtGui.QColor(0, 0, 0))
                table.setItem(x, 3, QtWidgets.QTableWidgetItem(str(formatted_float_debit2 + devise)))
                table.item(x, 3).setForeground(QtGui.QColor(0, 0, 0))

    def CaisseMTable(self):
        date_text = self.dateedit.text()
        date_text2 = self.dateedit_2.text()
        self.m = MyCursor()
        self.m.mycursor.execute(
            """SELECT created, user, reference, bal, caisse, dif FROM CaisseMad
             WHERE created between %s and %s""",
            (date_text, date_text2))
        f = self.m.mycursor.fetchall()
        self.c_table.setRowCount(0)
        for column_number, row_data in enumerate(f):
            self.c_table.insertRow(column_number)
            for row_number, data in enumerate(row_data):
                self.c_table.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
        self.stylesheet_tables(self.c_table, ' DH')

        self.stack.insertWidget(1, self.c_table)

        self.stack.setCurrentIndex(1)

    def devise_graph(self, group):
        date_text = self.dateedit.text()
        date_text2 = self.dateedit_2.text()

        self.w = MplCanvas()
        self.m = MyCursor()
        self.m.mycursor.execute(
            f"""SELECT totalE FROM CaisseD WHERE created between %s and %s GROUP BY {group}""",
            (date_text, date_text2))
        f = self.m.mycursor.fetchall()
        self.m = MyCursor()
        self.m.mycursor.execute(
            f"""SELECT created FROM CaisseD WHERE created between %s and %s GROUP BY {group}""",
            (date_text, date_text2))
        p = self.m.mycursor.fetchall()

        self.w.figure.suptitle(f"Graphique CAISSE DEVISE de {date_text} à {date_text2}")
        self.w.x.xlabel('Date/Heure')
        self.w.x.ylabel("Total d'EURO en €")
        line, = self.w.x.plot(p, f, marker="o", label="EURO", linestyle='solid')
        annot = self.w.ax.annotate("", xy=(0, 0), xytext=(-20, 20), textcoords="offset points",
                                   bbox=dict(boxstyle="round", fc="w"),
                                   arrowprops=dict(arrowstyle="->"))
        annot.set_visible(False)

        def update_annot(ind):
            x, y = line.get_data()
            annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
            text = "{}, {}".format(" ".join([str("{:,.2f}".format(y[n])) + ' €' for n in ind["ind"]]),
                                   " ".join([str(x[n]) for n in ind["ind"]]))
            annot.set_text(text)
            annot.get_bbox_patch().set_alpha(0.4)

        def hover(event):
            vis = annot.get_visible()
            if event.inaxes == self.w.ax:
                cont, ind = line.contains(event)
                if cont:
                    update_annot(ind)
                    annot.set_visible(True)
                    self.w.figure.canvas.draw_idle()
                else:
                    if vis:
                        annot.set_visible(False)
                        self.w.figure.canvas.draw_idle()

        self.w.figure.canvas.mpl_connect("motion_notify_event", hover)

        self.w.ax.grid()
        self.stack.insertWidget(1, self.w)
        if self.graph.isChecked() and self.cR.isChecked():
            self.stack.setCurrentIndex(1)

    def BalGraph(self, group):
        date_text = self.dateedit.text()
        date_text2 = self.dateedit_2.text()

        self.w = MplCanvas()

        # self.m.mycursor.execute(
        #     f"""SELECT SUM(`debit`) FROM Ops WHERE opID=%s and acc=%s and type IN (%s, %s) and created between %s and %s GROUP BY {group}""",
        #     (self.acc_box2.currentText(), self.acc_box.currentText(), 'C / Annulation', 'NC / Annulation', date_text, date_text2))
        # ann = self.m.mycursor.fetchall()

        # self.m.mycursor.execute(
        #     f"""SELECT SUM(`credit`) FROM Ops WHERE opID=%s and acc=%s and type IN (%s, %s) and created between %s and %s GROUP BY {group}""",
        #     (self.acc_box2.currentText(), self.acc_box.currentText(), 'C / Annulation', 'NC / Annulation', date_text, date_text2))
        # ann14 = self.m.mycursor.fetchall()

        self.m.mycursor.execute(
            f"""SELECT SUM(`debit`) FROM Ops WHERE opID=%s and acc=%s and created between %s and %s GROUP BY {group}""",
            (self.acc_box2.currentText(), self.acc_box.currentText(), date_text, date_text2))
        f = self.m.mycursor.fetchall()
        self.m.mycursor.execute(
            f"""SELECT SUM(`credit`) FROM Ops WHERE opID=%s and acc=%s and created between %s and %s GROUP BY {group}""",
            (self.acc_box2.currentText(), self.acc_box.currentText(), date_text, date_text2))
        c = self.m.mycursor.fetchall()

        self.m.mycursor.execute(
            f"""SELECT COUNT(credit) FROM Ops WHERE opID=%s and acc=%s and created between %s and %s GROUP BY {group}""",
            (self.acc_box2.currentText(), self.acc_box.currentText(), date_text, date_text2))
        a = self.m.mycursor.fetchall()

        self.m.mycursor.execute(
            f"""SELECT COUNT(debit) FROM Ops WHERE opID=%s and acc=%s and created between %s and %s GROUP BY {group}""",
            (self.acc_box2.currentText(), self.acc_box.currentText(), date_text, date_text2))
        a2 = self.m.mycursor.fetchall()

        v_credit = []
        for x in c:
            t = x[0]
            v_credit.append(t)

        v_debit = []
        for x in f:
            t = x[0] 
            v_debit.append(t)

        u = []
        g = list(map(add, v_debit, v_credit))
        for y in range(0,len(g)):
            b = g[y]
            if b < 0 or b == 0:
                b = g[y] * (-1)
                u.append(b)
            else:
                u.append(b)
        
        self.m.mycursor.execute(
           f"""SELECT DATE(created) as DATE FROM Ops WHERE opID=%s and acc=%s and created between %s and %s GROUP BY {group}""",
            (self.acc_box2.currentText(), self.acc_box.currentText(), date_text, date_text2))
        p = self.m.mycursor.fetchall()

        self.w.figure.suptitle(
            f"Graphique des opérations. Compte: {self.acc_box2.currentText()} de {date_text} à {date_text2}")

        self.w.x.xlabel('Date/Heure')
        self.w.x.ylabel('Débit/Crédit en DH')
        if f is None and c is None:
            pass
        else:

            line1, = self.w.x.plot(p, u, marker="o", label="Débit", linestyle='solid')
        
            # line, = self.w.x.plot(p, v_credit, marker="o", label="Crédit", linestyle='solid')


            # annot = self.w.ax.annotate("", xy=(0, 0), xytext=(-20, 20), textcoords="offset points",
            #                         bbox=dict(boxstyle="round", fc="w"),
            #                         arrowprops=dict(arrowstyle="->"))
            # annot.set_visible(False)
            annot1 = self.w.ax.annotate("", xy=(0, 0), xytext=(-20, 20), textcoords="offset points",
                                    bbox=dict(boxstyle="round", fc="w"),
                                    arrowprops=dict(arrowstyle="->"))
            annot1.set_visible(False)

            # def update_annot(ind):
            #     x, y = line.get_data()
            #     annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
            #     text = "{}, {}".format(" ".join([str("{:,.2f}".format(y[n])) + ' DH' + ' | Nbr: '+ "".join(map(str,a[n])) for n in ind["ind"]]),
            #                         " ".join([str(x[n]) for n in ind["ind"]]))
            #     annot.set_text(text)
            #     annot.get_bbox_patch().set_alpha(0.4)
            def update_annot1(ind):
                x, y = line1.get_data()
                annot1.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
                text = "{}, {}".format(" ".join([str("{:,.2f}".format(y[n])) + ' DH' + ' | Nbr: '+ "".join(map(str,a2[n])) for n in ind["ind"]]),
                                    " ".join([str(x[n]) for n in ind["ind"]]))
                annot1.set_text(text)
                annot1.get_bbox_patch().set_alpha(0.4)

            def hover(event):
                vis = annot1.get_visible()
                if event.inaxes == self.w.ax:
                    # cont, ind = line.contains(event)
                    cont1, ind1 = line1.contains(event)
                    # if cont:
                    #     update_annot(ind)
                    #     annot.set_visible(True)
                    #     self.w.figure.canvas.draw_idle()
                    if cont1:
                        update_annot1(ind1)
                        annot1.set_visible(True)
                        self.w.figure.canvas.draw_idle()
                    else:
                        if vis:
                            # annot.set_visible(False)
                            # self.w.figure.canvas.draw_idle()
                            annot1.set_visible(False)
                            self.w.figure.canvas.draw_idle()

            self.w.figure.canvas.mpl_connect("motion_notify_event", hover)

            self.w.ax.grid()
            self.stack.insertWidget(3, self.w)
            if self.graph.isChecked() and self.cBox.isChecked():
                self.stack.setCurrentIndex(3)

    def style_opTable(self):
        for x in range(self.ops_table.rowCount()):
                        
            s = float(self.ops_table.item(x, 8).text())
            o = float(self.ops_table.item(x, 9).text())
            g = float(self.ops_table.item(x, 7).text())
            y = float(self.ops_table.item(x, 6).text())
            formatted_float_debit8 = "{:,.2f}".format(s)
            item_s = QtWidgets.QTableWidgetItem(str(formatted_float_debit8 + ' DH'))
            item_s.setTextAlignment(Qt.AlignCenter)

            formatted_float_debit5 = "{:,.2f}".format(o)
            item_o = QtWidgets.QTableWidgetItem(str(formatted_float_debit5 + ' DH'))
            item_o.setTextAlignment(Qt.AlignCenter)

            formatted_float_debit9 = "{:,.2f}".format(g)
            item_g = QtWidgets.QTableWidgetItem(str(formatted_float_debit9 + ' DH'))
            item_g.setTextAlignment(Qt.AlignCenter)

            formatted_float_debit1 = "{:,.2f}".format(y)
            item_y = QtWidgets.QTableWidgetItem(str(formatted_float_debit1 + ' DH'))
            item_y.setTextAlignment(Qt.AlignCenter)
           
            if s < 0:
                self.ops_table.setItem(x, 8, item_s)
                self.ops_table.item(x, 8).setForeground(QtGui.QColor(255, 0, 0))
            elif s > 0:
                self.ops_table.setItem(x, 8, item_s)
                self.ops_table.item(x, 8).setForeground(QtGui.QColor(0, 170, 0))
            if  o < 0:
                self.ops_table.setItem(x, 9, item_o)
                self.ops_table.item(x, 9).setForeground(QtGui.QColor(255, 0, 0))
            elif o > 0:
                self.ops_table.setItem(x, 9, item_o)
                self.ops_table.item(x, 9).setForeground(QtGui.QColor(0, 170, 0))

            if g < 0 and y == 0:
                formatted_float_debit9 = "{:,.2f}".format(g)
                self.ops_table.setItem(x, 7, item_g)
                self.ops_table.item(x, 7).setForeground(QtGui.QColor(255, 0, 0))
                self.ops_table.setItem(x, 6, QtWidgets.QTableWidgetItem(''))
                self.ops_table.item(x, 6).setForeground(QtGui.QColor(0, 0, 0))
            
            elif y > 0 and g == 0:
                formatted_float_debit1 = "{:,.2f}".format(y)
                self.ops_table.setItem(x, 6, item_y)
                self.ops_table.item(x, 6).setForeground(QtGui.QColor(0, 170, 0))
                self.ops_table.setItem(x, 7, QtWidgets.QTableWidgetItem(''))
                self.ops_table.item(x, 7).setForeground(QtGui.QColor(0, 0, 0))

    def OpSort(self, type_, tip_):
        global SWITCH
        
        if self.table.isChecked() and self.cBox.isChecked():
            if self.con.isChecked():
                if self.acc_box2.currentText() == 'Tout':
                    self.type = self.con.text()
                    self.OpTypeTable(self.type, (self.con.text() + ' / Annulation'), '', '', f'ORDER BY {type_} {tip_}',
                                     'acc',
                                     self.acc_box.currentText())
                elif self.acc_box2.currentText() == 'Selectionnez un sous-compte...':
                    self.OpTypeTable(self.type, (self.con.text() + ' / Annulation'), '', '', f'ORDER BY {type_} {tip_}',
                                     'acc',
                                     self.acc_box.currentText())
                else:
                    self.type = self.con.text()
                    self.OpTypeTable(self.type, (self.con.text() + ' / Annulation'), '', '', f'ORDER BY {type_} {tip_}',
                                     'opID',
                                     self.acc_box2.currentText())
            elif self.non_con.isChecked():
                if self.acc_box2.currentText() == 'Tout' or 'Selectionnez un sous-compte...':
                    self.type = self.non_con.text()
                    self.OpTypeTable(self.type, (self.non_con.text() + ' / Annulation'), '', '',
                                     f'ORDER BY {type_} {tip_}',
                                     'acc',
                                     self.acc_box.currentText())
                elif self.acc_box2.currentText() == 'Selectionnez un sous-compte...':
                    self.type = self.non_con.text()
                    self.OpTypeTable(self.type, (self.non_con.text() + ' / Annulation'), '', '',
                                     f'ORDER BY {type_} {tip_}',
                                     'acc',
                                     self.acc_box.currentText())
                else:
                    self.type = self.non_con.text()
                    self.OpTypeTable(self.type, (self.non_con.text() + ' / Annulation'), '', '',
                                     f'ORDER BY {type_} {tip_}',
                                     'opID',
                                     self.acc_box2.currentText())
            elif self.con_non_con.isChecked():
                if SWITCH == 1:
                    rows = self.b_table.selectionModel().selectedRows()
                    for self.index in sorted(rows):
                        pass
                    if len(rows) > 0:
                        for row in range(self.index.row(), self.index.row() + 1):
                            self.twib = self.b_table.item(row, 0)
                   
                    self.type = self.non_con.text()
                    self.OpTypeTable((self.type + ' / Annulation'), (self.con.text() + ' / Annulation'),
                                     self.con.text(), self.non_con.text(),
                                     f'ORDER BY {type_} {tip_}', 'acc',
                                     self.twib.text())
                else:
                    if self.acc_box2.currentText() == 'Tout':
                        self.type = self.non_con.text()
                        self.OpTypeTable((self.type + ' / Annulation'), (self.con.text() + ' / Annulation'),
                                        self.con.text(), self.non_con.text(),
                                        f'ORDER BY {type_} {tip_}', 'acc',
                                        self.acc_box.currentText())

                        
                    elif self.acc_box2.currentText() == 'Selectionnez un sous-compte...':
                        self.type = self.non_con.text()
                        self.OpTypeTable((self.type + ' / Annulation'), (self.con.text() + ' / Annulation'),
                                        self.con.text(), self.non_con.text(),
                                        f'ORDER BY {type_} {tip_}', 'acc',
                                        self.acc_box.currentText())
                        
                    else:
                        self.type = self.non_con.text()
                        self.OpTypeTable((self.type + ' / Annulation'), (self.con.text() + ' / Annulation'),
                                        self.con.text(), self.non_con.text(),
                                        f'ORDER BY {type_} {tip_}', 'opID',
                                        self.acc_box2.currentText())
                    
                self.stack.insertWidget(0, self.ops_table)
                self.stack.setCurrentIndex(0)

    def OpSorted(self, type_):
        global DEFAULT_STATE2, SWITCH
        status = DEFAULT_STATE2

        if status == 0:
            if SWITCH == 2:
                self.fill_all_ops(col=type_, order='DESC')
            elif SWITCH == 1:
                self.OpSort(type_, 'DESC')
            elif SWITCH == 0:
                self.OpSort(type_, 'DESC')
            DEFAULT_STATE2 = 1
        else:
            if SWITCH == 2:
                self.fill_all_ops(col=type_, order='ASC')
            elif SWITCH == 1:
                self.OpSort(type_, 'ASC')
            elif SWITCH == 0:
                self.OpSort(type_, 'ASC')
            DEFAULT_STATE2 = 0

    def OpTypeTable(self, OpType, Optyp, stype, thtype, type_, all_, all_type):
        global SWITCH

        if self.table.isChecked() and self.cBox.isChecked():
            if SWITCH == 1:
                rows = self.b_table.selectionModel().selectedRows()
                for self.index in sorted(rows):
                    pass
                if len(rows) > 0:
                    for row in range(self.index.row(), self.index.row() + 1):
                        self.twib = self.b_table.item(row, 0)
                y = self.twib.text()
            else:
                y = self.acc_box.currentText()

            date_text = self.dateedit.text()
            date_text2 = self.dateedit_2.text()
            self.m = MyCursor()
            self.m.mycursor.execute(
                f"""SELECT  created, acc, opID, reference, userID, type ,debit, credit, soldeCompte, soldeSCompte, motif FROM Ops WHERE
                 {all_}=%s and acc=%s and type IN (%s, %s, %s, %s) and created between %s and %s {type_}""",
                (all_type, y, OpType, Optyp, stype, thtype, date_text, date_text2))
            f = self.m.mycursor.fetchall()

            self.ops_table.setRowCount(0)
            for column_number, row_data in enumerate(f):
                self.ops_table.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.ops_table.setItem(column_number, row_number, item)
        
            self.style_opTable()
            self.stack.insertWidget(0, self.ops_table)
            self.stack.setCurrentIndex(0)

    def rCaisseM(self):
        if self.graph.isChecked:
            self.CaisseMGraph()
        if self.table.isChecked() and self.cM.isChecked():
            self.CaisseMTable()
        self.stackedWidget_2.setCurrentIndex(0)
        self.stacked2.setCurrentIndex(0)
        self.y_m_d.setCurrentIndex(1)

    def caisse_M(self):
        self.c = CaisseMad()
        self.c.show()
        self.c.user.setText(self.user.text())
        self.c.date_mad.setText(self.date)
        self.c.close_btn.clicked.connect(self.clicked_update)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def table_(self):
        if self.cBox.isChecked():
            if self.con.isChecked():
                self.resume_c()
            elif self.non_con.isChecked():
                self.resume_nc()
            elif self.con_non_con.isChecked():
                self.resume_()
        elif self.cM.isChecked():
            self.CaisseMTable()
        elif self.cR.isChecked():
            self.caisse_devise_check()
        self.y_m_d.setCurrentIndex(1)
        self.stacked2.setCurrentIndex(0)
        self.stacked3.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(0)

    def graph_(self):
        if self.cM.isChecked():
            self.CaisseMGraph()
        elif self.cBox.isChecked():
            self.y_m_d.setCurrentIndex(0)
            self.year_m_d()
        elif self.cR.isChecked():
            self.y_m_d.setCurrentIndex(0)
            self.year_m_d()
        self.stacked2.setCurrentIndex(0)
        self.stacked3.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(0)

    def caissemadSort(self, desc, column):
        date_text = self.dateedit.text()
        date_text2 = self.dateedit_2.text()

        self.m.mycursor.execute(
            f"""SELECT created, user, reference, bal, caisse, dif FROM CaisseMad
             WHERE created between %s and %s ORDER BY {column} {desc}""",
            (date_text, date_text2))
        f = self.m.mycursor.fetchall()
        self.c_table.setRowCount(0)
        for column_number, row_data in enumerate(f):
            self.c_table.insertRow(column_number)
            for row_number, data in enumerate(row_data):
                self.c_table.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
        self.stylesheet_tables(self.c_table, ' DH')
        self.stack.insertWidget(1, self.c_table)
        self.stack.setCurrentIndex(1)

    def caisseSort(self, column):
        global DEFAULT_STATE3
        status = DEFAULT_STATE3
        if status == 0:
            self.caissemadSort('ASC', column)
            DEFAULT_STATE3 = 1
        else:
            self.caissemadSort('DESC', column)
            DEFAULT_STATE3 = 0

    def DcaisseSort(self, column, desc):
        date_text = self.dateedit.text()
        date_text2 = self.dateedit_2.text()
        m = MyCursor()
        m.mycursor.execute(f"""SELECT created, user, reference, totalE, ExC, Cour FROM CaisseD 
                    WHERE created between %s and %s ORDER BY {column} {desc}""", (date_text, date_text2,))
        f = m.mycursor.fetchall()
        self.devise_table.setRowCount(0)
        for column_number, row_data in enumerate(f):
            self.devise_table.insertRow(column_number)
            for row_number, data in enumerate(row_data):
                self.devise_table.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
        self.stylesheet_tables(self.devise_table, ' €')
        self.stack.insertWidget(2, self.devise_table)
        self.stack.setCurrentIndex(2)

    def DcaissSorted(self, column):
        global DEFAULT_STATE4
        status = DEFAULT_STATE4
        if status == 0:
            self.DcaisseSort(column, 'ASC')
            DEFAULT_STATE4 = 1
        else:
            self.DcaisseSort(column, 'DESC')
            DEFAULT_STATE4 = 0

    def BalSorted(self, tablewidget, num):
        global DEFAULT_STATE1
        status = DEFAULT_STATE1
        if status == 0:

            self.m.mycursor.execute(
                f"""SELECT name, balance FROM Accounts ORDER BY balance DESC""")
            f = self.m.mycursor.fetchall()
            tablewidget.setRowCount(0)
            for column_number, row_data in enumerate(f):
                tablewidget.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    tablewidget.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
            for x in range(tablewidget.rowCount()):
                g = float(tablewidget.item(x, num).text())
                if g < 0:
                    formatted_float_debit = "{:,.2f}".format(g)
                    tablewidget.setItem(x, num, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH')))
                    tablewidget.item(x, num).setForeground(QtGui.QColor(255, 0, 0))
                elif g > 0:
                    formatted_float_debit = "{:,.2f}".format(g)
                    tablewidget.setItem(x, num, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH')))
                    tablewidget.item(x, num).setForeground(QtGui.QColor(0, 170, 0))
                elif g == 0:
                    formatted_float_debit = "{:,.2f}".format(g)
                    tablewidget.setItem(x, num, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH')))
                    tablewidget.item(x, num).setForeground(QtGui.QColor(0, 0, 0))

            DEFAULT_STATE1 = 1
        else:

            self.m.mycursor.execute(
                f"""SELECT name, balance FROM Accounts ORDER BY balance ASC""")
            f = self.m.mycursor.fetchall()

            tablewidget.setRowCount(0)
            for column_number, row_data in enumerate(f):
                tablewidget.insertRow(column_number)
                for row_number, data in enumerate(row_data):
                    tablewidget.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
            for x in range(tablewidget.rowCount()):
                g = float(tablewidget.item(x, num).text())
                if g < 0:
                    formatted_float_debit = "{:,.2f}".format(g)
                    tablewidget.setItem(x, num, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH ')))
                    tablewidget.item(x, num).setForeground(QtGui.QColor(255, 0, 0))
                elif g > 0:
                    formatted_float_debit = "{:,.2f}".format(g)
                    tablewidget.setItem(x, num, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH ')))
                    tablewidget.item(x, num).setForeground(QtGui.QColor(0, 170, 0))
                elif g == 0:
                    formatted_float_debit = "{:,.2f}".format(g)
                    tablewidget.setItem(x, num, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH ')))
                    tablewidget.item(x, num).setForeground(QtGui.QColor(0, 0, 0))

            DEFAULT_STATE1 = 0

    def date_changed(self):
        self.date_text = self.dateedit.text()
        self.date_text2 = self.dateedit_2.text()
        global SWITCH

        if self.cBox.isChecked():
            if self.con.isChecked():
                if SWITCH == 1:
                    self.resume2_c()
                else:
                    self.resume_c()
            elif self.non_con.isChecked():
                if SWITCH == 1:
                    self.resume2_nc()
                else:
                    self.resume_nc()
            elif self.con_non_con.isChecked():
                if self.acc_box.currentText() == 'Tout':
                    self.fill_all_ops()
                elif SWITCH == 2:
                    self.fill_all_ops()
                if SWITCH == 1:
                    self.resume2_()
                elif SWITCH == 0:
                    self.resume_()

        elif self.cM.isChecked():
            self.CaisseMTable()
        elif self.cR.isChecked():
            self.caisse_devise_check()
        self.g_ballance_func()
        if self.graph.isChecked():
            if self.cBox.isChecked():
                self.year_m_d()
            elif self.cM.isChecked():
                self.CaisseMGraph()

    def con_(self):
        global SWITCH

        if SWITCH == 0:
            self.resume_c()
        elif SWITCH == 1:
            self.resume2_c()
        elif SWITCH == 2:
            if self.deletedOps.isChecked():
                self.fill_all_ops(t1='', t2='C / Annulation', t3='', t4='')
            else:
                self.fill_all_ops(t1='C', t2='C / Annulation', t3='', t4='')
        self.stacked2.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)

    def non_con_(self):
        global SWITCH

        if SWITCH == 0:
            self.resume_nc()
        elif SWITCH == 1:
            self.resume2_nc()
        elif SWITCH == 2:
            if self.deletedOps.isChecked():
                self.fill_all_ops(t1='', t2='NC / Annulation', t3='', t4='')
            else:
                self.fill_all_ops(t1='NC', t2='NC / Annulation', t3='', t4='')
        self.stacked2.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)

    def con_non_con_(self):
        global SWITCH

        if SWITCH == 0:
            self.resume_()
        elif SWITCH == 1:
            self.resume2_()
        elif SWITCH == 2:
            if self.deletedOps.isChecked():
                self.fill_all_ops(t1='C / Annulation', t2='NC / Annulation', t3='', t4='')
            else:
                self.fill_all_ops()
        self.stacked2.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)

    def resume_c(self):
        if self.deletedOps.isChecked():
            if self.acc_box2.currentText() == 'Tout':
                self.OpTypeTable('', (self.con.text() + ' / Annulation'), '', '', '', 'acc', self.acc_box.currentText())
            elif self.acc_box2.currentText() == 'Selectionnez un sous-compte...':
                self.OpTypeTable('', (self.con.text() + ' / Annulation'), '', '', '', 'acc', self.acc_box.currentText())
            else:
                self.OpTypeTable('', (self.con.text() + ' / Annulation'), '', '', '', 'opID',
                                 self.acc_box2.currentText())
        else:
            self.type = self.con.text()
            if self.acc_box2.currentText() == 'Tout':
                self.OpTypeTable(self.type, (self.con.text() + ' / Annulation'), '', '', '', 'acc',
                                 self.acc_box.currentText())
            elif self.acc_box2.currentText() == 'Selectionnez un sous-compte...':
                self.OpTypeTable(self.type, (self.con.text() + ' / Annulation'), '', '', '', 'acc',
                                 self.acc_box.currentText())
            else:
                self.OpTypeTable(self.type, (self.con.text() + ' / Annulation'), '', '', '', 'opID',
                                 self.acc_box2.currentText())

    def resume_nc(self):
        if self.deletedOps.isChecked():
            if self.acc_box2.currentText() == 'Tout':
                self.OpTypeTable('', (self.non_con.text() + ' / Annulation'), '', '', '', 'acc',
                                 self.acc_box.currentText())
            elif self.acc_box2.currentText() == 'Selectionnez un sous-compte...':
                self.OpTypeTable('', (self.non_con.text() + ' / Annulation'), '', '', '', 'acc',
                                 self.acc_box.currentText())
            else:
                self.OpTypeTable('', (self.non_con.text() + ' / Annulation'), '', '', '', 'opID',
                                 self.acc_box2.currentText())
        else:
            self.type = self.non_con.text()
            if self.acc_box2.currentText() == 'Tout':
                self.OpTypeTable(self.type, (self.non_con.text() + ' / Annulation'), '', '', '', 'acc',
                                 self.acc_box.currentText())
            elif self.acc_box2.currentText() == 'Selectionnez un sous-compte...':
                self.OpTypeTable(self.type, (self.non_con.text() + ' / Annulation'), '', '', '', 'acc',
                                 self.acc_box.currentText())
            else:
                self.OpTypeTable(self.type, (self.non_con.text() + ' / Annulation'), '', '', '', 'opID',
                                 self.acc_box2.currentText())

    def resume_(self):
        if self.deletedOps.isChecked():
            if self.acc_box2.currentText() == 'Tout':
                self.OpTypeTable((self.con.text() + ' / Annulation'), (self.non_con.text() + ' / Annulation'), '', '',
                                 '',
                                 'acc', self.acc_box.currentText())
            elif self.acc_box2.currentText() == 'Selectionnez un sous-compte...':
                self.OpTypeTable((self.con.text() + ' / Annulation'), (self.non_con.text() + ' / Annulation'), '', '',
                                 '',
                                 'acc', self.acc_box.currentText())
            else:
                self.OpTypeTable((self.con.text() + ' / Annulation'), (self.non_con.text() + ' / Annulation'), '', '',
                                 '', 'opID', self.acc_box2.currentText())
        else:
            if self.acc_box2.currentText() == 'Tout':
                self.OpTypeTable((self.con.text() + ' / Annulation'), (self.non_con.text() + ' / Annulation'),
                                 self.con.text(), self.non_con.text(),
                                 '',
                                 'acc', self.acc_box.currentText())
            elif self.acc_box2.currentText() == 'Selectionnez un sous-compte...':
                self.OpTypeTable((self.con.text() + ' / Annulation'), (self.non_con.text() + ' / Annulation'),
                                 self.con.text(), self.non_con.text(),
                                 '',
                                 'acc', self.acc_box.currentText())
            else:
                self.OpTypeTable((self.con.text() + ' / Annulation'), (self.non_con.text() + ' / Annulation'),
                                 self.con.text(), self.non_con.text(),
                                 '',
                                 'opID', self.acc_box2.currentText())

    def g_ballance_func(self):
        date_text = self.dateedit.text()
        date_text2 = self.dateedit_2.text()

        self.m.mycursor.execute("SELECT SUM(debit) FROM Ops WHERE opID=%s and acc=%s and created between %s and %s",
                                (self.acc_box2.currentText(), self.acc_box.currentText(), date_text, date_text2))
        result = self.m.mycursor.fetchone()[0]

        self.m.mycursor.execute("SELECT SUM(credit) FROM Ops WHERE opID=%s and acc=%s and created between %s and %s",
                                (self.acc_box2.currentText(), self.acc_box.currentText(), date_text, date_text2))
        result1 = self.m.mycursor.fetchone()[0]

        if result is None and result1 is None:
            self.g_ballance.setStyleSheet("""QLineEdit{border-radius:10px;
                                                          color: rgb(0, 0, 0);}""")
            fr1 = 0
            formatted_float_debit = "{:,.2f}".format(fr1)
            self.g_ballance.setText(str(formatted_float_debit) + ' DH')
        else:
            fr = result + result1
            if fr < 0:
                self.g_ballance.setStyleSheet("""QLineEdit{border-radius:10px;
                                                          color: rgb(255, 0, 0);}""")
                formatted_float_debit = "{:,.2f}".format(fr)
                self.g_ballance.setText(str(formatted_float_debit) + ' DH')

            elif fr > 0:
                self.g_ballance.setStyleSheet("""QLineEdit{border-radius:10px;
                                                                          color: rgb(0, 170, 0);}""")
                formatted_float_debit = "{:,.2f}".format(fr)
                self.g_ballance.setText(str(formatted_float_debit) + ' DH')

    def repeat_(self):
        global SWITCH
        SWITCH = 0
        if self.table.isChecked() and self.cBox.isChecked():
            if self.con.isChecked():
                self.resume_c()
            elif self.non_con.isChecked():
                self.resume_nc()
            elif self.con_non_con.isChecked():
                self.resume_()
            self.g_ballance_func()
        else:
            self.year_m_d()

        self.stacked2.setCurrentIndex(0)

    def repeat(self):
        global SWITCH
        SWITCH = 0
        self.acc_box2.clear()
        self.m = MyCursor()
        self.m.mycursor.execute('SELECT name FROM SAccounts WHERE accountID=%s', (self.acc_box.currentText(),))

        for x in self.m.mycursor.fetchall():
            self.acc_box2.addItems(x)
        self.acc_box2.insertItem(0, 'Tout')
        if self.acc_box2.currentText() == 'Selectionnez un sous-compte...':
            if self.con.isChecked():
                self.resume_c()
            elif self.non_con.isChecked():
                self.resume_nc()
            elif self.con_non_con.isChecked():
                self.resume_()
        self.g_ballance_func()

        if self.acc_box.currentText() == 'Selectionnez un compte...':
            self.g_ballance.clear()
            self.g_ballance_.clear()
        else:
            if self.acc_box.currentText() == 'Tout':
                SWITCH = 2
                self.fill_all_ops()
            else:
                self.m = MyCursor()
                self.m.mycursor.execute('SELECT balance FROM Accounts WHERE name=%s',
                                        (self.acc_box.currentText(),))
                l_ = self.m.mycursor.fetchone()[0]

                if l_ < 0:
                    self.g_ballance_.setStyleSheet("""QLineEdit{border-radius:10px;
                                                                             color: rgb(255, 0, 0);}""")
                    formatted_float_debit = "{:,.2f}".format(l_)
                    self.g_ballance_.setText(str(formatted_float_debit) + ' DH')

                elif l_ > 0:
                    self.g_ballance_.setStyleSheet("""QLineEdit{border-radius:10px;
                                                                             color: rgb(0, 170, 0);}""")
                    formatted_float_debit = "{:,.2f}".format(l_)
                    self.g_ballance_.setText(str(formatted_float_debit) + ' DH')

                elif l_ == 0:
                    self.g_ballance_.setStyleSheet("""QLineEdit{border-radius:10px;
                                                                             color: rgb(0, 0, 0);}""")
                    formatted_float_debit = "{:,.2f}".format(l_)
                    self.g_ballance_.setText(str(formatted_float_debit) + ' DH')
        if self.table.isChecked() and self.cBox.isChecked():
            self.m = MyCursor()
            self.m.mycursor.execute("SELECT SUM(debit) FROM Ops WHERE acc=%s", (self.acc_box.currentText(),))
            result2 = self.m.mycursor.fetchone()[0]
            self.m = MyCursor()
            self.m.mycursor.execute("SELECT SUM(credit) FROM Ops WHERE acc=%s", (self.acc_box.currentText(),))
            result3 = self.m.mycursor.fetchone()[0]

            if result2 is None and result3 is None:
                fr = 0
                self.m.mycursor.execute("UPDATE Accounts SET balance=%s WHERE name=%s",
                                        (fr, self.acc_box.currentText(),))
                self.m.db.commit()
            else:
                fr = result2 + result3
                self.m.mycursor.execute("UPDATE Accounts SET balance=%s WHERE name=%s",
                                        (fr, self.acc_box.currentText(),))
                self.m.db.commit()
        self.stacked2.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)

    def clicked_update(self):
        if self.cM.isChecked() and self.table.isChecked():
            self.CaisseMTable()
        elif self.cR.isChecked() and self.table.isChecked():
            self.caisse_devise_check()
        self.acc_box.clear()
        self.m = MyCursor()
        self.m.mycursor.execute('SELECT name FROM Accounts')

        for x in self.m.mycursor.fetchall():
            self.acc_box.addItems(x)
        self.m = MyCursor()
        self.m.mycursor.execute("SELECT SUM(debit) FROM Ops WHERE type IN ('C', 'C / Annulation')")
        result4 = self.m.mycursor.fetchone()[0]
        self.m = MyCursor()
        self.m.mycursor.execute("SELECT SUM(credit) FROM Ops WHERE type IN ('C', 'C / Annulation')")
        result5 = self.m.mycursor.fetchone()[0]
        if result4 is None and result5 is None:
            re = 0
            formatted_re = "{:,.2f}".format(re)
            self.general.setStyleSheet("""QLineEdit{border-radius:10px;
                                                                          color: rgb(0, 0, 0);}""")
            self.general.setText(formatted_re + ' DH')
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
        self.m = MyCursor()
        self.m.mycursor.execute("SELECT SUM(debit) FROM Ops WHERE opID=%s",
                                (self.acc_box2.currentText(),))
        result = self.m.mycursor.fetchone()[0]

        self.m.mycursor.execute("SELECT SUM(credit) FROM Ops WHERE opID=%s",
                                (self.acc_box2.currentText(),))
        result1 = self.m.mycursor.fetchone()[0]

        if result is None and result1 is None:
            self.g_ballance.setStyleSheet("""QLineEdit{border-radius:10px;
                                                          color: rgb(0, 0, 0);}""")
            fr1 = 0
            formatted_float_debit = "{:,.2f}".format(fr1)
            self.g_ballance.setText(str(formatted_float_debit) + ' DH')
        else:
            fr = result + result1
            if fr < 0:
                self.g_ballance.setStyleSheet("""QLineEdit{border-radius:10px;
                                                          color: rgb(255, 0, 0);}""")
                formatted_float_debit = "{:,.2f}".format(fr)
                self.g_ballance.setText(str(formatted_float_debit) + ' DH')

            elif fr > 0:
                self.g_ballance.setStyleSheet("""QLineEdit{border-radius:10px;
                                                                          color: rgb(0, 170, 0);}""")
                formatted_float_debit = "{:,.2f}".format(fr)
                self.g_ballance.setText(str(formatted_float_debit) + ' DH')
        self.m = MyCursor()
        self.m.mycursor.execute(
            f"""SELECT name, balance FROM Accounts ORDER BY balance DESC""")
        f = self.m.mycursor.fetchall()
        self.b_table.setRowCount(0)
        for column_number, row_data in enumerate(f):
            self.b_table.insertRow(column_number)
            for row_number, data in enumerate(row_data):
                self.b_table.setItem(column_number, row_number, QtWidgets.QTableWidgetItem(str(data)))
        for x in range(self.b_table.rowCount()):
            g = float(self.b_table.item(x, 1).text())
            if g < 0:
                formatted_float_debit = "{:,.2f}".format(g)
                self.b_table.setItem(x, 1, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH')))
                self.b_table.item(x, 1).setForeground(QtGui.QColor(255, 0, 0))
            elif g > 0:
                formatted_float_debit = "{:,.2f}".format(g)
                self.b_table.setItem(x, 1, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH')))
                self.b_table.item(x, 1).setForeground(QtGui.QColor(0, 170, 0))
            elif g == 0:
                formatted_float_debit = "{:,.2f}".format(g)
                self.b_table.setItem(x, 1, QtWidgets.QTableWidgetItem(str(formatted_float_debit + ' DH')))
                self.b_table.item(x, 1).setForeground(QtGui.QColor(0, 0, 0))
        self.acc_box.insertItem(0, 'Tout')
        self.stackedWidget_2.setCurrentIndex(0)

    def displaytime(self):
        time = QTime.currentTime()
        self.time.setText(time.toString(Qt.DefaultLocaleLongDate))

    def clicked_add_acc(self):
        self.a = AddAcc()
        self.a.user.setText(self.user.text())
        self.a.close_btn.clicked.connect(self.clicked_update)
        self.a.show()

    def clicked_add(self):
        self.m = AddCollab()
        self.m.user.setText(self.user.text())
        self.m.show()

    def clicked_add_ops(self):
        self.a = AddOps()
        self.a.user.setText(self.user.text())
        self.a.date_label.setText(self.date)
        self.a.show()
        self.a.debit.setFocus()
        self.a.debit.selectAll()
        self.a.colse_btn.clicked.connect(self.clicked_update)

    def remarque_ops(self):
        self.rem = MotifOps()
        self.rem.show()

        rows = self.ops_table.selectionModel().selectedRows()
        for self.index in sorted(rows):
            pass
        if len(rows) > 0:
            for row in range(self.index.row(), self.index.row() + 1):
                self.twi0 = self.ops_table.item(row, 3)

        self.m.mycursor.execute("""SELECT motif FROM Ops WHERE reference=%s""", (int(self.twi0.text()),))
        motif = ''.join(self.m.mycursor.fetchone())
        self.rem.motif.setText(str(motif))


# y_m_d for accs and devise

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
