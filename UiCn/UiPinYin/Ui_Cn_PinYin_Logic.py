from json import load, dump
from os import getcwd
from sys import argv
from winsound import PlaySound

from PyQt5.QtCore import Qt, QRegExp, QBasicTimer, QThread, QTimer, pyqtSlot, QPoint, QRectF
from PyQt5.QtGui import QRegExpValidator, QMovie, QTextCursor, QColor, QFont, QTextLength, QTextCharFormat, QIcon, \
    QBitmap, QPainter, QBrush
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QApplication, QTextEdit, QTextBrowser, QLineEdit, QLabel, \
    QMenu, QAction
from UiCn.UiPinYin.Ui_Cn_PinYin import Ui_Cn_PinYin

# C:\Users\Administrator.DESKTOP-VMCD0IN\AppData\Roaming\Python\Python36\site-packages\pyqt5_tools
# E:\Qt\Qt5.11.1\5.11.1\mingw53_32\bin\
# uic     C:\ProgramData\Anaconda3\python.exe

class UiCn_PinYin_Logic(QWidget, Ui_Cn_PinYin):
    def __init__(self, parent):
        super(UiCn_PinYin_Logic, self).__init__(parent.widCenter)
        self.setupUi(self)
        self.p = parent
        self.pEventLog = parent.eventLog
        # self.textEditUp.setDisabled(True)

        # 课程选择菜单按钮显示出来，并提前加载模拟的widMenu内的数据
        parent.btnMenu.show()
        self.data = load(open(f'UiCn/UiPinYin/pinYin.json', 'r', encoding='utf-8'))
        parent.loadMenuData(self.data, self)

        # 创建一个计时器，用来实时显示数据
        self.timer = QBasicTimer()
        self.countTimer = 0  # 线程里的计数
        self.countSecond = 0
        self.countMinute = 0
        self.countHour = 0

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
            elif 27 + pixel + count <= 885:  # 894
                new += ' ' + j
                pixel += 27 + count
            else:
                self.listText.append(new)
                new = j
                pixel = 0
            if i == len(listStr) - 1 and new != '':
                self.listText.append(new)
        self.lenListText = len(self.listText)
        self.textEditUp.setText(self.listText[0])

    def on_textEditDn_textChanged(self):
        try:
            self.textDn = self.textEditDn.toPlainText()
            self.textUp = self.textEditUp.toPlainText()
            self.lenTextDn = len(self.textDn)
            self.lenTextUp = len(self.textUp)
            if self.lenTextDn == 0:  # 删除全部字符时，下面lastTextDn就超出索引了
                return
            if self.timer.isActive() is False:  # 这两句if就是让有输出时开始计时
                self.timer.start(10, self)
            lastTextDn = self.textDn[-1]
            lastTextUp = self.textUp[self.lenTextDn - 1]
            if lastTextDn in 'av':  # 目的是把输出的a和v，改成'ɑ'和'ü'。
                if lastTextDn == 'a':
                    lastTextDn = 'ɑ'
                else:
                    lastTextDn = 'ü'
                self.textEditDn.textCursor().deletePreviousChar()  # 删除前一个字符
                self.textEditDn.insertPlainText(lastTextDn)  # 把改过的字符串插入
            if lastTextDn == lastTextUp:
                PlaySound('UiCn/UiPinYin/sound/Type.wav', flags=1)
                color = 'gray'
            else:
                PlaySound('UiCn/UiPinYin/sound/ERROR.wav', flags=1)
                color = 'red'
            fmt = QTextCharFormat()  # 创建字符格式类
            fmt.setForeground(QColor(color))  # 设置格式类的字符颜色
            self.changeTextColor(fmt, self.lenTextDn)  # 调用自定义的改变字符颜色的方法
        except Exception as e:
            print(e)

    def changeTextColor(self, fmt, length):
        try:
            # 改变输入框textEditDn的字体颜色
            cursor = self.textEditDn.textCursor()
            cursor.setPosition(length - 1)  # 设置position位置(前一个字符),setPosition(虚的)位置和setCursorPosition(实体)位置不是一个概念
            cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, 1)  # 往右移动一次,并且选择(KeepAnchor).移动2次就选择2个字符
            self.textEditDn.blockSignals(True)  # 先关闭信号，不然报错超过递归深度
            cursor.mergeCharFormat(fmt)  # 选择的字符设置字符格式类
            self.textEditDn.blockSignals(False)  # 完成插入操作，再打开信号
            # self.textEditDn.mergeCurrentCharFormat(fmt)  # 这一句不知道做什么用的。

            # 改变显示框textEditUp的字体颜色
            cursor2 = self.textEditUp.textCursor()  # 没有焦点的textEditUp，不用关闭信号，直接操作
            cursor2.setPosition(length - 1)
            cursor2.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, 1)  # 往右移动1次,并且选择(KeepAnchor).移动2次就选择2个字符
            cursor2.mergeCharFormat(fmt)  # 选择的字符设置字符格式类

        except Exception as e:
            print(e)

    def on_textEditDn_cursorPositionChanged(self):
        if not self.textEditDn.textCursor().atEnd():  # 如果光标不在最后，强制移动到最后。禁止光标移动。
            self.textEditDn.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)

    def timerEvent(self, e):
        """实例化QBasicTimer的事件"""
        try:
            self.countTimer += 1
            # 时间
            if self.countTimer == 100:  # 设计的是千分之10秒刷新一次，所以等于100时才是1秒。这样你按一个键快速输入，
                self.countTimer = 0  # EidtInput不会再超出规定的达到26个字符停止，不然1秒才刷新，输入太快，一超出就崩溃了
                self.countSecond += 1
            if self.countSecond == 60:
                self.countMinute += 1
                self.countSecond = 0
            if self.countMinute == 60:
                self.countHour += 1
                self.countMinute = 0
            second, minute, hour = str(self.countSecond), str(self.countMinute), str(self.countHour)
            if self.countSecond < 10:  # 为了处理01不然上一句和这三个if都不需要
                second = '0' + str(self.countSecond)
            if self.countMinute < 10:
                minute = '0' + str(self.countMinute)
            if self.countHour < 10:
                hour = '0' + str(self.countHour)
            self.labTime.setText(f'{hour}:{minute}:{second}')
            # 速度
            lastSecond = self.countSecond + self.countMinute * 60 + self.countHour * 60 * 60
            if self.countSecond == 0:
                speed = 0
            else:
                speed = int(self.lenTextDn / lastSecond * 60)
            self.labSpeed.setText(f'{speed} 字/分')
            # 进度
            progress = int(self.lenTextDn / len(self.allChar) * 100)
            self.labProgress.setText(f'{progress}%')
            # 正确率
            if self.lenTextDn == 0:
                accuracy = 0
            else:
                right = 0
                for i, j in enumerate(self.textDn):
                    if self.textDn[i] == self.textUp[i]:
                        right += 1
                accuracy = int(right / self.lenTextDn * 100)
            self.labAccuracy.setText(f' {accuracy}%')

            # 显示下一组数据和结束条件
            if self.lenTextDn == self.lenTextUp:
                self.listText.pop(0)
                if len(self.listText):
                    self.textEditUp.setText(self.listText[0])
                    self.textEditDn.clear()
                else:
                    self.timer.stop()
                    self.textEditDn.setDisabled(True)
                    self.btnTimeStart.setDisabled(True)

            # if self.cursor.position() == self.countTextShow:  # 如果完成全部输入（不管对错），弹出成绩
            #     self.timer.stop()
            #     self.editInput.setEnabled(False)
            #     self.btn1.setEnabled(False)
            #     if accuracy < 90:
            #         self.dataStr = '因正确率低于90%，本次成绩 无效!'  # 空格一定要加上，后面有用
            #     else:
            #         lvList = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一',
            #                   '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九', '二十',
            #                   '二十一', '二十二', '二十三', '二十四', '二十五', '二十六', '二十七',
            #                   '二十八', '二十九', '三十', '三十一', '三十二', '三十三', '三十四', '三十五',
            #                   '三十六', '三十七', '三十八', '三十九', '四十', '四十一', '四十二', '四十三',
            #                   '四十四', '四十五', '四十六', '四十七', '四十八', '四十九', '五十']
            #         index = int(speed / 10)
            #         self.dataStr = f'速度：{speed} 字/分，正确率：{accuracy}%，级别：  {lvList[index]}级'  # 级别后要加两个空格，后面有用
            #
            #     # self.dialogScore = DialogScore(self.dataStr, self)  # 只要关闭就会delete掉。因为类里设置有Qt.WA_DeleteOnClose
            #     # self.dialogScore.exec()  # 模态运行
            #     # self.slotUpdataAndStop()  # 刷新editInput
        except Exception as e:
            print(e)
