# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Games_Guess.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Games_Guess(object):
    def setupUi(self, Games_Guess):
        Games_Guess.setObjectName("Games_Guess")
        Games_Guess.resize(980, 522)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Games_Guess)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(Games_Guess)
        self.widget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget = QtWidgets.QWidget(self.widget_5)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.labCountPrevious = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(25)
        self.labCountPrevious.setFont(font)
        self.labCountPrevious.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labCountPrevious.setObjectName("labCountPrevious")
        self.verticalLayout_2.addWidget(self.labCountPrevious)
        self.horizontalLayout_4.addWidget(self.widget)
        self.labDisplayNum = QtWidgets.QLabel(self.widget_5)
        self.labDisplayNum.setMinimumSize(QtCore.QSize(350, 0))
        self.labDisplayNum.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(50)
        self.labDisplayNum.setFont(font)
        self.labDisplayNum.setAlignment(QtCore.Qt.AlignCenter)
        self.labDisplayNum.setObjectName("labDisplayNum")
        self.horizontalLayout_4.addWidget(self.labDisplayNum)
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.labCountPresently = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(25)
        self.labCountPresently.setFont(font)
        self.labCountPresently.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labCountPresently.setObjectName("labCountPresently")
        self.verticalLayout_3.addWidget(self.labCountPresently)
        self.horizontalLayout_4.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnGuess = QtWidgets.QPushButton(self.widget_4)
        self.btnGuess.setMinimumSize(QtCore.QSize(160, 160))
        self.btnGuess.setMaximumSize(QtCore.QSize(160, 160))
        self.btnGuess.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGuess.setObjectName("btnGuess")
        self.horizontalLayout_3.addWidget(self.btnGuess)
        self.labGuess = QtWidgets.QLabel(self.widget_4)
        self.labGuess.setMinimumSize(QtCore.QSize(160, 160))
        self.labGuess.setMaximumSize(QtCore.QSize(160, 160))
        self.labGuess.setText("")
        self.labGuess.setObjectName("labGuess")
        self.horizontalLayout_3.addWidget(self.labGuess)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 135))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 135))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labSmall = QtWidgets.QLabel(self.widget_3)
        self.labSmall.setMinimumSize(QtCore.QSize(130, 130))
        self.labSmall.setMaximumSize(QtCore.QSize(130, 130))
        self.labSmall.setText("")
        self.labSmall.setObjectName("labSmall")
        self.horizontalLayout_2.addWidget(self.labSmall)
        self.labBig = QtWidgets.QLabel(self.widget_3)
        self.labBig.setMinimumSize(QtCore.QSize(130, 130))
        self.labBig.setMaximumSize(QtCore.QSize(130, 130))
        self.labBig.setText("")
        self.labBig.setObjectName("labBig")
        self.horizontalLayout_2.addWidget(self.labBig)
        self.labGuessRight = QtWidgets.QLabel(self.widget_3)
        self.labGuessRight.setMinimumSize(QtCore.QSize(329, 130))
        self.labGuessRight.setMaximumSize(QtCore.QSize(329, 130))
        self.labGuessRight.setText("")
        self.labGuessRight.setObjectName("labGuessRight")
        self.horizontalLayout_2.addWidget(self.labGuessRight)
        self.verticalLayout.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget_2)
        self.widInput = QtWidgets.QWidget(Games_Guess)
        self.widInput.setEnabled(True)
        self.widInput.setObjectName("widInput")
        self.gridLayout = QtWidgets.QGridLayout(self.widInput)
        self.gridLayout.setContentsMargins(80, 60, 40, 40)
        self.gridLayout.setObjectName("gridLayout")
        self.btn1 = QtWidgets.QPushButton(self.widInput)
        self.btn1.setMinimumSize(QtCore.QSize(110, 100))
        self.btn1.setMaximumSize(QtCore.QSize(110, 100))
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 0, 2, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.widInput)
        self.btn3.setMinimumSize(QtCore.QSize(110, 100))
        self.btn3.setMaximumSize(QtCore.QSize(110, 100))
        self.btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn3.setObjectName("btn3")
        self.gridLayout.addWidget(self.btn3, 0, 4, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.widInput)
        self.btn2.setMinimumSize(QtCore.QSize(110, 100))
        self.btn2.setMaximumSize(QtCore.QSize(110, 100))
        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 0, 3, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.widInput)
        self.btn6.setMinimumSize(QtCore.QSize(110, 100))
        self.btn6.setMaximumSize(QtCore.QSize(110, 100))
        self.btn6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn6.setObjectName("btn6")
        self.gridLayout.addWidget(self.btn6, 1, 4, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.widInput)
        self.btn8.setMinimumSize(QtCore.QSize(110, 100))
        self.btn8.setMaximumSize(QtCore.QSize(110, 100))
        self.btn8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn8.setObjectName("btn8")
        self.gridLayout.addWidget(self.btn8, 2, 3, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.widInput)
        self.btn5.setMinimumSize(QtCore.QSize(110, 100))
        self.btn5.setMaximumSize(QtCore.QSize(110, 100))
        self.btn5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn5.setObjectName("btn5")
        self.gridLayout.addWidget(self.btn5, 1, 3, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.widInput)
        self.btn7.setMinimumSize(QtCore.QSize(110, 100))
        self.btn7.setMaximumSize(QtCore.QSize(110, 100))
        self.btn7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn7.setObjectName("btn7")
        self.gridLayout.addWidget(self.btn7, 2, 2, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.widInput)
        self.btn4.setMinimumSize(QtCore.QSize(110, 100))
        self.btn4.setMaximumSize(QtCore.QSize(110, 100))
        self.btn4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn4.setObjectName("btn4")
        self.gridLayout.addWidget(self.btn4, 1, 2, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.widInput)
        self.btn9.setMinimumSize(QtCore.QSize(110, 100))
        self.btn9.setMaximumSize(QtCore.QSize(110, 100))
        self.btn9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn9.setObjectName("btn9")
        self.gridLayout.addWidget(self.btn9, 2, 4, 1, 1)
        self.btn0 = QtWidgets.QPushButton(self.widInput)
        self.btn0.setMinimumSize(QtCore.QSize(110, 100))
        self.btn0.setMaximumSize(QtCore.QSize(110, 100))
        self.btn0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn0.setObjectName("btn0")
        self.gridLayout.addWidget(self.btn0, 3, 2, 1, 1)
        self.btnBackspace = QtWidgets.QPushButton(self.widInput)
        self.btnBackspace.setMinimumSize(QtCore.QSize(110, 100))
        self.btnBackspace.setMaximumSize(QtCore.QSize(110, 100))
        self.btnBackspace.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBackspace.setObjectName("btnBackspace")
        self.gridLayout.addWidget(self.btnBackspace, 3, 3, 1, 1)
        self.btnOk = QtWidgets.QPushButton(self.widInput)
        self.btnOk.setMinimumSize(QtCore.QSize(110, 100))
        self.btnOk.setMaximumSize(QtCore.QSize(110, 100))
        self.btnOk.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnOk.setObjectName("btnOk")
        self.gridLayout.addWidget(self.btnOk, 3, 4, 1, 1)
        self.horizontalLayout.addWidget(self.widInput)

        self.retranslateUi(Games_Guess)
        QtCore.QMetaObject.connectSlotsByName(Games_Guess)

    def retranslateUi(self, Games_Guess):
        _translate = QtCore.QCoreApplication.translate
        Games_Guess.setWindowTitle(_translate("Games_Guess", "Form"))
        self.label.setText(_translate("Games_Guess", "上一局\n"
"次数"))
        self.labCountPrevious.setText(_translate("Games_Guess", "0"))
        self.labDisplayNum.setText(_translate("Games_Guess", "??"))
        self.label_3.setText(_translate("Games_Guess", "当前\n"
"次数"))
        self.labCountPresently.setText(_translate("Games_Guess", "0"))
        self.btnGuess.setText(_translate("Games_Guess", "猜"))
        self.btn1.setText(_translate("Games_Guess", "1"))
        self.btn3.setText(_translate("Games_Guess", "3"))
        self.btn2.setText(_translate("Games_Guess", "2"))
        self.btn6.setText(_translate("Games_Guess", "6"))
        self.btn8.setText(_translate("Games_Guess", "8"))
        self.btn5.setText(_translate("Games_Guess", "5"))
        self.btn7.setText(_translate("Games_Guess", "7"))
        self.btn4.setText(_translate("Games_Guess", "4"))
        self.btn9.setText(_translate("Games_Guess", "9"))
        self.btn0.setText(_translate("Games_Guess", "0"))
        self.btnBackspace.setText(_translate("Games_Guess", "backspace"))
        self.btnOk.setText(_translate("Games_Guess", "ok"))


