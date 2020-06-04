# -*- coding: utf-8 -*-

"""
-------------------------------------
Created on 2020/4/4 19:49
@author: Teyying
@site: https://github.com/teyying
@email: 165227316@qq.com
-------------------------------------
@file: keyboardPane.py
@description:
@problem:
-------------------------------------

"""
from sys import argv, exit
from PyQt5.Qt import *
import cgitb

from login.resource.keyBoardUi import Ui_Form

cgitb.enable(format='text')


class KeyboardPane(QWidget, Ui_Form):
    insertCharSignal = pyqtSignal(str)
    delPreStrSignal = pyqtSignal()

    def __init__(self):
        super(KeyboardPane, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.Popup)  # 设置为子窗口(非模态弹窗)
        try:
            style = open("resource/keyBoard.css", encoding='utf8').read()
        except FileNotFoundError as e:
            style = open("login/resource/keyBoard.css", encoding='utf8').read()

        self.setStyleSheet(style)  # qss文件引入
        self.btnSymbol = []
        self.btnLetter = []
        for i in self.children():
            if i.property('state'):
                i.clicked.connect(self.clicked)
            if i.property('state') == 'symbol':
                self.btnSymbol.append(i)
            elif i.property('state') == 'letter':
                self.btnLetter.append(i)

    def clicked(self):
        btn = self.sender()
        if btn.property('state') == 'shift':
            for i in self.btnSymbol:
                i.changeState()
        elif btn.property('state') == 'capsLock':
            for i in self.btnLetter:
                i.setText(i.text().upper() if btn.isChecked() else i.text().lower())
        elif btn.property('state') == 'symbol' or btn.property('state') == 'letter':
            self.insertCharSignal.emit(btn.text())

    def delPreStr(self):
        self.delPreStrSignal.emit()

    def closeEvent(self, QCloseEvent):
        self.deleteLater()


if __name__ == '__main__':
    app = QApplication(argv)
    window = KeyboardPane()
    window.show()
    exit(app.exec_())
