# -*- coding: utf-8 -*-

"""
-------------------------------------
Created on 2020/4/24 17:16
@author: Teyying
@site: https://github.com/teyying
@email: 165227316@qq.com
-------------------------------------
@file: skinPane.py
@description:
@problem:
-------------------------------------

"""
from os import listdir
from os.path import splitext, exists, split as os_split
from shutil import copyfile
from sys import argv, exit
from PyQt5.Qt import *
from main.resource.skinUi import Ui_Skin

import cgitb

cgitb.enable(format='text')


class SkinPane(QWidget, Ui_Skin):
    imagePathSignal = pyqtSignal(str)

    def __init__(self):
        super(SkinPane, self).__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowFlag(Qt.Popup)  # 设置为子窗口(非模态弹窗)
        self.gridTab1.setAlignment(Qt.AlignTop)
        self.gridTab2.setAlignment(Qt.AlignTop)

        self.btnAddSkin = QPushButton()
        self.btnAddGifSkin = QPushButton()
        self.btnAddSkin.setProperty('function', 'add')
        self.btnAddGifSkin.setProperty('function', 'add')
        self.btnAddSkin.setFixedSize(50, 50)
        self.btnAddGifSkin.setFixedSize(50, 50)
        self.btnAddSkin.setCursor(Qt.PointingHandCursor)
        self.btnAddGifSkin.setCursor(Qt.PointingHandCursor)
        self.btnAddSkin.setIcon(QIcon(":/main/images/icon_addSkin.png"))
        self.btnAddGifSkin.setIcon(QIcon(":/main/images/icon_addSkin.png"))
        self.btnAddSkin.setIconSize(QSize(25, 25))
        self.btnAddGifSkin.setIconSize(QSize(25, 25))
        self.btnAddSkin.clicked.connect(self.slot_btnAddSkin)
        self.btnAddGifSkin.clicked.connect(self.slot_btnAddSkin)

        self.setStyleSheet("QWidget#Skin QPushButton:hover {border:2px solid red;}"
                           "QWidget#Skin QPushButton[function='add']:hover {border:2px solid lightblue;}")
        self.path = 'main/resource/images/skin' if exists('main/resource/images/skin') else 'resource/images/skin'
        self.filenames = listdir(self.path)
        self.count = len(self.filenames) - 1
        self.timer = self.startTimer(1, Qt.CoarseTimer)

    def addToGridLayout(self, layout, widget):
        count = layout.count()
        row = count // 4  # 行索引，其实就是整除的值
        column = count % 4  # 列索引，其实就是余数（remainder）
        layout.addWidget(widget, row, column)

    def timerEvent(self, e):
        """加载换肤的按钮和图片"""
        filename = self.filenames[self.count]
        extension = splitext(filename)[1]  # 得到图片扩展名

        btn = QPushButton()
        btn.setFixedSize(50, 50)
        btn.setCursor(Qt.PointingHandCursor)

        imagePath = f"{self.path}/{filename}"
        btn.clicked.connect(lambda: self.imagePathSignal.emit(imagePath))

        lab = QLabel(btn)
        lab.setFixedSize(QSize(btn.height()-4, btn.width()-4))
        lab.move(2, 2)
        lab.setScaledContents(True)

        if extension == '.gif':
            movie = QMovie(imagePath, parent=lab)
            lab.setMovie(movie)
            movie.start()
            self.addToGridLayout(self.gridTab2, btn)
        else:
            lab.setPixmap(QPixmap(imagePath))
            self.addToGridLayout(self.gridTab1, btn)

        self.count -= 1

        if self.count == -1:
            self.addToGridLayout(self.gridTab1, self.btnAddSkin)
            self.addToGridLayout(self.gridTab2, self.btnAddGifSkin)
            self.killTimer(self.timer)

    def slot_btnAddSkin(self):
        """添加皮肤功能"""
        self.flagAdd = True
        self.filenames = []  # 重新保存新的文件名列表给计时器用，为了实时的把添加的图片显示出来
        file_path_list, _ = QFileDialog.getOpenFileNames(self.parentWidget(), "选取文件", "C:",
                                                         "所有图片格式(*.jpg;*.png;*.gif)")
        for file_path in file_path_list:
            extension = splitext(os_split(file_path)[1])[1]  # 得到图片文件扩展名
            flag = 1
            while True:
                savePath = f"{self.path}/{flag}{extension}"
                isExist = exists(savePath)  # 判断是否存在相同的文件名
                if isExist:
                    flag += 1
                else:
                    self.filenames.append(f"{flag}{extension}")
                    copyfile(file_path, savePath)  # 复制原图片路径到指定路径
                    break

        if file_path_list:  # 实时的把添加的图片显示出来
            self.btnAddSkin.setParent(None)
            self.btnAddGifSkin.setParent(None)
            self.count = len(self.filenames) - 1
            self.timer = self.startTimer(1, Qt.CoarseTimer)
        self.show()

    def showEvent(self, e):
        self.flagAdd = False  # 处理添加完图片后，再把界面显示出来，原本关闭后self.deleteLater()了
        return super().showEvent(e)

    def closeEvent(self, e):
        if not self.flagAdd:
            self.deleteLater()
        else:
            return super().closeEvent(e)


if __name__ == '__main__':
    app = QApplication(argv)
    window = SkinPane()
    window.show()
    exit(app.exec_())
