# -*- coding: utf-8 -*-

"""
-------------------------------------
Created on 2020/4/3 13:42
@author: Teyying
@site: https://github.com/teyying
@email: 165227316@qq.com
-------------------------------------
@file: registerPane.py
@description:
@problem:
-------------------------------------

"""
from sys import argv, exit
from PyQt5.Qt import *
import cgitb

from login.resource.registerUi import Ui_Form
cgitb.enable(format='text')
# QWidget#Form {border-images: url(:/register/images/register_bg.png);}

class RegisterPane(QWidget, Ui_Form):
    exitSignal = pyqtSignal()
    registerSignal = pyqtSignal(str, str, str)

    def __init__(self):
        super(RegisterPane, self).__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        try:
            style = open("resource/register.css", encoding='utf8').read()
        except FileNotFoundError as e:
            style = open("login/resource/register.css", encoding='utf8').read()

        self.setStyleSheet(style)  # qss文件引入
        self.flagMove = False

        # 用遮罩的方法给窗体设置圆角
        whiteMask = QBitmap(self.size())  # 创建位图，窗体大小
        whiteMask.fill(Qt.white)  # 填充位图全白，相当于把窗口擦掉了，后面再用黑色画刷显示出来。
        self.p = QPainter(whiteMask)
        self.p.setRenderHint(QPainter.Antialiasing)  # 使用抗锯齿的方式渲染
        self.p.setBrush(QBrush(Qt.black))  # 设置画刷
        self.p.drawRoundedRect(QRectF(0.0, 0.0, self.width(), self.height()), 5.0, 5.0)  # 给矩形添加圆角
        self.setMask(whiteMask)  # 设置遮罩

    def checkRegister(self):
        account = self.leAccount.text()
        password = self.lePassword.text()
        nickname = self.leNickname.text()
        self.registerSignal.emit(account, password, nickname)

    def exitPane(self):
        self.exitSignal.emit()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.setFocus()  # 主要处理焦点在账号和密码框内时，左键窗口的焦点位置，让输入框失去焦点
            self.flagMove = True
            self.posMove = e.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            e.accept()
        elif e.button() == Qt.RightButton:  # 如果焦点在密码框里，右键窗口的焦点位置，账号框会得到焦点并全选
            if self.lePassword.hasFocus():
                self.comboAccount.setFocus()
                self.comboAccount.lineEdit().selectAll()

    def mouseMoveEvent(self, e):
        if Qt.LeftButton and self.flagMove:
            self.move(e.globalPos() - self.posMove)  # 更改窗口位置
            e.accept()

    def mouseReleaseEvent(self, e):
        self.flagMove = False


if __name__ == '__main__':
    app = QApplication(argv)
    window = RegisterPane()
    window.exitSignal.connect(lambda: print('退出注册界面'))
    window.registerSignal.connect(lambda a, b, c: print(a, b, c))
    window.show()
    exit(app.exec_())
