# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accountItem.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(250, 60)
        Form.setMinimumSize(QtCore.QSize(250, 0))
        Form.setMaximumSize(QtCore.QSize(250, 16777215))
        Form.setStyleSheet("")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setContentsMargins(10, 0, 15, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labItemUserAvatar = QtWidgets.QLabel(Form)
        self.labItemUserAvatar.setMinimumSize(QtCore.QSize(50, 50))
        self.labItemUserAvatar.setMaximumSize(QtCore.QSize(50, 50))
        self.labItemUserAvatar.setStyleSheet("")
        self.labItemUserAvatar.setText("")
        self.labItemUserAvatar.setObjectName("labItemUserAvatar")
        self.horizontalLayout_2.addWidget(self.labItemUserAvatar)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labNickname = QtWidgets.QLabel(Form)
        self.labNickname.setMinimumSize(QtCore.QSize(144, 0))
        self.labNickname.setMaximumSize(QtCore.QSize(144, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.labNickname.setFont(font)
        self.labNickname.setText("")
        self.labNickname.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.labNickname.setObjectName("labNickname")
        self.verticalLayout.addWidget(self.labNickname)
        self.labAccount = QtWidgets.QLabel(Form)
        self.labAccount.setEnabled(False)
        self.labAccount.setMinimumSize(QtCore.QSize(144, 0))
        self.labAccount.setMaximumSize(QtCore.QSize(144, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.labAccount.setFont(font)
        self.labAccount.setText("")
        self.labAccount.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labAccount.setObjectName("labAccount")
        self.verticalLayout.addWidget(self.labAccount)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.btnDelItem = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelItem.sizePolicy().hasHeightForWidth())
        self.btnDelItem.setSizePolicy(sizePolicy)
        self.btnDelItem.setMinimumSize(QtCore.QSize(20, 20))
        self.btnDelItem.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.btnDelItem.setFont(font)
        self.btnDelItem.setStyleSheet("")
        self.btnDelItem.setObjectName("btnDelItem")
        self.horizontalLayout_2.addWidget(self.btnDelItem)

        self.retranslateUi(Form)
        self.btnDelItem.clicked.connect(Form.delItem)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnDelItem.setToolTip(_translate("Form", "删除账号信息"))
        self.btnDelItem.setText(_translate("Form", "×"))
