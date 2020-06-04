# -*- coding: utf-8 -*-

"""
-------------------------------------
Created on 2020/4/22 14:40
@author: Teyying
@site: https://github.com/teyying
@email: 165227316@qq.com
-------------------------------------
@file: mainPane.py
@description:
@problem:
-------------------------------------

"""
from os import listdir
from sys import argv, exit
from PyQt5.Qt import *
from main.resource.mainUi import Ui_Main

import cgitb

cgitb.enable(format='text')


class MainPane(QLabel, Ui_Main):
    showSkinSignal = pyqtSignal()
    loadButtons = pyqtSignal()

    def __init__(self):
        super(MainPane, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setScaledContents(True)
        self.setBorderRadius(True)
        self.center()
        self.widTitle.installEventFilter(self)

        # # 用遮罩的方法给窗体设置圆角
        # whiteMask = QBitmap(self.size())  # 创建位图，窗体大小
        # whiteMask.fill(Qt.white)  # 填充位图全白，相当于把窗口擦掉了，后面再用黑色画刷显示出来。
        # self.p = QPainter(whiteMask)
        # self.p.setRenderHint(QPainter.Antialiasing)  # 使用抗锯齿的方式渲染
        # self.p.setBrush(QBrush(Qt.black))  # 设置画刷
        # self.p.drawRoundedRect(QRectF(0.0, 0.0, self.width(), self.height()), 5.0, 5.0)  # 给矩形添加圆角
        # self.setMask(whiteMask)  # 设置遮罩

        self.flagMove = False

        try:
            style = open("resource/main.css", encoding='utf8').read()
        except FileNotFoundError as e:
            style = open("main/resource/main.css", encoding='utf8').read()
        self.setStyleSheet(style)  # qss文件引入

        print(self.pushButton_6.isChecked())
        self.loadButtons.connect(self.fn)
        self.pushButton_6.clicked[bool].connect(lambda x: self.showFullScreen() if x else self.showNormal())

    def fn4(self, x):
        if x:
            self.showFullScreen()
        else:
            self.showNormal()

    def showFullScreen(self):
        super().showFullScreen()
        self.setBorderRadius(False)


    # def showNormal(self):
    #     self.resize(self.minimumSize())
    #
    #     return super().showNormal()

    def setBorderRadius(self, _bool: bool):
        if _bool:
            # 用遮罩的方法给窗体设置圆角
            whiteMask = QBitmap(self.size())  # 创建位图，窗体大小
            whiteMask.fill(Qt.white)  # 填充位图全白，相当于把窗口擦掉了，后面再用黑色画刷显示出来。
            self.p = QPainter(whiteMask)
            self.p.setRenderHint(QPainter.Antialiasing)  # 使用抗锯齿的方式渲染
            self.p.setBrush(QBrush(Qt.black))  # 设置画刷
            self.p.drawRoundedRect(QRectF(0.0, 0.0, self.width(), self.height()), 5.0, 5.0)  # 给矩形添加圆角
            self.setMask(whiteMask)  # 设置遮罩
        else:
            blackMask = QBitmap(self.size())
            blackMask.fill(Qt.black)  # 填充黑色位图，相当于把窗口显示出来
            self.setMask(blackMask)  # 设置遮罩

    def changePage(self):
        index = self.sender().property('pageIndex')
        self.stkWid.setCurrentIndex(index)

        # if index == 1:
        #     origin_path = "plugins/study/cn"
        #     filenames = listdir(origin_path)
        #     for filename in filenames:
        #         __import__(f"plugins.study.cn.{filename}.resource.logo_rc")
        #
        #         btn = QPushButton()
        #         btn.setFixedSize(163, 163)
        #         btn.setIconSize(QSize(163, 163))
        #         btn.setIcon(QIcon(f":/{filename}/images/logo.png"))
        #         self.addToGridLayout(getattr(self, f"gridLayout_{index}"), btn)
        #         return

    def fn(self):
        # a = "plugins.study.cn.{filename}.resource.logo_rc"
        # a = "plugins.study.math.{filename}.resource.logo_rc"
        # a = "plugins.study.en.{filename}.resource.logo_rc"
        # a = "plugins.play.game.{filename}.resource.logo_rc"
        # a = "plugins.play.movie.{filename}.resource.logo_rc"
        # a = "plugins.play.music.{filename}.resource.logo_rc"
        # a = ["plugins.study.cn.", "plugins.study.math.", "plugins.study.en.",
        #      "plugins.play.game.", "plugins.play.movie.", "plugins.play.music."]
        # a = ["plugins/study/cn/", "plugins/study/math/", "plugins/study/en/", "plugins/play/game/"]
        a = ["plugins/study/cn/"]

        for i in a:
            filenames = listdir(i)
            print(i, filenames, 22222222222222)

        self.scrollArea.setParent(None)


    def addToGridLayout(self, layout, widget):
        count = layout.count()
        row = count // 4  # 行索引，其实就是整除的值
        column = count % 4  # 列索引，其实就是余数（remainder）
        layout.addWidget(widget, row, column)

    def showSkins(self):
        self.showSkinSignal.emit()

    def showCollect(self):
        pass

    def showShop(self):
        pass


    def setBackGround(self, filePath):
        if self.movie():
            self.movie().deleteLater()

        if filePath[-4:] == ".gif":

            movie = QMovie(filePath)
            movie.setParent(self)
            movie.setScaledSize(self.size())
            self.setMovie(movie)
            movie.start()
        else:
            self.setPixmap(QPixmap(filePath))

    def eventFilter(self, obj, e):
        """只有self.widTitle注册了遍历器，所以没有用obj对象"""
        if obj == self.widTitle:
            if e.type() == e.MouseButtonPress and e.button() == Qt.LeftButton:
                self.flagMove = True
                self.posMove = e.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
                e.accept()
            if e.type() == e.MouseMove and self.flagMove:
                self.move(e.globalPos() - self.posMove)  # 更改窗口位置
                e.accept()
            if e.type() == e.MouseButtonRelease:
                self.flagMove = False

        return False  # 必须有

    def center(self):
        # 得到主窗体的框架信息
        qr = self.frameGeometry()
        # 得到桌面的中心
        cp = QDesktopWidget().availableGeometry().center()
        # 框架的中心与桌面中心对齐
        qr.moveCenter(cp)
        # 自身窗体的左上角与框架的左上角对齐
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(argv)
    window = MainPane()
    window.show()
    exit(app.exec_())
