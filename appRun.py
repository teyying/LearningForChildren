# -*- coding: utf-8 -*-

"""
-------------------------------------
Created on 2020/4/21 23:20
@author: Teyying
@site: https://github.com/teyying
@email: 165227316@qq.com
-------------------------------------
@file: appRun.py
@description:
@problem:
-------------------------------------

"""
from sys import argv, exit
from PyQt5.Qt import *
import cgitb


cgitb.enable(format='text')

from login.controller import Controller as LoginContoller

class appRun(LoginContoller):
    def __init__(self):
        super(appRun, self).__init__()
        self.loginPane.checkLoginSignal[str, str].connect(self.checkLogin)

        self.loginPane.comboAccount.setCurrentText('1')
        self.loginPane.lePassword.setText('1')

    def checkLogin(self, account, password):
        print(f"账号：{account}, 密码：{password}", end='\t')
        if account and password:
            from main.controller import Controller as MainContoller
            self.mainContoller = MainContoller()
            self.mainContoller.mainPane.show()
            self.loginPane.close()
            print('成功登陆主界面')



if __name__ == '__main__':
    app = QApplication(argv)
    appRun = appRun()
    appRun.loginPane.show()
    exit(app.exec_())
