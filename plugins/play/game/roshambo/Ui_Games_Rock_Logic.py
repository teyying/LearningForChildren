from random import choice

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie, QPalette
from PyQt5.QtWidgets import QWidget

from UiGames.UiRock.Ui_Games_Rock import Ui_Games_Rock


class UiGames_Rock_Logic(QWidget, Ui_Games_Rock):
    def __init__(self, parent):
        super(UiGames_Rock_Logic, self).__init__(parent.widCenter)
        self.setupUi(self)

        # 设置一个gif图片
        self.movie = QMovie("game/roshambo/images/5.gif")
        self.labMovie.setMovie(self.movie)
        self.movie.start()

        # 把石头剪刀布QLabel和QPushButton放进列表内，以便按钮槽函数内进行操作
        self.ltLabAndBtn = self.widLab.children()[1:] + self.widBtn.children()[1:]
        [btn.clicked.connect(self.slot_btns) for btn in self.ltLabAndBtn if btn.objectName()[:3] == 'btn']
        self.btnPk.clicked.connect(self.slot_btns)

        # 为了当前计数变动时字体颜色改变为红色，其它还原为黑
        self.paRed = QPalette()
        self.paBlack = QPalette()
        self.paRed.setColor(QPalette.WindowText, Qt.red)
        self.paBlack.setColor(QPalette.WindowText, Qt.black)

        self.btnPk.hide()
        self.flagBtn = None

    def slot_btns(self):
        """石头剪刀布游戏里的按钮槽函数(不包括继承过来的原主窗口按钮)"""
        sender = self.sender()
        if sender == self.btnPk:
            self.btnPk.hide()
            [i.show() for i in self.ltLabAndBtn]
            self.flagBtn.setEnabled(True)
        else:
            robotShow = choice([lab for lab in self.ltLabAndBtn if lab.objectName()[:3] == 'lab'])
            sender.setEnabled(False)
            self.flagBtn = sender
            [i.hide() for i in self.ltLabAndBtn if i != robotShow and i != sender]
            self.btnPk.show()

            if sender.objectName()[3:] == robotShow.objectName()[3:]:
                self.flagLab = self.labDraw
            elif sender == self.btnRock and robotShow == self.labScissor or \
                    sender == self.btnScissor and robotShow == self.labPaper or \
                    sender == self.btnPaper and robotShow == self.labRock:
                self.flagLab = self.labWin
            else:
                self.flagLab = self.labLose

            for lab in [self.labWin, self.labLose, self.labDraw]:
                if lab == self.flagLab:
                    lab.setText(str(int(lab.text()) + 1))
                    lab.setPalette(self.paRed)
                else:
                    lab.setPalette(self.paBlack)
