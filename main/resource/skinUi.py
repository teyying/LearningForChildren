# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'skin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Skin(object):
    def setupUi(self, Skin):
        Skin.setObjectName("Skin")
        Skin.resize(233, 183)
        Skin.setMinimumSize(QtCore.QSize(233, 183))
        Skin.setMaximumSize(QtCore.QSize(233, 183))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Skin)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(Skin)
        self.tabWidget.setMinimumSize(QtCore.QSize(233, 183))
        self.tabWidget.setMaximumSize(QtCore.QSize(233, 183))
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollAreaTab1 = QtWidgets.QScrollArea(self.tab)
        self.scrollAreaTab1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollAreaTab1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollAreaTab1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollAreaTab1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollAreaTab1.setWidgetResizable(True)
        self.scrollAreaTab1.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollAreaTab1.setObjectName("scrollAreaTab1")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 210, 158))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridTab1 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridTab1.setContentsMargins(2, -1, 2, 2)
        self.gridTab1.setSpacing(2)
        self.gridTab1.setObjectName("gridTab1")
        self.scrollAreaTab1.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollAreaTab1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollAreaTab2 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollAreaTab2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollAreaTab2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollAreaTab2.setLineWidth(1)
        self.scrollAreaTab2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollAreaTab2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollAreaTab2.setWidgetResizable(True)
        self.scrollAreaTab2.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollAreaTab2.setObjectName("scrollAreaTab2")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 210, 158))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridTab2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridTab2.setContentsMargins(2, -1, 2, 2)
        self.gridTab2.setSpacing(2)
        self.gridTab2.setObjectName("gridTab2")
        self.scrollAreaTab2.setWidget(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_2.addWidget(self.scrollAreaTab2)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)

        self.retranslateUi(Skin)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Skin)

    def retranslateUi(self, Skin):
        _translate = QtCore.QCoreApplication.translate
        Skin.setWindowTitle(_translate("Skin", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Skin", "静图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Skin", "动图"))
