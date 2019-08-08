# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_CardMatching.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CardMatching(object):
    def setupUi(self, CardMatching):
        CardMatching.setObjectName("CardMatching")
        CardMatching.resize(980, 520)
        self.verticalLayout = QtWidgets.QVBoxLayout(CardMatching)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(CardMatching)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(70, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lab = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.lab.setFont(font)
        self.lab.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab.setObjectName("lab")
        self.horizontalLayout.addWidget(self.lab)
        self.labCount = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.labCount.setFont(font)
        self.labCount.setObjectName("labCount")
        self.horizontalLayout.addWidget(self.labCount)
        self.verticalLayout.addWidget(self.widget)
        self.widMatching = QtWidgets.QWidget(CardMatching)
        self.widMatching.setObjectName("widMatching")
        self.gridLayout = QtWidgets.QGridLayout(self.widMatching)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout.addWidget(self.widMatching)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 9)

        self.retranslateUi(CardMatching)
        QtCore.QMetaObject.connectSlotsByName(CardMatching)

    def retranslateUi(self, CardMatching):
        _translate = QtCore.QCoreApplication.translate
        CardMatching.setWindowTitle(_translate("CardMatching", "Form"))
        self.lab.setText(_translate("CardMatching", "剩余卡片对："))
        self.labCount.setText(_translate("CardMatching", "0"))


