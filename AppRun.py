"""
Script Name		: AppRun.py
Author		    : Teyying
Created		    : 2018.5.17
Last Modified	: 2019.1.22
Version		    : 4.2   算是第个四版本了,前两个版本是用Tkinter写的，第三版本没用设计师设计界面。
                 这第四版本用设计师画界面，相当于重写了一次，之前的代码做了大幅改动优化，并大动了
                 两次文件目录布局，往后就可以以插件形式慢慢无限添加各种想要的功能了。
Description		: 这是用PyQt5编写的帮助儿童学习汉字,英语,数学算式的GUI程序,并有游戏、音乐、动画。
Pending Problem : 目前没有困难问题
Next Step       : 1.margin可以折叠垂直元素,是否可以做一个指定显示几个按钮的效果.
"""

from sys import argv
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import (QApplication, QSplashScreen)

from UiLogin.Ui_Login_Logic import Ui_Login_Logic
from UiMain.Ui_Main_Logic import Ui_Main_Logic

class App(QApplication):
    """封装QApplication仅仅是为了让Ui_Main_Logic中的self.widMenu，有QMenu的效果"""
    def __init__(self, *args):
        super().__init__(*args)
        self.flagMenuLeave = False
        self.widget = None  # 从Ui_Main_Logic初始化中，赋值给它，self.app.widget = self.widMenu

    def notify(self, obj, e):
        if self.flagMenuLeave and e.type() == e.MouseButtonPress:
            self.widget.hide()
        if obj == self and e.type() == e.Close:
            # QEvent().Close
            # print(22222222)
            pass
        return super().notify(obj, e)

if __name__ == '__main__':
    # app = QApplication(argv)
    app = App(argv)
    app.setStyleSheet(open("Style.qss", encoding='utf8').read())  # qss文件引入
    font = QFont()
    font.setPointSize(13)
    font.setFamily("Roman Times")
    app.setFont(font)

    splash = QSplashScreen(QPixmap("run.png"))  # 设置启动界面
    splash.show()  # 显示启动画面

    window = Ui_Main_Logic(app) # 实例化主窗口
    window.setAttribute(Qt.WA_StyledBackground) # 这一句可以解决QWidget不显示图片的问题。不用重写paintEvent了。
    window.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏标题栏
    window.show()
    splash.finish(window)  # 窗体对象初始化完成后，结束启动画面


    uiLogin = Ui_Login_Logic(window)  # 登录界面
    uiLogin.exec()  # 登录界面同时模态显示

    exit(app.exec_())

