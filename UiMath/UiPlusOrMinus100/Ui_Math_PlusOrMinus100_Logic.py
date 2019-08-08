from random import choice
from re import match

from PyQt5.QtCore import Qt, pyqtSlot, QRectF
from PyQt5.QtGui import QBrush, QPixmap, QMovie, QIntValidator, QBitmap, QPainter, QCursor
from PyQt5.QtWidgets import QWidget, QDialog

from UiMain.Ui_DialogChoose_Logic import Ui_DialogChoose_Logic
from UiMath.UiPlusOrMinus100.Ui_Math_PlusOrMinus100 import Ui_Math_PlusOrMinus100
# time.strftime("%Y/%m/%d_%H:%M:%S")

class UiMath_PlusOrMinus100_Logic(QWidget, Ui_Math_PlusOrMinus100):
    def __init__(self, parent):
        super(UiMath_PlusOrMinus100_Logic, self).__init__(parent.widCenter)
        self.setupUi(self)
        self.p = parent

        # 加载自己封装的下拉菜单，并显示菜单按钮
        parent.btnMenu.show()
        self.ltData = []
        self.lt = ['10以内加减法', '20以内加减法', '50以内加减法', '100以内加减法']
        parent.loadMenuData(self.lt, self)

        self.movieNormal = QMovie("UiMath/UiPlusOrMinus100/image/6.gif")
        self.movieWin = QMovie("UiMath/UiPlusOrMinus100/image/7.gif")
        self.labMovie.setMovie(self.movieNormal)
        self.movieNormal.start()

        self.pixRight = QPixmap("UiMath/UiPlusOrMinus100/image/3.png")
        self.pixWrong = QPixmap("UiMath/UiPlusOrMinus100/image/4.png")
        self.pixSmile = QPixmap("UiMath/UiPlusOrMinus100/image/5.png")
        for widget in self.widget.children()[1:]:
            widget.children()[1:][0].setPixmap(self.pixSmile)
            widget.children()[-1].setValidator(QIntValidator(0, 100))

        self.labTime.timerEvent = self.labTime_timerEvent
        [btn.clicked.connect(self.slot_btn_startOrStop) for btn in [self.btnTimeStart, self.btnTimeStop]]
        self.getInputData(self.lt[0])

    def countScore(self):
        self.timeWidgetStatusChange()
        _list = self.widget.children()[1:]
        for widget in _list:
            numLeft = int(widget.children()[1:][1].text())
            symbol = widget.children()[1:][2].text()
            numRight = int(widget.children()[1:][3].text())
            result = eval(f"numLeft{symbol}numRight")
            widget.children()[1:][-1].setEnabled(False)
            userInput = widget.children()[1:][-1].text()
            if userInput != '' and int(userInput) == result:  # 判断用户输入的是否为数字
                widget.children()[1:][0].setPixmap(self.pixRight)
                self.labRight.setText(str(int(self.labRight.text())+1))
            else:
                widget.children()[1:][0].setPixmap(self.pixWrong)
                self.labWrong.setText(str(int(self.labWrong.text())+1))
        score = 100/9*int(self.labRight.text())
        self.labScore.setText(str(int(score)))
        if score == 100:
            self.labMovie.setMovie(self.movieWin)
            self.movieWin.start()
            self.movieNormal.stop()

    def getInputData(self, char):
        try:
            num = int(match(r"(^[0-9]+)", char).group(0))  # 正则匹配数字
            for index, widget in enumerate(self.widget.children()[1:]):
                a = choice(range(num + 1))
                b = choice(["+", "-"])
                if b == "+":
                    c = choice(range(num - a + 1))
                elif b == "-":
                    c = choice(range(a + 1))
                widget.children()[1:][0].setPixmap(self.pixSmile)
                widget.children()[1:][-1].setEnabled(True)
                widget.children()[1:][-1].clear()
                widget.children()[1:][1].setText(str(a))
                widget.children()[1:][2].setText(b)
                widget.children()[1:][3].setText(str(c))
            self.timeWidgetStatusChange(True)
        except Exception as e:
            print(e)

    def slot_btn_startOrStop(self):
        sender = self.sender()
        sender.setEnabled(False)
        if sender == self.btnTimeStart:
            self.btnTimeStop.setEnabled(True)
            self.flagLabTime = self.labTime.startTimer(1000)
        elif sender == self.btnTimeStop:
            self.btnTimeStart.setEnabled(True)
            self.labTime.killTimer(self.flagLabTime)
        self.sBoxTimeChange.setEnabled(self.btnTimeStart.isEnabled())

    @pyqtSlot()
    def on_btnCommit_clicked(self):
        replay = Ui_DialogChoose_Logic().setInfo(self.p, '提交作业', '小朋友，检查过了吗？\n要养成检查作业的好习惯哦！')
        if replay:
            self.countScore()

    @pyqtSlot(int)
    def on_spinBox_valueChanged(self, index):
        if index:
            seconde = index * 60
            self.labTime.setText(str(seconde))
            self.btnTimeStart.setEnabled(True)
        else:
            self.labTime.setText("0")
            self.btnTimeStart.setEnabled(False)
            self.btnTimeStop.setEnabled(False)

    def timeWidgetStatusChange(self, enalbled=False):
        self.sBoxTimeChange.setEnabled(enalbled)
        self.btnCommit.setEnabled(enalbled)
        self.btnTimeStart.setEnabled(False)
        self.btnTimeStop.setEnabled(False)
        if enalbled:  # 刷新题目时
            self.sBoxTimeChange.setValue(0)
            self.labRight.setText('0')
            self.labWrong.setText('0')
            self.labScore.setText('0')
            self.labMovie.setMovie(self.movieNormal)
            self.movieWin.stop()
        if hasattr(self, 'flagLabTime'):
            self.labTime.killTimer(self.flagLabTime)


    def labTime_timerEvent(self, e):
        num = int(self.labTime.text())
        if num <= 0:
            self.countScore()
        else:
            self.labTime.setText(str(num - 1))

