# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_DialogChoose.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogChoose(object):
    def setupUi(self, DialogChoose):
        DialogChoose.setObjectName("DialogChoose")
        DialogChoose.resize(400, 200)
        DialogChoose.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogChoose)
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(DialogChoose)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(DialogChoose)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 85, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.widget = QtWidgets.QWidget(DialogChoose)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(0, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(220, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 2)

        self.retranslateUi(DialogChoose)
        self.pushButton_2.clicked.connect(DialogChoose.close)
        QtCore.QMetaObject.connectSlotsByName(DialogChoose)

    def retranslateUi(self, DialogChoose):
        _translate = QtCore.QCoreApplication.translate
        DialogChoose.setWindowTitle(_translate("DialogChoose", "提交作业"))
        self.label_2.setText(_translate("DialogChoose", "提交作业"))
        self.label.setText(_translate("DialogChoose", "小朋友，检查过了吗？\n"
"要养成检查作业的好习惯哦！"))
        self.pushButton.setText(_translate("DialogChoose", "确定"))
        self.pushButton_2.setText(_translate("DialogChoose", "取消"))


