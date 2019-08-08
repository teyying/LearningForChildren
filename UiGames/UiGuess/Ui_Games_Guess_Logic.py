from random import choice

from PyQt5.QtWidgets import QWidget

from UiGames.UiGuess.Ui_Games_Guess import Ui_Games_Guess


class UiGames_Guess_Logic(QWidget, Ui_Games_Guess):
    def __init__(self, parent):
        super(UiGames_Guess_Logic, self).__init__(parent.widCenter)
        self.setupUi(self)

        self.labGuess.hide()
        self.labGuessRight.hide()
        self.widInput.hide()

        [btn.clicked.connect(self.slot_btns) for btn in self.widInput.children()[1:]]
        self.btnGuess.clicked.connect(self.slot_btns)

        self.flagOk = False  # 设置一个标志，用来处理再输入数字直接设置，不用再点删除按钮了

    def slot_btns(self):
        text = self.sender().text()
        displayText = self.labDisplayNum.text()
        self.labBig.hide()
        self.labSmall.hide()
        if text == '猜':
            self.widInput.show()
            self.labGuess.show()
            self.btnGuess.hide()

            self.labBig.hide()
            self.labSmall.hide()
            self.labGuessRight.hide()

            self.labDisplayNum.setText('??')
            self.labCountPrevious.setText(self.labCountPresently.text())
            self.labCountPresently.setText('0')

            self.secretNum = choice(range(101))
        elif text == 'backspace':
            self.labDisplayNum.setText('??')
        elif text == 'ok':
            self.flagOk = True  # 设置一个标志，用来处理再输入数字直接设置，不用再点删除按钮了
            displayInt = int(displayText)
            self.labCountPresently.setText(str(int(self.labCountPresently.text())+1))
            if displayInt == self.secretNum:
                self.widInput.hide()
                self.labBig.hide()
                self.labSmall.hide()
                self.labGuess.hide()
                self.btnGuess.show()
                self.labGuessRight.show()
            elif displayInt < self.secretNum:
                self.labSmall.show()
                self.labBig.hide()
            else:
                self.labSmall.hide()
                self.labBig.show()
        elif displayText == '??' or self.flagOk is True:  # 如果游戏刷新或者点过一次ok按钮，再输入数字直接设置，不用再点删除按钮了
            self.labDisplayNum.setText(text)
            self.flagOk = False
        elif displayText != '??' and len(displayText) == 2 or displayText == '0':  # 不让超过两位数以及不让出现0几的现象
            return
        else:
            self.labDisplayNum.setText(displayText + text)
