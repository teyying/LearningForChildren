# -*- coding: utf-8 -*-

"""
-------------------------------------
Created on 2020/4/20 17:36
@author: Teyying
@site: https://github.com/teyying
@email: 165227316@qq.com
-------------------------------------
@file: controller.py
@description:
@problem:
-------------------------------------

"""
from sys import argv, exit
from PyQt5.Qt import *
import cgitb

from login.accountItemPane import AccountItemPane
from login.keyboardPane import KeyboardPane
from login.loginPane import LoginPane
from login.registerPane import RegisterPane

cgitb.enable(format='text')


# todo 槽函数是否都加上slot，以及加上"__"私有方法
# todo 怎么取得comboBox 划过item时的信号，不知怎么得到此item
class Controller(QObject):
    def __init__(self):
        super(Controller, self).__init__()
        self.loginPane = LoginPane()
        self.registerPane = RegisterPane()
        self.loginPane.comboAccount.setFocus()  # 账号控件设置焦点后，登录界面的自定义信号

        # 信号与槽设置
        self.registerPane.exitSignal.connect(self.changePane)
        self.loginPane.showRegisterPaneSignal.connect(self.changePane)
        self.loginPane.showKeyboardPaneSignal.connect(self.showKeyboardPane)
        # self.loginPane.checkLoginSignal.connect(self.fn)

        self.loginPane.addAccountItemSignal.emit(AccountItemPane(QPixmap(), '悄好', '123215221'))
        self.loginPane.addAccountItemSignal.emit(AccountItemPane(QPixmap(), '悄321好', '215221'))
        self.loginPane.addAccountItemSignal.emit(AccountItemPane(QPixmap(), '悄555好', '1232'))

    def changePane(self):
        def state():  # 显示要打开的界面，隐藏当前界面
            otherOne.show()
            sender.hide()

        def openingSignal():  # 设置禁用状态为False
            self.loginPane.setDisabled(False)
            self.registerPane.setDisabled(False)

        sender = self.sender()  # 当前界面
        otherOne = [i for i in [self.loginPane, self.registerPane] if i is not sender][0]  # 得到要打开的界面
        self.loginPane.setDisabled(True)  # 设置禁用状态为True
        self.registerPane.setDisabled(True)

        rect = QRect(QPoint(sender.x(), sender.y() - sender.height()), sender.size())
        animation1 = QPropertyAnimation(sender, b'geometry')
        animation1.setDuration(500)
        animation1.setEasingCurve(QEasingCurve.InOutBack)
        animation1.setStartValue(sender.geometry())
        animation1.setEndValue(rect)
        animation1.finished.connect(state)
        animation2 = QPropertyAnimation(otherOne, b'geometry')
        animation2.setDuration(500)
        animation2.setEasingCurve(QEasingCurve.InCurve)
        animation2.setStartValue(rect)
        animation2.setEndValue(sender.geometry())
        animation_group = QSequentialAnimationGroup(self)  # 实例化一个串行动画
        animation_group.addAnimation(animation1)  # 添加属性动画
        animation_group.addAnimation(animation2)
        animation_group.start(animation_group.DeleteWhenStopped)  # 启动串行动画
        animation_group.finished.connect(openingSignal)

    def fn(self, account, password):
        print(account, password)

    def showKeyboardPane(self):
        self.keyboardPane = KeyboardPane()
        self.keyboardPane.delPreStrSignal.connect(self.loginPane.lePassword.backspace)
        self.keyboardPane.insertCharSignal[str].connect(lambda s: self.loginPane.lePassword.insert(s))
        self.keyboardPane.move(QPoint(self.loginPane.cursor().pos().x() - 300, self.loginPane.cursor().pos().y() + 25))
        self.keyboardPane.show()

if __name__ == '__main__':
    app = QApplication(argv)
    controller = Controller()
    controller.loginPane.show()
    exit(app.exec_())
