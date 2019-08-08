# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MenuData.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MenuData(object):
    def setupUi(self, MenuData):
        MenuData.setObjectName("MenuData")
        MenuData.resize(284, 224)
        MenuData.setMinimumSize(QtCore.QSize(284, 224))
        MenuData.setMaximumSize(QtCore.QSize(284, 224))
        self.tabWidget = QtWidgets.QTabWidget(MenuData)
        self.tabWidget.setGeometry(QtCore.QRect(2, 2, 280, 220))
        self.tabWidget.setMinimumSize(QtCore.QSize(280, 220))
        self.tabWidget.setMaximumSize(QtCore.QSize(280, 220))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnClear = QtWidgets.QPushButton(self.tab)
        self.btnClear.setObjectName("btnClear")
        self.verticalLayout.addWidget(self.btnClear)
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWid = QtWidgets.QWidget()
        self.scrollAreaWid.setGeometry(QtCore.QRect(0, 0, 274, 164))
        self.scrollAreaWid.setObjectName("scrollAreaWid")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWid)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWid)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout.setStretch(1, 9)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 80, 104, 71))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.tab_2, "")
        self.lineEditSearch = QtWidgets.QLineEdit(MenuData)
        self.lineEditSearch.setGeometry(QtCore.QRect(167, 2, 113, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.lineEditSearch.setFont(font)
        self.lineEditSearch.setText("")
        self.lineEditSearch.setMaxLength(15)
        self.lineEditSearch.setFrame(True)
        self.lineEditSearch.setObjectName("lineEditSearch")

        self.retranslateUi(MenuData)
        self.tabWidget.setCurrentIndex(1)
        self.btnClear.clicked.connect(self.lineEditSearch.clear)
        QtCore.QMetaObject.connectSlotsByName(MenuData)

    def retranslateUi(self, MenuData):
        _translate = QtCore.QCoreApplication.translate
        MenuData.setWindowTitle(_translate("MenuData", "Form"))
        self.btnClear.setText(_translate("MenuData", "×"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MenuData", "默认课程"))
        self.lineEdit.setText(_translate("MenuData", "的的"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MenuData", "自定义课程"))

