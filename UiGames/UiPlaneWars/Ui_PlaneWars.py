# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_PlaneWars.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PlaneWars(object):
    def setupUi(self, PlaneWars):
        PlaneWars.setObjectName("PlaneWars")
        PlaneWars.resize(980, 520)
        PlaneWars.setMinimumSize(QtCore.QSize(980, 520))
        self.label = QtWidgets.QLabel(PlaneWars)
        self.label.setGeometry(QtCore.QRect(20, 220, 54, 51))
        self.label.setObjectName("label")

        self.retranslateUi(PlaneWars)
        QtCore.QMetaObject.connectSlotsByName(PlaneWars)

    def retranslateUi(self, PlaneWars):
        _translate = QtCore.QCoreApplication.translate
        PlaneWars.setWindowTitle(_translate("PlaneWars", "Form"))
        self.label.setText(_translate("PlaneWars", "飞机"))