# class MenuData(QMenu, Ui_MenuData):
#     def __init__(self, data, parent):
#         super(MenuData, self).__init__(parent)
#         self.setupUi(self)
#
#         # 用遮罩的方法给窗体设置圆角
#         self.whiteMask = QBitmap(self.size())  # 创建位图，全屏大小
#         self.whiteMask.fill(Qt.white)  # 填充位图全白，相当于把窗口擦掉了，后面再用画刷显示出来。
#         p = QPainter(self.whiteMask)
#         brush = QBrush(Qt.black)  # 创建画刷并设置成黑色，这样黑色区域内的窗口就显示出来了。
#         p.setBrush(brush)  # 设置画刷
#         rectF = QRectF(0.0, 0.0, 284, 224)  # 画一个矩形
#         p.drawRoundedRect(rectF, 8.0, 8.0)  # 给矩形添加圆角
#         self.setMask(self.whiteMask)  # 设置遮罩
#
#         act = QAction(self.lineEditSearch)
#         act.setIcon(QIcon("UiCn/UiPinYin/image/search.png"))
#         self.lineEditSearch.addAction(act, QLineEdit.TrailingPosition)  # 右侧图标
#
#         self.btnClear.hide()
#
#         self.loadData(data, parent)
#
#     def loadData(self, data, parent):
#         def addGrid(btn):
#             count = len(self.scrollAreaWid.children()[1:])
#             row = count // 2  # 行索引，其实就是整除的值
#             column = count % 2  # 列索引，其实就是余数（remainder）
#             self.scrollAreaWid.children()[0].addWidget(btn, row, column)  # 第0项就是此widget的gridlayout
#
#         for k, v in data.items():
#             btn = QPushButton(k)
#             btn.clicked.connect(parent.getInputData(v))
#             addGrid(btn)
#
#     def on_lineEditSearch_textChanged(self, input):
#         print(22, input)
#         for btn in self.scrollAreaWid.children()[1:]:
#             bText = btn.text()
#             if input in bText:
#                 print(bText, 222)
#                 btn.show()
#             else:
#                 btn.hide()
#
#
#     # shengMu = 'b p m f d t n l g k h j q x zh ch sh r z c s y w'  # 声母
#     # yunMu = 'ɑ o e i u ü ɑi ei ui ɑo ou iu ie üe er ɑn en in un ün ɑng eng ing ong'  # 韵母
#     # wholeSyllables = 'zhi chi shi ri zi ci si yi wu yu ye yue yuɑn yin yun ying'  # 整体认读音节
#     # b = 'b bɑ bo bɑi bei bɑo bɑn ben bɑng beng bi bie biɑo biɑn bin bing bu'  # 拼音音节表[b]
#     # p = 'p pɑ po pɑi pɑo pou pɑn pen pei pɑng peng pi pie piɑo piɑn pin ping pu'
#     # m = 'm mɑ mo me mɑi mɑo mou mɑn men mei mɑng meng mi mie miɑo miu miɑn min ming mu'
#     # f = 'f fɑ fo fei fou fɑn fen fɑng feng fu'
#     # d = 'd dɑ de dɑi dei dɑo dou dɑn dɑng den deng di die diɑo diu diɑn ding dong du duɑn dun dui duo'
#     # t = 't tɑ te tɑi tɑo tou tɑn tɑng teng ti tie tiɑo tiɑn ting tong tu tuɑn tun tui tuo'
#     # n = 'n nɑ nɑi nei nɑo ne nen nɑn nɑng neng ni nie niɑo niu niɑn nin niɑng ning nong nou nu nuɑn nun nuo nü nüe'
#     # l = 'l lɑ le lɑi lei lɑo lou lɑn lɑng len leng li liɑ lie liɑo liu liɑn lin liɑng ling long lu luo lou luɑn lun lü lüe'
#     # g = 'g gɑ ge gɑi gei gɑo gou gɑn gen gɑng geng gong gu guɑ guɑi guɑn guɑng gui guo'
#     # k = 'k kɑ ke kɑi kɑo kou kɑn ken kɑng keng kong ku kuɑ kuɑi kuɑn kuɑng kui kun kuo'
#     # h = 'h hɑ he hɑi hɑn hei hɑo hou hen hɑng heng hong hu huɑ huɑi huɑn hui huo hun huɑng'
#     # j = 'j ji jiɑ jie jiɑo jiu jiɑn jin jiɑng jing jiong ju juɑn jun jue'
#     # q = 'q qi qiɑ qie qiɑo qiu qiɑn qin qiɑng qing qiong qu quɑn qun que'
#     # x = 'x xi xiɑ xie xiɑo xiu xiɑn xin xiɑng xing xiong xu xuɑn xun xue'
#     # zh = 'zh zhɑ zhe zhi zhɑi zhɑo zhou zhɑn zhen zhɑng zheng zhong zhu zhuɑ zhuɑi zhuɑn zhuɑng zhun zhui zhuo'
#     # ch = 'ch chɑ che chi chɑi chɑo chou chɑn chen chɑng cheng chong chu chuɑ chuɑi chuɑn chuɑng chun chui chuo'
#     # sh = 'sh shɑ she shi shɑi shɑo shou shɑn shen shɑng sheng shu shuɑ shuɑi shuɑn shuɑng shun shui shuo'
#     # r = 'r re ri rɑo rou rɑn ren rɑng reng rong ru ruɑn run ruo'
#     # z = 'z zɑ ze zi zɑi zɑo zɑn zou zɑng zei zen zeng zong zu zuɑn zun zui zuo'
#     # c = 'c cɑ ce ci cɑi cɑo cou cɑn cen cɑng ceng cong cu cuɑn cun cui cuo'
#     # s = 's sɑ se si sɑi sɑo sou sɑn sen sɑng seng song su suɑn sun sui suo'
#     # y = 'y yɑ yɑo you yɑn yɑng yu ye yue yuɑn yi yin yun ying yo yong'
#     # w = 'w wɑ wo wɑi wei wɑn wen wɑng weng wu'
#     # lis = [b, p, m, f, d, t, n, l, g, k, h, j, q, x, zh, ch, sh, r, z, c, s, y, w]
#     # dic = dict()
#     # dic['声母'] = shengMu
#     # dic['韵母'] = yunMu
#     # dic['整体认读音节'] = wholeSyllables
#     # for i in lis:
#     #     if i in [zh, ch, sh]:
#     #         dic["拼音音节["+i[:2]+"]"] = i
#     #     else:
#     #         dic["拼音音节["+i[0]+"]"] = i
#     #
#     # # print(dic)
#     # # dump(dic, open('pinYin.json', 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
#     # # a = load(open('UiCn/UiPinYin/pinYin.json', 'r', encoding='utf-8'))
#     # # print(a)
#
#     # b = ''
#     # d = dict()
#     # for k, v in self.data.items():
#     #     a = self.data[k].split(' ')
#     #     for i in a[:-1]:
#     #         b += i + '    '
#     #         if i == a[:-1][-1]:
#     #             b += a[-1]
#     #     d[k] = b
#     #     b = ''
#     # print(d)
#     # # self.lineEditUp.cursorPositionChanged.connect
#     # dump(d, open('pinYin.json', 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
#     # print('OK')
