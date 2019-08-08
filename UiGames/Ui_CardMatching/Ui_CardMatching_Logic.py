from os import listdir
from random import shuffle

from PyQt5.QtCore import QPointF, Qt, QTimeLine, QPropertyAnimation, QEasingCurve, QRect
from PyQt5.QtGui import QPainter, QTransform, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel

from UiGames.Ui_CardMatching.Ui_CardMatching import Ui_CardMatching


class UiGames_CardMatching_Logic(QWidget, Ui_CardMatching):
    def __init__(self, parent):
        super(UiGames_CardMatching_Logic, self).__init__(parent.widCenter)
        self.setupUi(self)
        self.p = parent

        self.btnFinish = QPushButton('游戏完成', self)
        self.btnFinish.setStyleSheet(
            "border-image: url('UiGames/Ui_CardMatching/image/3.png');border-radius:5px;font-size:100px;color:cyan;")
        self.btnFinish.clicked.connect(lambda: self.updateCard(20))
        self.updateCard(20)

    def updateCard(self, num):
        """游戏开始和游戏完成点击按钮更新卡牌的方法。num参数是为之后改进游戏提前设置的"""

        def addToGrid(btn):
            count = len(self.widMatching.children()[1:])
            row = count // 10  # 行索引，其实就是整除的值
            column = count % 10  # 列索引，其实就是余数（remainder）
            self.gridLayout.addWidget(btn, row, column)

        [_b.deleteLater() for _b in self.widMatching.children()[1:]]
        self.flagBtnOld = None  # 之前点击的按钮标记
        self.flagBtnNew = None  # 当前点击的按钮标记
        self.btnFinish.hide()
        self.labCount.setText(str(num))
        listImgNames = listdir("UiGames/Ui_CardMatching/image/奥特曼")
        shuffle(listImgNames)  # 打乱顺序后，下面for循环中取前num个(为有更多图片素材提前做的设置)
        listBtns = []
        for i in range(num):  # 卡牌背面1.png也可以设置随机选择，暂时先不设置了。
            btn = MyBtn(self, '1.png', listImgNames[i])
            btn2 = MyBtn(self, '1.png', listImgNames[i])
            btn.clicked.connect(self.slot_btns)
            btn2.clicked.connect(self.slot_btns)
            listBtns.append(btn)
            listBtns.append(btn2)
        shuffle(listBtns)  # 打乱图片顺序。注释掉后，相邻两个就是一对。
        [addToGrid(btn) for btn in listBtns]

    def slot_btns(self):
        # 交换数据，当前信号源为flagBtnNew，之前的信号源为flagBtnOld
        self.flagBtnNew, self.flagBtnOld = self.sender(), self.flagBtnNew
        if self.flagBtnOld == self.flagBtnNew:  # 处理已经翻开的卡片点击第二次，直接返回。
            return
        self.flagBtnNew.timeLine_start(0, 180)  # 翻开当前点击的卡片
        if self.flagBtnOld:  # 处理第一次执行程序时点击任何btn时，self.flagBtnOld=None。
            if self.flagBtnNew.pixPathFace == self.flagBtnOld.pixPathFace:
                self.flagBtnNew.deleteLater()
                self.flagBtnOld.deleteLater()
                self.flagBtnOld = None  # 之前点击的按钮标记
                self.flagBtnNew = None  # 当前点击的按钮标记
                num = int(self.labCount.text()) - 1
                self.labCount.setText(str(num))
                if num == 0:
                    self.p.updateGoldAndJewel('金币', 20, 'Plus')
                    self.btnFinish.show()
                    animation = QPropertyAnimation(self.btnFinish, b'geometry', self)
                    animation.setDuration(2000)  # 持续时间
                    animation.setEasingCurve(QEasingCurve.OutBounce)
                    animation.setStartValue(QRect(490, 260, 0, 0))
                    animation.setEndValue(QRect(240, 110, 500, 300))
                    animation.start(animation.DeleteWhenStopped)
            else:
                self.flagBtnOld.timeLine_start(180, 0)


class MyBtn(QPushButton):
    """
    自己封装的QPushButton, 需要继承一个parent对像， 并传一个背景图片路径pixPathBg和正面图片路径pixPathFace。
    父对你parent只需根据条件传参(翻转度数范围)执行此QPushButton的timeLine_start方法，就会自动进行翻转动作。
    """

    def __init__(self, parent, pixPathBg, pixPathFace):
        super(MyBtn, self).__init__(parent)
        self.setFixedSize(80, 100)
        self.setFlat(True)  # 扁平化风格，相当于前景透明，没有默认的点击效果
        self.rotateDegrees = 0  # 在timeLine_frameChanged方法里动态标记翻转度数
        self.pixPathFace = pixPathFace
        self.pixBg = QPixmap(f"UiGames/Ui_CardMatching/image/{pixPathBg}").scaled(self.size())
        # 创建一个翻转180度的QPixmap(卡片正面)，如果不提前翻转，lab_paintEvent绘制事件的翻转动作结束后，图片会左右变反
        self.pixFace = QPixmap(f"UiGames/Ui_CardMatching/image/奥特曼/{pixPathFace}").scaled(self.size()).transformed(
            QTransform().rotate(180, Qt.YAxis))

        self.lab = QLabel(self)
        self.lab.setFixedSize(self.size())
        self.lab.paintEvent = self.lab_paintEvent

        self.timeLine = QTimeLine(1000, self)
        self.timeLine.setUpdateInterval(25)  # 更新频率（也就是frameChanged(int)的执行速度），每25ms更新一次，相当于每秒40帧，
        self.timeLine.frameChanged.connect(self.timeLine_frameChanged)  # frameChanged()值改变连接的槽函数

    def timeLine_start(self, startValue, endValue):
        self.timeLine.setFrameRange(startValue, endValue)  # frameChanged()发出的值在startValue - endValue之间
        self.timeLine.start()

    def timeLine_frameChanged(self, frame):
        self.rotateDegrees = frame
        self.update()  # 每次frame值改变就更新一下lab的绘制事件, self.lab.update()也可以

    def lab_paintEvent(self, e):
        painter = QPainter(self.lab)
        painter.setRenderHint(QPainter.Antialiasing, True)  # 反走样
        painter.setTransform(QTransform().translate(self.width() / 2, self.height() / 2).rotate
                             (self.rotateDegrees, Qt.YAxis).translate(-self.width() / 2, -self.width() / 2))
        if self.rotateDegrees >= 90:  # 大于等于90度设置卡片正面.-(height-width)/2,这样才能把非正方形的图片放在正确的位置
            painter.drawPixmap(QPointF(0, -(self.height() - self.width()) / 2), self.pixFace)
        else:  # 小于90度设置卡片背面
            painter.drawPixmap(QPointF(0, -(self.height() - self.width()) / 2), self.pixBg)
