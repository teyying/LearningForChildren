# -*- coding: utf-8 -*-

"""
-------------------------------------
Created on 2020/4/6 16:51
@author: Teyying
@site: https://github.com/teyying
@email: 165227316@qq.com
-------------------------------------
@file: keyboardBtn.py
@description:
@problem:
-------------------------------------

"""
from sys import argv, exit
from PyQt5.Qt import *
import cgitb

cgitb.enable(format='text')



class KeyboardBtn(QPushButton):

    def __init__(self, parent=None):
        super(KeyboardBtn, self).__init__(parent)

    def changeState(self):
        for i in self.children():
            if isinstance(i, QLabel):  # and i.isEnabled()
                i.setEnabled(not i.isEnabled())

    def text(self):
        for i in self.children():
            if isinstance(i, QLabel) and i.isEnabled():  # and i.isEnabled()
                    return i.text()




if __name__ == '__main__':
    app = QApplication(argv)
    window = KeyboardBtn()
    window.show()
    exit(app.exec_())
