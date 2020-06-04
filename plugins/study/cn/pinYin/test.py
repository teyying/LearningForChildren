import cgitb
from sys import argv
from PyQt5.Qt import *
from PyQt5.QtCore import pyqtSlot, Qt

from UiCn.UiPinYin.UI_Form import Ui_Form
cgitb.enable(format='text')  # 解决pyqt5异常只要进入事件循环,程序就崩溃,而没有任何提示

"""
*VAR* 可以定义一个变量
*ARRAY* 可输入一个数组
*PARAM* 可变长度参数
*END* 光标结束符号
用的时候，把*号换成美元符号。
"""


class TestUi(QWidget, Ui_Form):
    def __init__(self):
        super(TestUi, self).__init__()
        self.setupUi(self)
        t = 't tɑ te tɑi tɑo tou tɑn tɑng teng ti tie tiɑo tiɑn ting tong tu tuɑn tun tui tuo'
        n = 'n nɑ nɑi nei nɑo ne nen nɑn nɑng neng ni nie niɑo niu niɑn nin niɑng ning nong nou nu nuɑn nun nuo nü nüe'
        l = 'l lɑ le lɑi lei lɑo lou lɑn lɑng len leng li liɑ lie liɑo liu liɑn lin liɑng ling long lu luo lou luɑn lun lü lüe'
        g = 'g gɑ ge gɑi gei gɑo gou gɑn gen gɑng geng gong gu guɑ guɑi guɑn guɑng gui guo'
        k = 'k kɑ ke kɑi kɑo kou kɑn ken kɑng keng kong ku kuɑ kuɑi kuɑn kuɑng kui kun kuo'
        h = 'h hɑ he hɑi hɑn hei hɑo hou hen hɑng heng hong hu huɑ huɑi huɑn hui huo hun huɑng'
        # self.getInputData(t)
        # self.pTEditUp.setPlainText(a)
        # self.pTEditUp.setMaximumBlockCount(1)
        self.pTEditUp.setLineWrapMode(QPlainTextEdit.NoWrap)
        # self.pTEditDn.setPlainText(a)
        self.pTEditDn.setLineWrapMode(QPlainTextEdit.NoWrap)

        # scrollbar.setSliderPosition(scrollbar.minimum())
        self.setFocus()

    def on_pTEditDn_textChanged(self):
        print(111)
        # hi_selection = QTextEdit.ExtraSelection()
        # hi_selection.format.setBackground(QColor(Qt.yellow).lighter(160))
        # hi_selection.format.setProperty(QTextFormat.FullWidthSelection, True)
        # hi_selection.cursor = self.pTEditDn.textCursor()
        # hi_selection.cursor.clearSelection()
        # self.setExtraSelections([hi_selection])

        # def on_pTEditDn_selectionChanged(self):
    #     print(222)
    #     hi_selection.format.setBackground(lineColor)
    @pyqtSlot()
    def on_btn_clicked(self):
        self.c = self.pTEditDn.textCursor()
        print(self.c.selectedText())

        hi_selection = QTextEdit.ExtraSelection()
        hi_selection.format.setBackground(QColor(Qt.yellow).lighter(160))
        hi_selection.format.setProperty(QTextFormat.FullWidthSelection, True)
        hi_selection.cursor = self.pTEditDn.textCursor()
        hi_selection.cursor.clearSelection()
        # self.setExtraSelections([hi_selection])

    def getInputData(self, char):
        self.allChar = char
        listStr = char.split(' ')
        new = ''
        pixel = 0
        self.listText = []
        for i, j in enumerate(listStr):
            count = len(j) * 27
            if new == '':
                new += j
            elif 27 + pixel + count <= 860:  # 894
                new += ' ' + j
                pixel += 27 + count
            else:
                self.listText.append(new)
                new = j
                pixel = 0
            if i == len(listStr) - 1 and new != '':
                self.listText.append(new)
        self.lenListText = len(self.listText)
        self.pTEditUp.setPlainText(self.listText[0])

if __name__ == '__main__':
    app = QApplication(argv)
    window = TestUi()  # 实例化主窗口
    window.show()
    exit(app.exec_())
