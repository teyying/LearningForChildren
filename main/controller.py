# -*- coding: utf-8 -*-

"""
-------------------------------------
Created on 2020/4/25 16:45
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

from main.mainPane import MainPane
from main.skinPane import SkinPane

cgitb.enable(format='text')


class Controller(QObject):
    def __init__(self):
        super(Controller, self).__init__()
        self.mainPane = MainPane()
        self.mainPane.showSkinSignal.connect(self.fn)
        self.mainPane.loadButtons.emit()

    def fn(self):
        self.skinPane = SkinPane()
        self.skinPane.imagePathSignal[str].connect(self.mainPane.setBackGround)
        point = self.mainPane.pushButton_3.mapTo(self.mainPane, self.mainPane.pos())
        self.skinPane.move(QPoint(point.x(), point.y()+self.mainPane.pushButton_3.height()))
        self.skinPane.show()

    def fn2(self):
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

        # for i in a:
        #     filenames = listdir(i)
        #     print(i, filenames)

if __name__ == '__main__':
    app = QApplication(argv)
    controller = Controller()
    controller.mainPane.show()
    exit(app.exec_())