# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'details_mad.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dfgsdx(object):
    def setupUi(self, dfgsdx):
        dfgsdx.setObjectName("dfgsdx")
        dfgsdx.resize(1070, 580)
        dfgsdx.setMinimumSize(QtCore.QSize(0, 0))
        dfgsdx.setMaximumSize(QtCore.QSize(1200, 650))
        self.frame_2 = QtWidgets.QFrame(dfgsdx)
        self.frame_2.setGeometry(QtCore.QRect(-1, -1, 1071, 581))
        self.frame_2.setStyleSheet("QFrame#frame_2{\n"
"border-radius:10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1071, 111))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.user = QtWidgets.QLabel(self.frame)
        self.user.setGeometry(QtCore.QRect(390, 60, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(16)
        self.user.setFont(font)
        self.user.setStyleSheet("background-color: transparent;")
        self.user.setText("")
        self.user.setObjectName("user")
        self.date = QtWidgets.QLabel(self.frame)
        self.date.setGeometry(QtCore.QRect(840, 60, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(13)
        self.date.setFont(font)
        self.date.setStyleSheet("background-color:transparent;")
        self.date.setObjectName("date")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(290, 60, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.time = QtWidgets.QLabel(self.frame)
        self.time.setGeometry(QtCore.QRect(980, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(13)
        self.time.setFont(font)
        self.time.setStyleSheet("background-color:transparent;")
        self.time.setObjectName("time")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(290, 30, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.title_bar = QtWidgets.QFrame(self.frame)
        self.title_bar.setGeometry(QtCore.QRect(0, -1, 1071, 31))
        self.title_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.mini = QtWidgets.QPushButton(self.title_bar)
        self.mini.setGeometry(QtCore.QRect(1010, 10, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.mini.setFont(font)
        self.mini.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:10px;\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(206, 137, 0);\n"
"}")
        self.mini.setText("")
        self.mini.setObjectName("mini")
        self.close_btn = QtWidgets.QPushButton(self.title_bar)
        self.close_btn.setGeometry(QtCore.QRect(1040, 10, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.close_btn.setFont(font)
        self.close_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:10px;\n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(211, 0, 0);\n"
"}")
        self.close_btn.setText("")
        self.close_btn.setObjectName("close_btn")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 89, 1221, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(-1, 109, 1073, 471))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.general = QtWidgets.QLineEdit(self.frame_3)
        self.general.setGeometry(QtCore.QRect(420, 50, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.general.setFont(font)
        self.general.setStyleSheet("border-radius:5px;\n"
"border-bottom:2px solid rgb(0, 0, 0);\n"
"background-color:transparent;")
        self.general.setText("")
        self.general.setAlignment(QtCore.Qt.AlignCenter)
        self.general.setReadOnly(True)
        self.general.setObjectName("general")
        self.dif = QtWidgets.QLineEdit(self.frame_3)
        self.dif.setGeometry(QtCore.QRect(420, 280, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.dif.setFont(font)
        self.dif.setStyleSheet("border-radius:5px;\n"
"border-bottom:2px solid rgb(0, 0, 0);\n"
"background-color:transparent;")
        self.dif.setText("")
        self.dif.setAlignment(QtCore.Qt.AlignCenter)
        self.dif.setReadOnly(True)
        self.dif.setObjectName("dif")
        self.sgeneral = QtWidgets.QLabel(self.frame_3)
        self.sgeneral.setGeometry(QtCore.QRect(440, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sgeneral.setFont(font)
        self.sgeneral.setStyleSheet("background-color: transparent;")
        self.sgeneral.setAlignment(QtCore.Qt.AlignCenter)
        self.sgeneral.setObjectName("sgeneral")
        self.caisseMAD = QtWidgets.QLineEdit(self.frame_3)
        self.caisseMAD.setGeometry(QtCore.QRect(420, 170, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.caisseMAD.setFont(font)
        self.caisseMAD.setStyleSheet("border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.caisseMAD.setText("")
        self.caisseMAD.setAlignment(QtCore.Qt.AlignCenter)
        self.caisseMAD.setReadOnly(True)
        self.caisseMAD.setObjectName("caisseMAD")
        self.differ = QtWidgets.QLabel(self.frame_3)
        self.differ.setGeometry(QtCore.QRect(440, 240, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.differ.setFont(font)
        self.differ.setStyleSheet("background-color: transparent;")
        self.differ.setAlignment(QtCore.Qt.AlignCenter)
        self.differ.setObjectName("differ")
        self.caissemad = QtWidgets.QLabel(self.frame_3)
        self.caissemad.setGeometry(QtCore.QRect(440, 130, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.caissemad.setFont(font)
        self.caissemad.setStyleSheet("background-color: transparent;")
        self.caissemad.setAlignment(QtCore.Qt.AlignCenter)
        self.caissemad.setObjectName("caissemad")
        self.label_25 = QtWidgets.QLabel(self.frame_3)
        self.label_25.setGeometry(QtCore.QRect(20, 350, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.remarque = QtWidgets.QTextEdit(self.frame_3)
        self.remarque.setGeometry(QtCore.QRect(120, 360, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.remarque.setFont(font)
        self.remarque.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);\n"
"border-right:2px solid rgb(0, 0, 0);")
        self.remarque.setReadOnly(True)
        self.remarque.setObjectName("remarque")
        self.layoutWidget = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 0, 91, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.l200 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l200.setFont(font)
        self.l200.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.l200.setAlignment(QtCore.Qt.AlignCenter)
        self.l200.setReadOnly(True)
        self.l200.setObjectName("l200")
        self.verticalLayout.addWidget(self.l200)
        self.l100 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l100.setFont(font)
        self.l100.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.l100.setAlignment(QtCore.Qt.AlignCenter)
        self.l100.setReadOnly(True)
        self.l100.setObjectName("l100")
        self.verticalLayout.addWidget(self.l100)
        self.l50 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l50.setFont(font)
        self.l50.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.l50.setAlignment(QtCore.Qt.AlignCenter)
        self.l50.setReadOnly(True)
        self.l50.setObjectName("l50")
        self.verticalLayout.addWidget(self.l50)
        self.l20 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l20.setFont(font)
        self.l20.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.l20.setAlignment(QtCore.Qt.AlignCenter)
        self.l20.setReadOnly(True)
        self.l20.setObjectName("l20")
        self.verticalLayout.addWidget(self.l20)
        self.l10 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l10.setFont(font)
        self.l10.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.l10.setAlignment(QtCore.Qt.AlignCenter)
        self.l10.setReadOnly(True)
        self.l10.setObjectName("l10")
        self.verticalLayout.addWidget(self.l10)
        self.l5 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l5.setFont(font)
        self.l5.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.l5.setAlignment(QtCore.Qt.AlignCenter)
        self.l5.setReadOnly(True)
        self.l5.setObjectName("l5")
        self.verticalLayout.addWidget(self.l5)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 0, 66, 331))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mp = QtWidgets.QLabel(self.layoutWidget1)
        self.mp.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mp.setFont(font)
        self.mp.setStyleSheet("background-color:transparent;")
        self.mp.setObjectName("mp")
        self.verticalLayout_2.addWidget(self.mp)
        self.mp_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.mp_2.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mp_2.setFont(font)
        self.mp_2.setStyleSheet("background-color:transparent;")
        self.mp_2.setObjectName("mp_2")
        self.verticalLayout_2.addWidget(self.mp_2)
        self.mp_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.mp_3.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mp_3.setFont(font)
        self.mp_3.setStyleSheet("background-color:transparent;")
        self.mp_3.setObjectName("mp_3")
        self.verticalLayout_2.addWidget(self.mp_3)
        self.mp_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.mp_4.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mp_4.setFont(font)
        self.mp_4.setStyleSheet("background-color:transparent;")
        self.mp_4.setObjectName("mp_4")
        self.verticalLayout_2.addWidget(self.mp_4)
        self.mp_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.mp_5.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mp_5.setFont(font)
        self.mp_5.setStyleSheet("background-color:transparent;")
        self.mp_5.setObjectName("mp_5")
        self.verticalLayout_2.addWidget(self.mp_5)
        self.mp_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.mp_6.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mp_6.setFont(font)
        self.mp_6.setStyleSheet("background-color:transparent;")
        self.mp_6.setObjectName("mp_6")
        self.verticalLayout_2.addWidget(self.mp_6)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(241, 0, 141, 331))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.o200 = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.o200.setFont(font)
        self.o200.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.o200.setText("")
        self.o200.setReadOnly(True)
        self.o200.setObjectName("o200")
        self.verticalLayout_3.addWidget(self.o200)
        self.o100 = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.o100.setFont(font)
        self.o100.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.o100.setText("")
        self.o100.setReadOnly(True)
        self.o100.setObjectName("o100")
        self.verticalLayout_3.addWidget(self.o100)
        self.o50 = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.o50.setFont(font)
        self.o50.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.o50.setText("")
        self.o50.setReadOnly(True)
        self.o50.setObjectName("o50")
        self.verticalLayout_3.addWidget(self.o50)
        self.o20 = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.o20.setFont(font)
        self.o20.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.o20.setText("")
        self.o20.setReadOnly(True)
        self.o20.setObjectName("o20")
        self.verticalLayout_3.addWidget(self.o20)
        self.o10 = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.o10.setFont(font)
        self.o10.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.o10.setText("")
        self.o10.setReadOnly(True)
        self.o10.setObjectName("o10")
        self.verticalLayout_3.addWidget(self.o10)
        self.o5 = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.o5.setFont(font)
        self.o5.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.o5.setText("")
        self.o5.setReadOnly(True)
        self.o5.setObjectName("o5")
        self.verticalLayout_3.addWidget(self.o5)
        self.layoutWidget3 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(700, 0, 72, 331))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.mp_7 = QtWidgets.QLabel(self.layoutWidget3)
        self.mp_7.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mp_7.setFont(font)
        self.mp_7.setStyleSheet("background-color:transparent;")
        self.mp_7.setObjectName("mp_7")
        self.verticalLayout_4.addWidget(self.mp_7)
        self.mp_8 = QtWidgets.QLabel(self.layoutWidget3)
        self.mp_8.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mp_8.setFont(font)
        self.mp_8.setStyleSheet("background-color:transparent;")
        self.mp_8.setObjectName("mp_8")
        self.verticalLayout_4.addWidget(self.mp_8)
        self.mp_9 = QtWidgets.QLabel(self.layoutWidget3)
        self.mp_9.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mp_9.setFont(font)
        self.mp_9.setStyleSheet("background-color:transparent;")
        self.mp_9.setObjectName("mp_9")
        self.verticalLayout_4.addWidget(self.mp_9)
        self.mp_10 = QtWidgets.QLabel(self.layoutWidget3)
        self.mp_10.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mp_10.setFont(font)
        self.mp_10.setStyleSheet("background-color:transparent;")
        self.mp_10.setObjectName("mp_10")
        self.verticalLayout_4.addWidget(self.mp_10)
        self.mp_11 = QtWidgets.QLabel(self.layoutWidget3)
        self.mp_11.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mp_11.setFont(font)
        self.mp_11.setStyleSheet("background-color:transparent;")
        self.mp_11.setObjectName("mp_11")
        self.verticalLayout_4.addWidget(self.mp_11)
        self.mp_12 = QtWidgets.QLabel(self.layoutWidget3)
        self.mp_12.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mp_12.setFont(font)
        self.mp_12.setStyleSheet("background-color:transparent;")
        self.mp_12.setObjectName("mp_12")
        self.verticalLayout_4.addWidget(self.mp_12)
        self.layoutWidget4 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget4.setGeometry(QtCore.QRect(790, 0, 91, 331))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.l2 = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.l2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2.setReadOnly(True)
        self.l2.setObjectName("l2")
        self.verticalLayout_5.addWidget(self.l2)
        self.l1 = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.l1.setReadOnly(True)
        self.l1.setObjectName("l1")
        self.verticalLayout_5.addWidget(self.l1)
        self.l05 = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l05.setFont(font)
        self.l05.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.l05.setAlignment(QtCore.Qt.AlignCenter)
        self.l05.setReadOnly(True)
        self.l05.setObjectName("l05")
        self.verticalLayout_5.addWidget(self.l05)
        self.l02 = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l02.setFont(font)
        self.l02.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.l02.setAlignment(QtCore.Qt.AlignCenter)
        self.l02.setReadOnly(True)
        self.l02.setObjectName("l02")
        self.verticalLayout_5.addWidget(self.l02)
        self.l01 = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l01.setFont(font)
        self.l01.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.l01.setAlignment(QtCore.Qt.AlignCenter)
        self.l01.setReadOnly(True)
        self.l01.setObjectName("l01")
        self.verticalLayout_5.addWidget(self.l01)
        self.l001 = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l001.setFont(font)
        self.l001.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.l001.setAlignment(QtCore.Qt.AlignCenter)
        self.l001.setReadOnly(True)
        self.l001.setObjectName("l001")
        self.verticalLayout_5.addWidget(self.l001)
        self.layoutWidget5 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget5.setGeometry(QtCore.QRect(910, 0, 142, 331))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.o2 = QtWidgets.QLineEdit(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.o2.setFont(font)
        self.o2.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.o2.setText("")
        self.o2.setReadOnly(True)
        self.o2.setObjectName("o2")
        self.verticalLayout_6.addWidget(self.o2)
        self.o1 = QtWidgets.QLineEdit(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.o1.setFont(font)
        self.o1.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.o1.setText("")
        self.o1.setReadOnly(True)
        self.o1.setObjectName("o1")
        self.verticalLayout_6.addWidget(self.o1)
        self.o05 = QtWidgets.QLineEdit(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.o05.setFont(font)
        self.o05.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.o05.setText("")
        self.o05.setReadOnly(True)
        self.o05.setObjectName("o05")
        self.verticalLayout_6.addWidget(self.o05)
        self.o02 = QtWidgets.QLineEdit(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.o02.setFont(font)
        self.o02.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.o02.setText("")
        self.o02.setReadOnly(True)
        self.o02.setObjectName("o02")
        self.verticalLayout_6.addWidget(self.o02)
        self.o01 = QtWidgets.QLineEdit(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.o01.setFont(font)
        self.o01.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.o01.setText("")
        self.o01.setReadOnly(True)
        self.o01.setObjectName("o01")
        self.verticalLayout_6.addWidget(self.o01)
        self.o001 = QtWidgets.QLineEdit(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.o001.setFont(font)
        self.o001.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);")
        self.o001.setText("")
        self.o001.setReadOnly(True)
        self.o001.setObjectName("o001")
        self.verticalLayout_6.addWidget(self.o001)
        self.info = QtWidgets.QLabel(self.frame_3)
        self.info.setGeometry(QtCore.QRect(680, 420, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        self.info.setFont(font)
        self.info.setStyleSheet("")
        self.info.setText("")
        self.info.setObjectName("info")
        self.identif = QtWidgets.QLineEdit(self.frame_3)
        self.identif.setGeometry(QtCore.QRect(430, 410, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.identif.setFont(font)
        self.identif.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"background-color:transparent;\n"
"border-bottom:2px solid rgb(0, 0, 0);\n"
"border-right:2px solid rgb(0, 0, 0);")
        self.identif.setText("")
        self.identif.setAlignment(QtCore.Qt.AlignCenter)
        self.identif.setReadOnly(False)
        self.identif.setObjectName("identif")
        self.label_27 = QtWidgets.QLabel(self.frame_3)
        self.label_27.setGeometry(QtCore.QRect(440, 360, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.print = QtWidgets.QPushButton(self.frame_2)
        self.print.setGeometry(QtCore.QRect(890, 530, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(16)
        self.print.setFont(font)
        self.print.setStyleSheet("QPushButton{\n"
"    border-radius:15px;\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0.475, y1:0, x2:0.534, y2:1, stop:0 rgba(206, 206, 206, 255), stop:1 rgba(156, 156, 156, 255));\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(0, 223, 164);\n"
" }")
        self.print.setObjectName("print")

        self.retranslateUi(dfgsdx)
        QtCore.QMetaObject.connectSlotsByName(dfgsdx)

    def retranslateUi(self, dfgsdx):
        _translate = QtCore.QCoreApplication.translate
        dfgsdx.setWindowTitle(_translate("dfgsdx", "dfgsdx"))
        self.date.setText(_translate("dfgsdx", "00:00:00"))
        self.label_5.setText(_translate("dfgsdx", "Utilisateur:"))
        self.time.setText(_translate("dfgsdx", "00/00/00"))
        self.label_9.setText(_translate("dfgsdx", "CAISSE MAD"))
        self.label_3.setText(_translate("dfgsdx", "MJDB"))
        self.sgeneral.setText(_translate("dfgsdx", "Solde Generale"))
        self.differ.setText(_translate("dfgsdx", "Différence"))
        self.caissemad.setText(_translate("dfgsdx", "Caisse MAD"))
        self.label_25.setText(_translate("dfgsdx", "Remarque:"))
        self.l200.setText(_translate("dfgsdx", "0"))
        self.l200.setPlaceholderText(_translate("dfgsdx", "Qté."))
        self.l100.setText(_translate("dfgsdx", "0"))
        self.l100.setPlaceholderText(_translate("dfgsdx", "Qté."))
        self.l50.setText(_translate("dfgsdx", "0"))
        self.l50.setPlaceholderText(_translate("dfgsdx", "Qté."))
        self.l20.setText(_translate("dfgsdx", "0"))
        self.l20.setPlaceholderText(_translate("dfgsdx", "Qté."))
        self.l10.setText(_translate("dfgsdx", "0"))
        self.l10.setPlaceholderText(_translate("dfgsdx", "Qté."))
        self.l5.setText(_translate("dfgsdx", "0"))
        self.l5.setPlaceholderText(_translate("dfgsdx", "Qté."))
        self.mp.setText(_translate("dfgsdx", "200 DH"))
        self.mp_2.setText(_translate("dfgsdx", "100 DH"))
        self.mp_3.setText(_translate("dfgsdx", "50 DH"))
        self.mp_4.setText(_translate("dfgsdx", "20 DH"))
        self.mp_5.setText(_translate("dfgsdx", "10 DH"))
        self.mp_6.setText(_translate("dfgsdx", "5 DH"))
        self.o200.setPlaceholderText(_translate("dfgsdx", "0.00 DH"))
        self.o100.setPlaceholderText(_translate("dfgsdx", "0.00 DH"))
        self.o50.setPlaceholderText(_translate("dfgsdx", "0.00 DH"))
        self.o20.setPlaceholderText(_translate("dfgsdx", "0.00 DH"))
        self.o10.setPlaceholderText(_translate("dfgsdx", "0.00 DH"))
        self.o5.setPlaceholderText(_translate("dfgsdx", "0.00 DH"))
        self.mp_7.setText(_translate("dfgsdx", "2 DH"))
        self.mp_8.setText(_translate("dfgsdx", "1 DH"))
        self.mp_9.setText(_translate("dfgsdx", "0.50 DH"))
        self.mp_10.setText(_translate("dfgsdx", "0.20 DH"))
        self.mp_11.setText(_translate("dfgsdx", "0.10 DH"))
        self.mp_12.setText(_translate("dfgsdx", "0.01 DH"))
        self.l2.setText(_translate("dfgsdx", "0"))
        self.l2.setPlaceholderText(_translate("dfgsdx", "Qté."))
        self.l1.setText(_translate("dfgsdx", "0"))
        self.l1.setPlaceholderText(_translate("dfgsdx", "Qté."))
        self.l05.setText(_translate("dfgsdx", "0"))
        self.l05.setPlaceholderText(_translate("dfgsdx", "Qté."))
        self.l02.setText(_translate("dfgsdx", "0"))
        self.l02.setPlaceholderText(_translate("dfgsdx", "Qté."))
        self.l01.setText(_translate("dfgsdx", "0"))
        self.l01.setPlaceholderText(_translate("dfgsdx", "Qté."))
        self.l001.setText(_translate("dfgsdx", "0"))
        self.l001.setPlaceholderText(_translate("dfgsdx", "Qté."))
        self.o2.setPlaceholderText(_translate("dfgsdx", "0.00 DH"))
        self.o1.setPlaceholderText(_translate("dfgsdx", "0.00 DH"))
        self.o05.setPlaceholderText(_translate("dfgsdx", "0.00 DH"))
        self.o02.setPlaceholderText(_translate("dfgsdx", "0.00 DH"))
        self.o01.setPlaceholderText(_translate("dfgsdx", "0.00 DH"))
        self.o001.setPlaceholderText(_translate("dfgsdx", "0.00 DH"))
        self.identif.setPlaceholderText(_translate("dfgsdx", "CNI"))
        self.label_27.setText(_translate("dfgsdx", "Identifiant:"))
        self.print.setText(_translate("dfgsdx", "Imprimer"))
