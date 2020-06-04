from os import listdir
from random import shuffle, choice

from PyQt5.QtCore import QRect, Qt, QPropertyAnimation, QEasingCurve, pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel

from UiGames.UIPuzzle.Ui_Puzzle import Ui_Puzzle
from UiMain.Ui_DialogChoose_Logic import Ui_DialogChoose_Logic


class UiGames_Puzzle_Logic(QWidget, Ui_Puzzle):
    def __init__(self, parent):
        super(UiGames_Puzzle_Logic, self).__init__(parent.widCenter)
        self.p = parent
        self.setupUi(self)
        self.installEventFilter(self)

        self.dictPos = dict()
        self.loadPix(True)
        self.flagMove = False
        self.flagPaint = False

        self.btnAnimat.clicked.connect(self.frameAnimat.hide)
        self.btnUpdataPix.clicked.connect(self.loadPix)  # 加载拼图

    def loadPix(self, savePos=False):
        self.btnFinish.hide()
        image = choice(listdir('game/UiPuzzle/images/bg'))  # 随机选择指定目录中的一张拼图
        bgImage = choice(listdir('game/UiPuzzle/images/bg2'))  # 随机选择指定目录中的一张背景图(拼图区)

        pix = QPixmap(f'game/UiPuzzle/images/bg/{images}').scaled(400, 400)  # 把图片缩放为400*400,如果有水印,还需要PS处理
        self.btnAnimat.setStyleSheet(f"border-images: url('game/UiPuzzle/images/bg/{images}');")
        self.frameBg.setStyleSheet(f"border-images: url('game/UiPuzzle/images/bg2/{bgImage}');")
        lt = [(0, 0, 0), (100, 0, 1), (200, 0, 2), (300, 0, 3),  # 固定的400*400px的图片，分割成16份
              (0, 100, 4), (100, 100, 5), (200, 100, 6), (300, 100, 7),
              (0, 200, 8), (100, 200, 9), (200, 200, 10), (300, 200, 11),
              (0, 300, 12), (100, 300, 13), (200, 300, 14), (300, 300, 15)]
        shuffle(lt)  # 打乱16个坐标顺序
        index = 0
        for w in self.children():
            if isinstance(w, QLabel):
                pixCopy = pix.copy(QRect(*lt[index][:-1], 100, 100))  # 复制选区内的图片
                w.setPixmap(pixCopy)
                w.setObjectName(f'lab{lt[index][-1]}')
                index += 1
                if savePos:  # 只有在刚打开拼图游戏时储存lab位置在字典中
                    self.dictPos[w.objectName()] = w.pos()
                if savePos is False and w.pos() != self.dictPos[w.objectName()]:  # 刷新界面时，让lab回到初始位置
                    w.move(self.dictPos[w.objectName()])
        self.startAnimat()

        if not savePos:  # 这个条件也可以不用,直接设置text。
            self.labCount.setText("0")  # 计操作步数(只有换位置的时候),16次为最佳(16张图)

    @pyqtSlot()
    def on_btnPix_clicked(self):
        replay = Ui_DialogChoose_Logic().setInfo(self.p, '查看原图', '你确定要花费10金币查看原图吗？')
        if replay and self.p.updateGoldAndJewel('金币', 10, 'Minus'):
            self.startAnimat()

    def startAnimat(self):
        self.frameAnimat.show()  # 因为frameAnimat显示6秒后会隐藏，所以每次执行动画时要显示它
        self.frameAnimat.raise_()
        propertyName, duration, startValue, endValue = 'geometry', 6000, (770, 304, 0, 0), (570, 104, 408, 408)
        animation = QPropertyAnimation(self.frameAnimat, propertyName.encode('ascii'), self)
        animation.setDuration(duration)
        animation.setStartValue(QRect(*startValue))
        animation.setKeyValueAt(0.2, QRect(*endValue))
        animation.setKeyValueAt(0.9, QRect(*endValue))
        animation.setEndValue(QRect(*startValue))
        animation.start(animation.DeleteWhenStopped)  # 动画结束后进行自清理
        animation.finished.connect(self.frameAnimat.hide)

    def paintEvent(self, e):
        if self.flagPaint:
            count = 0  # 每次绘制事件标记打开都设置计数为0，相当于每次都判断16次（16个拼图）位置是否正确
            for w in self.children():
                if type(w) is QWidget and w is not self.horizontalLayoutWidget:  # 先找到拼图区的QWidget
                    # 再判断此QWidget的pos如果是QLabel类型，说明已经放了拼图，如果不是说明还是空的（不处理）。再判断此位
                    # 置的lab对象名的-1项是否等于此位置的widget对象名的-1项，如果是说明位置正确，如果不是，说明位置错
                    # 误（不处理）
                    if isinstance(self.childAt(w.pos()), QLabel) and self.childAt(w.pos()).objectName()[-1] == \
                            w.objectName()[-1]:
                        count += 1  # 位置正确，计数加1
            if count == 16:  # 再判断位置正确的计数是否等于16，如果等于就说明完成了拼图。
                self.p.updateGoldAndJewel('金币', 20, 'Plus')
                self.btnFinish.show()
                self.btnFinish.raise_()
                animation = QPropertyAnimation(self.btnFinish, b'geometry', self)
                animation.setDuration(2000)  # 持续时间
                animation.setEasingCurve(QEasingCurve.OutBounce)
                animation.setStartValue(QRect(490, 260, 0, 0))
                animation.setEndValue(QRect(240, 110, 500, 300))
                animation.start(animation.DeleteWhenStopped)

            self.flagPaint = False

    def eventFilter(self, obj, e):
        if self.frameAnimat.isVisible() or self.btnFinish.isVisible():
            return False
        if e.type() == e.MouseButtonPress and e.button() == Qt.LeftButton:
            self.widgetLab = self.childAt(e.pos())
            if isinstance(self.widgetLab, QLabel):
                self.flagMove = True
                self.widgetLab.raise_()  # 提升选中的lab为顶层
                self.flagPos = self.widgetLab.pos()  # 标记选中lab的“当前”位置
                self.mPos = e.localPos().toPoint() - self.widgetLab.pos()  # 获取鼠标相对程序窗口的位置
                e.accept()
        if e.type() == e.MouseMove and self.flagMove:
            self.widgetLab.move(e.localPos().toPoint() - self.mPos)  # 选中lab移动位置(lab相对鼠标的位置)
            e.accept()
        if e.type() == e.MouseButtonRelease and e.button() == Qt.LeftButton and self.flagMove:
            self.widgetLab.hide()  # 鼠标释放时，用的小办法，先隐藏选中的lab,不然self.childAt(e.pos())会是选中的lab
            # 如果鼠标释放后(选中的lab已经提前隐藏)的位置是布局的16个QWidget其中一个,并且“当前”不等于下面的QWidget的位置
            # if isinstance(self.childAt(e.pos()), QWidget) and self.flagPos != self.childAt(e.pos()).pos():
            # 这里不用isinstance方法判断类型是因为，QLabel的基类是QWidget，而type方法不会查询到基类
            if type(self.childAt(e.pos())) is QWidget and self.flagPos != self.childAt(e.pos()).pos():
                self.widgetLab.move(self.childAt(e.pos()).pos())  # 选中的lab移动到鼠标下面的QWidget的位置
                self.labCount.setText(str(int(self.labCount.text()) + 1))  # 计操作步数(只有换位置的时候),16次为最佳(16张图)
                self.flagPaint = True  # 只有把lab放在拼图区时，才打开绘制事件中的判断条件（判断是否完成拼图）
            else:  # 如果不是布局的16个QWidget其中一个
                self.widgetLab.move(self.flagPos)  # 选中的lab移动到“当前”位置
            self.flagMove = False
            self.widgetLab.show()  # 已经得到选中lab下面的控件，再把它显示出来
        if e.type() == e.MouseButtonRelease and e.button() == Qt.RightButton:
            widgetTempLab = self.childAt(e.pos())  # 如果是右键释放，要处理鼠标位置下的lab不在初始位置时，再回到初始位置
            if isinstance(widgetTempLab, QLabel) and widgetTempLab.pos() != self.dictPos[widgetTempLab.objectName()]:
                widgetTempLab.move(self.dictPos[widgetTempLab.objectName()])
        return False
