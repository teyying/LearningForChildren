# -*- coding: utf-8 -*-

"""
-------------------------------------
Created on 2020/4/7 21:27
@author: Teyying
@site: https://github.com/teyying
@email: 165227316@qq.com
-------------------------------------
@file: comboBox.py
@description:
@problem:
-------------------------------------

"""
from sys import argv, exit
from PyQt5.Qt import *
import cgitb

cgitb.enable(format='text')


class ComboBox(QComboBox):
    finished = pyqtSignal()

    def __init__(self, parent=None):
        super(ComboBox, self).__init__(parent)
        self.listWidget = QListWidget()
        self.setView(self.listWidget)
        self.setModel(self.listWidget.model())
        self.activated[int].connect(self.showAccount)
        self.setEditable(True)  # 设置可编辑，才有lineEdit子类的

        path = ":/login/images/login_icon_account_normal.png"
        self.lineEdit().addAction(QAction(QIcon(path), '', self), QLineEdit.LeadingPosition)  # 左侧图标
        self.lineEdit().setPlaceholderText('账号')  # 设置默认提示语
        self.lineEdit().setMaxLength(11)
        # self.lineEdit().setClearButtonEnabled(True)
        self.popupIsVisible = False

    def showAccount(self, index):
        item = self.listWidget.item(index)
        if item:  # AttributeError: 'NoneType' object has no attribute 'data'
            account = item.data(666)
            self.lineEdit().setText(account)

    def keyPressEvent(self, e):
        """处理按下回车键后会往下拉列表添加item的情况"""
        # 登录成功后把账号信息添加到数据库，再启动登录程序时，就把账号信息添加到下拉列表中
        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter:
            self.finished.emit()  # finished信号连接的是密码框setFocus
        else:
            return super().keyPressEvent(e)

    def addAcountItem(self, widget):
        widget.delItemSignal.connect(self.delItem)  #
        item = QListWidgetItem()
        item.setData(666, widget.account())
        widget.setProperty('item', item)
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, widget)

    def delItem(self, item):
        index = self.listWidget.row(item)
        self.removeItem(index)
        if not self.count():
            self.hidePopup()

    def showPopup(self):
        """下拉菜单显示事件(点击事件)"""
        self.popupIsVisible = True
        self.__setActionIcon(True)
        return super().showPopup()

    def hidePopup(self):
        self.popupIsVisible = False
        self.__setActionIcon(False)
        return super().hidePopup()

    def focusInEvent(self, e):
        self.__setActionIcon(True)
        return super().focusInEvent(e)

    def focusOutEvent(self, e):
        if not self.popupIsVisible:
            self.__setActionIcon(False)
        return super().focusOutEvent(e)

    def __setActionIcon(self, isFocus):
        if isFocus:
            path = ":/login/images/login_icon_account_hover.png"
        else:
            path = ":/login/images/login_icon_account_normal.png"
        self.lineEdit().actions()[0].setIcon(QIcon(path))


if __name__ == '__main__':
    app = QApplication(argv)
    window = ComboBox()
    window.show()
    exit(app.exec_())
