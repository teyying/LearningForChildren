# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Form.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(970, 373)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(50, 20, 900, 130))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(5, 5, 0, 5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pTEditUp = QtWidgets.QPlainTextEdit(self.widget)
        self.pTEditUp.setMinimumSize(QtCore.QSize(894, 0))
        self.pTEditUp.setMaximumSize(QtCore.QSize(894, 16777215))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(40)
        self.pTEditUp.setFont(font)
        self.pTEditUp.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pTEditUp.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pTEditUp.setObjectName("pTEditUp")
        self.verticalLayout.addWidget(self.pTEditUp)
        self.pTEditDn = QtWidgets.QPlainTextEdit(self.widget)
        self.pTEditDn.setMinimumSize(QtCore.QSize(894, 0))
        self.pTEditDn.setMaximumSize(QtCore.QSize(894, 16777215))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(40)
        self.pTEditDn.setFont(font)
        self.pTEditDn.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pTEditDn.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pTEditDn.setObjectName("pTEditDn")
        self.verticalLayout.addWidget(self.pTEditDn)
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(450, 280, 75, 23))
        self.btn.setObjectName("btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn.setText(_translate("Form", "PushButton"))


