# -*- coding: utf-8 -*-

"""
-------------------------------------
Created on 2020/4/7 20:06
@author: Teyying
@site: https://github.com/teyying
@email: 165227316@qq.com
-------------------------------------
@file: accountItemPane.py
@description:
@problem:
-------------------------------------

"""

from sys import argv, exit
from PyQt5.Qt import *
import cgitb

cgitb.enable(format='text')
from login.resource.accountItemUi import Ui_Form


class AccountItemPane(QWidget, Ui_Form):
    """这个是设计师画的用于QComboBox下拉菜单每个Item的界面，并设置有需要的情报接口"""
    delItemSignal = pyqtSignal(QListWidgetItem)

    def __init__(self, pixmap, nickname, account):
        super(AccountItemPane, self).__init__()
        self.setupUi(self)
        try:
            style = open("resource/keyBoard.css", encoding='utf8').read()
        except FileNotFoundError as e:
            style = open("login/resource/keyBoard.css", encoding='utf8').read()

        self.setStyleSheet(style)  # qss文件引入
        self.labItemUserAvatar.setPixmap(pixmap)
        self.labNickname.setText(nickname)
        self.labAccount.setText(account)

    def account(self):
        return self.labAccount.text()

    def delItem(self):
        # comboBox类中绑定有每个widget的'item'属性
        self.delItemSignal.emit(self.property('item'))


if __name__ == '__main__':
    app = QApplication(argv)
    window = AccountItemPane()
    window.show()
    exit(app.exec_())
