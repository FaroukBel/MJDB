# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_acc.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_edit_colab(object):
    def setupUi(self, edit_colab):
        edit_colab.setObjectName("edit_colab")
        edit_colab.resize(345, 386)
        self.frame = QtWidgets.QFrame(edit_colab)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 361, 91))
        self.frame.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(14, 25, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(30)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(160, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.wrong1 = QtWidgets.QPushButton(edit_colab)
        self.wrong1.setGeometry(QtCore.QRect(230, 350, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.wrong1.setFont(font)
        self.wrong1.setObjectName("wrong1")
        self.label_4 = QtWidgets.QLabel(edit_colab)
        self.label_4.setGeometry(QtCore.QRect(30, 300, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(edit_colab)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 111, 49))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.desc = QtWidgets.QTextEdit(edit_colab)
        self.desc.setGeometry(QtCore.QRect(110, 150, 191, 131))
        self.desc.setObjectName("desc")
        self.nom1 = QtWidgets.QLineEdit(edit_colab)
        self.nom1.setGeometry(QtCore.QRect(70, 100, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        self.nom1.setFont(font)
        self.nom1.setStyleSheet("background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid #9f9f9f;")
        self.nom1.setObjectName("nom1")
        self.label_2 = QtWidgets.QLabel(edit_colab)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 51, 49))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(edit_colab)
        QtCore.QMetaObject.connectSlotsByName(edit_colab)

    def retranslateUi(self, edit_colab):
        _translate = QtCore.QCoreApplication.translate
        edit_colab.setWindowTitle(_translate("edit_colab", "edit_colab"))
        self.label_5.setText(_translate("edit_colab", "MJDB"))
        self.label_6.setText(_translate("edit_colab", "Editeur"))
        self.wrong1.setText(_translate("edit_colab", "Ok"))
        self.label_3.setText(_translate("edit_colab", "Description:"))
        self.nom1.setPlaceholderText(_translate("edit_colab", "Nom"))
        self.label_2.setText(_translate("edit_colab", "Nom:"))
