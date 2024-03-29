# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'motif.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_efed(object):
    def setupUi(self, efed):
        efed.setObjectName("efed")
        efed.setWindowModality(QtCore.Qt.ApplicationModal)
        efed.resize(380, 241)
        self.frame = QtWidgets.QFrame(efed)
        self.frame.setGeometry(QtCore.QRect(0, 0, 381, 241))
        self.frame.setStyleSheet("QFrame#frame{\n"
"    border-radius:15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.116919 rgba(0, 115, 173, 255), stop:0.944118 rgba(0, 0, 0, 255));\n"
"    \n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.title_bar = QtWidgets.QFrame(self.frame)
        self.title_bar.setGeometry(QtCore.QRect(-1, -1, 381, 41))
        self.title_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.mini = QtWidgets.QPushButton(self.title_bar)
        self.mini.setGeometry(QtCore.QRect(320, 10, 20, 20))
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
        self.label = QtWidgets.QLabel(self.title_bar)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.close_btn = QtWidgets.QPushButton(self.title_bar)
        self.close_btn.setGeometry(QtCore.QRect(350, 10, 20, 20))
        self.close_btn.setMinimumSize(QtCore.QSize(20, 20))
        self.close_btn.setMaximumSize(QtCore.QSize(20, 20))
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
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(100, 140, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.motif = QtWidgets.QTextEdit(self.frame)
        self.motif.setGeometry(QtCore.QRect(33, 106, 331, 121))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(14)
        self.motif.setFont(font)
        self.motif.setStyleSheet("background-color:transparent;\n"
"color: rgb(255, 255, 255);\n"
"border-bottom:1px solid rgb(255, 255, 255);\n"
"border-right:1px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"")
        self.motif.setReadOnly(True)
        self.motif.setObjectName("motif")

        self.retranslateUi(efed)
        QtCore.QMetaObject.connectSlotsByName(efed)

    def retranslateUi(self, efed):
        _translate = QtCore.QCoreApplication.translate
        efed.setWindowTitle(_translate("efed", "efed"))
        self.label.setText(_translate("efed", "Annulation"))
        self.label_2.setText(_translate("efed", "Motif d\'annulation :"))
