# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Music.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Music(object):
    def setupUi(self, Music):
        Music.setObjectName("Music")
        Music.resize(980, 520)
        Music.setMinimumSize(QtCore.QSize(980, 520))
        self.widget = QtWidgets.QWidget(Music)
        self.widget.setGeometry(QtCore.QRect(200, 350, 391, 151))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setStatusTip("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setStatusTip("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStatusTip("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.tableWidget = QtWidgets.QTableWidget(Music)
        self.tableWidget.setGeometry(QtCore.QRect(80, 80, 511, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        self.retranslateUi(Music)
        QtCore.QMetaObject.connectSlotsByName(Music)

    def retranslateUi(self, Music):
        _translate = QtCore.QCoreApplication.translate
        Music.setWindowTitle(_translate("Music", "Form"))
        self.pushButton_3.setToolTip(_translate("Music", "上一首"))
        self.pushButton_3.setText(_translate("Music", "上一首"))
        self.pushButton_2.setToolTip(_translate("Music", "播放"))
        self.pushButton_2.setText(_translate("Music", "播放"))
        self.pushButton.setToolTip(_translate("Music", "下一首"))
        self.pushButton.setText(_translate("Music", "下一首"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Music", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Music", "音乐"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Music", "歌手"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Music", "专辑"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Music", "时长"))


