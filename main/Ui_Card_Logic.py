from functools import partial

from PyQt5.QtCore import Qt, QRectF, QSize, QEvent
from PyQt5.QtGui import QBitmap, QPainter, QBrush, QCursor
from PyQt5.QtWidgets import QDialog, QPushButton, QWidget, QLabel, QHBoxLayout, QScrollArea, QFrame

from UiMain.Ui_Card import Ui_Card


class Ui_Card_Logic(QDialog, Ui_Card):
    def __init__(self, parent=None):
        super(Ui_Card_Logic, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏标题栏
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.flagMove = False
        self.widTitle.installEventFilter(self)

        # 用遮罩的方法给窗体设置圆角
        self.whiteMask = QBitmap(self.size())  # 创建位图，窗体大小
        self.whiteMask.fill(Qt.white)  # 填充位图全白，相当于把窗口擦掉了，后面再用画刷显示出来。
        p = QPainter(self.whiteMask)
        brush = QBrush(Qt.black)  # 创建画刷并设置成黑色，这样黑色区域内的窗口就显示出来了。
        p.setBrush(brush)  # 设置画刷
        rectF = QRectF(0.0, 0.0, 884, 680)  # 画一个矩形
        p.drawRoundedRect(rectF, 8.0, 8.0)  # 给矩形添加圆角
        self.setMask(self.whiteMask)  # 设置遮罩

        # self.uiCardFullScreen = Ui_CardFullScreen_Logic()
        # self.widFullScreen.installEventFilter(self)

        self.setBtns()

    def setBtns(self):
        # 速度：77字 / 分，正确率：95 %，级别：  七级
        # 19
        try:
            num = 100
            if num > 1052:
                num = 1052
            self.labTitle.setText(str(num))
            row = 0
            column = 0
            for i in range(num):
                btn = QPushButton()
                btn.setFixedSize(210, 300)
                btn.setCursor(QCursor(Qt.PointingHandCursor))
                self.gridLayout.addWidget(btn, row, column)
                column += 1
                if column == 4:
                    row += 1
                    column = 0

            self.btns = self.scrollAreaWid.children()[1:]  # 列表第一个是QGrdLayout
            self.numBtns = len(self.btns)  # 图片文件共有1052张图，如果超过就会崩溃。暂不解决这个问题。
            self.index = 0
            self.timer = self.startTimer(10)

        except Exception as e:
            print(e)

    def slot_btns(self, styleStr):
        self.uiCardFullScreen = Ui_CardFullScreen(styleStr)
        self.uiCardFullScreen.exec()

    def timerEvent(self, e):
        """每10毫秒添加一张图片，这样图片多了之后启动窗口就不会出现无响应状态"""
        try:
            self.btns[self.index].setStyleSheet(f"border-images: url('UiMain/images/card/{self.index}.png')")
            self.btns[self.index].clicked.connect(partial(self.slot_btns, self.btns[self.index].styleSheet()))

            if self.index == self.numBtns - 1:
                self.killTimer(self.timer)
            self.index += 1
        except Exception as e:
            print(e)

    def eventFilter(self, obj, e):
        """只有self.widTitle注册了遍历器，所以没有用obj对象"""
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


class Ui_CardFullScreen(QDialog):
    def __init__(self, styleStr):
        super(Ui_CardFullScreen, self).__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 隐藏标题栏，并让窗体一直在顶层
        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体透明
        self.setWindowOpacity(1)  # 设置为1，控件不透明

        hbox = QHBoxLayout(self)
        hbox.setContentsMargins(0, 0, 0, 0)  # 调整边距
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setStyleSheet('background:rgba(0,0,0,120)')
        self.scrollArea.setFrameShape(QFrame.NoFrame)  # 去掉边框
        self.scrollArea.setWidgetResizable(True)  # 这一句很重要。意思应该是让内部的widget随它的尺寸
        self.widPix = QWidget()
        self.widPix.setMouseTracking(True)  # 设置鼠标跟踪后会实时跟踪，不然只有在点击的时候才跟踪。
        self.widPix.installEventFilter(self)
        hbox2 = QHBoxLayout(self.widPix)
        hbox2.setContentsMargins(0, 0, 0, 0)
        self.labPix = QLabel(self.widPix)
        self.labPix.setStyleSheet(styleStr + ';background:transparent;')
        self.labPix.setFixedSize(210, 300)
        hbox2.addWidget(self.labPix)
        self.scrollArea.setWidget(self.widPix)
        hbox.addWidget(self.scrollArea)
        self.labClose = QLabel('×', self.widPix)  # 为了让字体靠右靠上，只能把btn改成lab，
        self.labClose.setFixedSize(60, 60)  # 不然只能qss设置水平方向text-align:right;找不到垂直靠上的方法。
        self.labClose.setAlignment(Qt.AlignRight | Qt.AlignTop)
        self.labClose.setCursor(QCursor(Qt.PointingHandCursor))
        self.labClose.setStyleSheet(
            'QLabel {font-size:50px;color:white;border-bottom-left-radius:60px 60px;}:hover{background:red;}')
        self.labClose.hide()
        self.labPercent = QLabel("100%", self.widPix)
        self.labPercent.installEventFilter(self)
        self.labPercent.setStyleSheet('background:rgba(255,255,255,120);font-size:30px;border-radius:5px;')
        self.labPercent.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.labPercent.setFixedSize(80, 40)
        self.labPercent.hide()

    def showEvent(self, e):  # 这也可以写进事件遍历器里面
        self.showFullScreen()
        self.scrollArea.setFixedSize(self.size())  # 这个尺寸只有在显示满屏后才能得到此Ui的尺寸
        self.labClose.move(self.width() - self.labClose.width(), 0)  # 固定在右上角
        self.labPercent.move(self.width() / 2 - self.labPercent.width() / 2,
                             self.height() / 2 - self.labPercent.height() / 2)

    def eventFilter(self, obj, e):
        if obj == self.widPix:
            if e.type() == e.MouseMove:  # 设置鼠标在屏幕四周60px内显示关闭按钮，离开60px范围藏关闭按钮
                if self.labClose.isHidden():
                    if e.globalX() == 0 or e.globalY() == 0 or e.globalX() >= self.width() - 1 or e.globalY() >= self.height() - 1:
                        self.labClose.show()
                elif self.labClose.isVisible():
                    if self.width() - 60 > e.globalX() >= 60 and self.height() - 60 > e.globalY() >= 60:
                        self.labClose.hide()
            elif e.type() == e.MouseButtonPress and e.button() == Qt.LeftButton:  # self.labClose不用childAt，设置鼠标跟踪应该也行
                if self.childAt(e.globalPos()) == self.widPix or self.childAt(e.globalPos()) == self.labClose:
                    self.close()
            elif e.type() == e.MouseButtonDblClick and e.button() == Qt.LeftButton:
                if self.childAt(e.globalPos()) == self.labPix:  # 判断双击位置是否是self.labPix
                    self.labPix.setFixedSize(210, 300)
                    self.num = 100
                    self.labPercent.setText('100%')
            elif e.type() == e.Wheel:  # e.angleDelta().y()大于0说明向上滚动，反之
                self.labPercent.show()
                num = int(self.labPercent.text()[:-1])
                if e.angleDelta().y() > 0 and num != 500:  # 上滚是QPoint(0, 120)，下滚是QPoint(0, -120)
                    symbol = '+'
                elif e.angleDelta().y() < 0 and num != 0:
                    symbol = '-'
                else:
                    return False
                self.labPix.setFixedSize(eval(f"self.labPix.width(){symbol}21"),
                                         eval(f"self.labPix.height(){symbol}30"))
                self.labPercent.setText(eval(f"str(num{symbol}10)+'%'"))
            return False
        if obj == self.labPercent:
            if e.type() == e.Show:
                self.timerId = self.labPercent.startTimer(1000, Qt.VeryCoarseTimer)
            elif e.type() == e.Timer:
                self.labPercent.killTimer(self.timerId)
                self.labPercent.hide()
            return False

        else:
            return False
