import datetime
import os
import shutil
import sys
from json import dump
from threading import Thread
from functools import partial

from PyQt5.QtCore import Qt, QSize, QPoint, QThread, QTimer, QBasicTimer, QEvent, QRect, QRectF, pyqtSlot
from PyQt5.QtGui import QPainter, QMovie, QIcon, QMouseEvent, QEnterEvent, QBitmap, QPen, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QStyleOption, QStyle, QTextEdit, QTextBrowser, QDesktopWidget, QPushButton, QLabel, \
    QDialog, QGridLayout, QMenu, QFileDialog, QListWidget, QAction, QLineEdit, QComboBox, QTableWidget

# from UiCn.UiPinYin.Ui_MenuData import Ui_MenuData
from UiMain.Ui_DialogChoose_Logic import Ui_DialogChoose_Logic
from UiMain.Ui_Main import Ui_Main
from UiMain.Ui_MenuSkin import Ui_MenuSkin

class Ui_Main_Logic(QWidget, Ui_Main):
    def __init__(self, app, parent=None):
        super(Ui_Main_Logic, self).__init__()
        self.setupUi(self)
        self.moveCenter()  # 让窗口显示在屏幕中间的自定义方法
        self.app = app
        self.app.widget = self.widMenu

        # 用遮罩的方法给窗体设置圆角
        self.whiteMask = QBitmap(self.size())  # 创建位图，窗体大小
        self.whiteMask.fill(Qt.white)  # 填充位图全白，相当于把窗口擦掉了，后面再用画刷显示出来。
        p = QPainter(self.whiteMask)
        brush = QBrush(Qt.black)  # 创建画刷并设置成黑色，这样黑色区域内的窗口就显示出来了。
        p.setBrush(brush)  # 设置画刷
        rectF = QRectF(0.0, 0.0, 980, 700)  # 画一个矩形
        p.drawRoundedRect(rectF, 8.0, 8.0)  # 给矩形添加圆角
        self.setMask(self.whiteMask)  # 设置遮罩

        # 先隐藏一些控件和按钮gif图片的设置
        self.widBack.hide()
        self.stkWid.hide()
        self.widHello.hide()
        self.widMenu.hide()
        self.btnSetMovie()  # 按钮gif图片的设置

        # 自定义的标题栏设置
        self.widTitle.installEventFilter(self)  # 注册事件遍历器用于控制窗口移动
        self.flagMove = False
        self.menuSkin = MenuSkin(self)  # 可以不实例化，那样就得每次点击都要创建，启动慢了，但是内存开销要少一些。
        self.btnChangeSkin.clicked.connect(
            lambda: self.menuSkin.exec(self.mapToGlobal(QPoint(747, 50))))  # 必须以self.myApp的坐标为准

        # 返回框架widBack控件设置
        self.labBackLink.setText("<style> a {text-decoration: none;color:gray;} </style><a href='首页'>首页 </a>> ")
        self.labBackLink.linkActivated[str].connect(self.fn)
        self.labBackLink.linkHovered[str].connect(self.fn)
        self.btnMenu.clicked.connect(self.widMenu.show)

        # 自定义模拟QMenu的QWidget容器设置
        self.widMenu.installEventFilter(self)
        self.btnMenu.installEventFilter(self)
        self.btnMenu.setIcon(QIcon("UiMain/image/drop-down.png"))
        self.btnMenu.setLayoutDirection(Qt.RightToLeft)
        act = QAction(self.lineEditSearch)
        act.setIcon(QIcon("UiCn/UiPinYin/image/search.png"))
        self.lineEditSearch.addAction(act, QLineEdit.TrailingPosition)  # 右侧图标
        self.btnClear.hide()

        # a = QTextBrowser(self)
        # a.resize(300, 300)
        # a.setOpenExternalLinks(True)
        # a.append("<a href = \"http://www.sina.com.cn/\">新浪</a>")

        # 一些控件的信号与槽
        self.flagUi = None  # 此标志是记录在学习或者娱乐选项下的哪一个ui选项被显示了，以方便点击返回时的使得操作
        [btn.clicked.connect(partial(self.slot_widChoseBtns, index)) for index, btn in
         enumerate([self.btnCn, self.btnMath, self.btnEn, self.btnGames, self.btnMusics, self.btnMovies, self.btnBack])]

        self.btnCn_HanZi.clicked.connect(self.slot_stkWidBtns)
        self.btnCn_PinYin.clicked.connect(self.slot_stkWidBtns)
        self.btnMath_PlusOrMinus100.clicked.connect(self.slot_stkWidBtns)
        self.btnGames_Rock.clicked.connect(self.slot_stkWidBtns)
        self.btnGames_Guess.clicked.connect(self.slot_stkWidBtns)
        self.btnGames_Puzzle.clicked.connect(self.slot_stkWidBtns)
        self.btnGames_CardMatching.clicked.connect(self.slot_stkWidBtns)

        # 写了一个简单的错误日志，传给每个界面此日志的调用方法，并且在方法内记录日志到Log.log文件
        menuEventLog = QMenu(self)
        menuEventLog.setFixedSize(980, 200)
        self.listWidEventLog = QListWidget(menuEventLog)
        self.listWidEventLog.setFixedSize(980, 200)
        self.btnStatusTip.clicked.connect(lambda: menuEventLog.exec(self.mapToGlobal(QPoint(0, 500))))
        self.btnStatusTipChange.clicked.connect(lambda: self.widStatusTip.setVisible(self.widStatusTip.isHidden()))
        self.widStatusTip.installEventFilter(self)  # 注册事件遍历器用于设置self.widStatusTip显示时间
        self.timer = QBasicTimer()
        # self.btnStatusTipChange.clicked.connect(lambda: self.timer.start(1000, Qt.PreciseTimer, self))
        self.eventLog('加载完毕')

    def isVipLogin(self, vip):
        self.vip = vip
        uiLogin = self.sender().nativeParentWidget()
        self.id = uiLogin.comboUserID.currentText()
        pswd = uiLogin.lineEdUserPswd.text()

        self.userData = uiLogin.userData
        if vip:  # 会员登录
            if self.id in self.userData and pswd == self.userData[self.id]["密码"]:
                self.btnUserpic.setStyleSheet(f"border-image: url(image/userPic/{self.userData[self.id]['头像']})")
                self.labGoldCount.setText(self.userData[self.id]["金币"])
                self.labJewelCount.setText(self.userData[self.id]["钻石"])
                self.labHello.setText(f"Hi,{self.userData[self.id]['昵称']}")
            else:
                uiLogin.labLoginError.show()
                return  # 显示出密码或账号错误后，什么也不做，下面代码有关闭窗口
        else:  # 游客登录
            self.labGoldCount.setText('50')
            self.labJewelCount.setText('20')
        uiLogin.parent().close()

    def loadMenuData(self, data, parent):
        """各个界面调用加载课程菜单数据"""

        def addGrid(btn):
            count = len(self.scrollAreaWid.children()[1:])
            row = count // 2  # 行索引，其实就是整除的值
            column = count % 2  # 列索引，其实就是余数（remainder）
            self.scrollAreaWid.children()[0].addWidget(btn, row, column)  # 第0项就是此widget的gridlayout

        # 先把别的界面设置的btnMenu的text恢复默认，并把菜单列表删除掉
        self.btnMenu.setText("课程选择")
        for i in self.scrollAreaWid.children()[1:]:
            i.deleteLater()  # 如果是实时删除，只能用sip库的delete方法
        # 加载菜单，动态添加按钮，并设置按钮的text（菜单名）
        if isinstance(data, dict):
            for k, v in data.items():
                btn = QPushButton(k)
                btn.clicked.connect(partial(parent.getInputData, v))
                btn.clicked.connect(partial(self.btnMenu.setText, k))
                addGrid(btn)
        elif isinstance(data, list):
            for i in data:
                btn = QPushButton(i)
                btn.clicked.connect(partial(parent.getInputData, i))
                btn.clicked.connect(partial(self.btnMenu.setText, i))
                btn.clicked.connect(self.widMenu.hide)  # 选择菜单后隐藏
                addGrid(btn)

    def btnSetMovie(self):
        """动画按钮的特殊设置。一个没有布局的QWidget，下面放QLabel显示gif图片，上面放QPushButton执行点击事件"""
        labs = [self.labMovies, self.labGames_Rock, self.labGames_Guess, self.labGames_Puzzle, self.labGames_CardMatching]
        movies = [QMovie('UiMain/image/10.gif'), QMovie('UiMain/image/game1.gif'), QMovie('UiMain/image/game2.gif'),
                  QMovie('UiMain/image/game3.gif'), QMovie('UiMain/image/game4.gif')]
        for index, lab in enumerate(labs):
            lab.setMovie(movies[index])
            movies[index].start()

    def eventFilter(self, obj, e):
        """一些控件的事件遍历器"""
        if obj == self.widTitle:  # obj设置左键点击移动窗口
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

        if obj == self.widMenu:
            if e.type() == e.Leave:
                self.app.flagMenuLeave = True
            if e.type() == e.Enter:
                self.app.flagMenuLeave = False
            return False

        if obj == self.btnMenu:  # obj设置鼠标滑入滑出改变QAction的Icon图片
            if e.type() == e.Enter:  # 鼠标滑入 HoverMove会一直打印，enter只触发一次
                self.btnMenu.setIcon(QIcon("UiMain/image/drop-down-hover.png"))
            if e.type() == e.Leave:  # 鼠标滑出 HoverLeave也只触发一次
                self.btnMenu.setIcon(QIcon("UiMain/image/drop-down.png"))
            return False  # 必须有

        if obj == self.widStatusTip:  # obj设置显示时间
            if e.type() == e.Show:
                self.flagCount = 10
                self.timer.start(1000, Qt.PreciseTimer, self)
            if e.type() == e.Hide:
                if self.timer.isActive():
                    self.timer.stop()
            return False  # 必须有

        else:
            return False  # 必须有，we don't care about other events

    def fn(self, text):
        if text == '首页':  # underline
            print(self.sender())
            htmlStr = "<style> a {text-decoration: underline} </style><a style='color: gray' href='首页'>首页 </a>>"
            self.labBackLink.setText(htmlStr)
            # self.labBackLink.setText(
            #     "<style> a {text-decoration: none;color:gray;} </style><a style='color: gray' href='首页'>首页 > ")

    @pyqtSlot()
    def on_btnCards_clicked(self):
        from UiMain.Ui_Card_Logic import Ui_Card_Logic
        self.uiCard = Ui_Card_Logic(self)
        self.uiCard.show()

    def updateGoldAndJewel(self, virtualGood, num, flag):
        if virtualGood == '金币':
            obj = self.labGoldCount
        elif virtualGood == '钻石':
            obj = self.labJewelCount

        intText = int(obj.text())
        if flag == 'Plus':
            obj.setText(str(intText + num))
        elif flag == 'Minus':
            if intText >= num:
                obj.setText(str(intText - num))
            else:
                Ui_DialogChoose_Logic().setInfo(self, f'{virtualGood}', f'你的{virtualGood}不够了，\n要多练习才能增加哦!')
                return False
        if self.vip:  # 如果是会员登录，就保存信息
            self.userData[self.id]["金币"] = self.labGoldCount.text()
            self.userData[self.id]["钻石"] = self.labJewelCount.text()
            dump(self.userData, open('UserData.json', 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
        return True

    def slot_stkWidBtns(self):
        from UiCn.UiHanZi.Ui_Cn_HanZi_Logic import UiCn_HanZi_Logic
        from UiCn.UiPinYin.Ui_Cn_PinYin_Logic import UiCn_PinYin_Logic
        from UiMath.UiPlusOrMinus100.Ui_Math_PlusOrMinus100_Logic import UiMath_PlusOrMinus100_Logic
        from UiGames.UiRock.Ui_Games_Rock_Logic import UiGames_Rock_Logic
        from UiGames.UiGuess.Ui_Games_Guess_Logic import UiGames_Guess_Logic
        from UiGames.UIPuzzle.Ui_Puzzle_Logic import UiGames_Puzzle_Logic
        from UiGames.Ui_CardMatching.Ui_CardMatching_Logic import UiGames_CardMatching_Logic

        sender = self.sender()
        if sender == self.btnCn_HanZi:
            self.uiCn_HanZi = UiCn_HanZi_Logic(self)
            self.uiCn_HanZi.show()
            self.flagUi = self.uiCn_HanZi
        elif sender == self.btnCn_PinYin:
            self.uiCn_PinYin = UiCn_PinYin_Logic(self)
            self.uiCn_PinYin.show()
            self.flagUi = self.uiCn_PinYin
        elif sender == self.btnGames_Rock:
            self.uiGames_Rock = UiGames_Rock_Logic(self)
            self.uiGames_Rock.show()
            self.flagUi = self.uiGames_Rock
        elif sender == self.btnGames_Guess:
            self.uiGames_Guess = UiGames_Guess_Logic(self)
            self.uiGames_Guess.show()
            self.flagUi = self.uiGames_Guess
        elif sender == self.btnMath_PlusOrMinus100:
            self.uiMath_PlusOrMinus100 = UiMath_PlusOrMinus100_Logic(self)
            self.uiMath_PlusOrMinus100.show()
            self.flagUi = self.uiMath_PlusOrMinus100
        elif sender == self.btnGames_Puzzle:
            self.uiGames_Puzzle = UiGames_Puzzle_Logic(self)
            self.uiGames_Puzzle.show()
            self.flagUi = self.uiGames_Puzzle
        elif sender == self.btnGames_CardMatching:
            self.uiGames_CardMatching = UiGames_CardMatching_Logic(self)
            self.uiGames_CardMatching.show()
            self.flagUi = self.uiGames_CardMatching
        self.flagUi.move(0, 30)  # 下面这两句这里设置后，逻辑文件里就不需要再设置了
        self.flagUi.setAttribute(Qt.WA_StyledBackground)  # 这一句可以解决QWidget不显示图片的问题。
        self.stkWid.hide()
        self.widHello.hide()

    def slot_widChoseBtns(self, index):
        """因为返回按钮和学习娱乐按钮列表的槽函数放在了一起（为了方便），所以要先判断是否是返回按钮在点击"""
        self.btnMenu.hide()
        flag = True
        if index == 6:  # 如果是返回按钮在点击，要针对两种情况做处理
            if self.flagUi:  # 第一种：已经点击了学习娱乐选项下选项，显示了此选项的ui
                self.flagUi.hide()
                self.flagUi = None  # 重新把是否显示了ui的标志设置为None.
                # self.act.triggered.connect(print)  # 因为如果某页面没有设置act的槽函数，就不能重复dis，所以随便给一个槽函数，反正下一句就dis掉了
                # self.act.disconnect()  # 因为不同页面有不同的槽函数，并且页面返回时此页面被销毁，所以每次每回时要彻底断开连接
            else:
                flag = False  # 第二种：没有点击了学习娱乐选项下选项，要回到首页，让flag为False，下面代码作相反设置就简便许多
        else:  # 如果不是返回按钮在点击，就是学习娱乐按钮列表在点击
            self.stkWid.setCurrentIndex(index)  # self.stkWid设置对应的索引

        self.stkWid.setVisible(flag)
        self.widBack.setVisible(flag)  # 只有点击学习娱乐选项时，返回按钮才会显示
        self.widHello.setVisible(flag)
        self.widWelcome.setVisible(not flag)
        self.widChose.setVisible(not flag)

    def eventLog(self, info):
        from time import strftime, localtime, time
        logTime = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))
        if isinstance(info, list):  # 是列表说明是try..except..的错误报告
            self.labStatusTip.setText('程序异常')
            self.labStatusTip.setStyleSheet('color:red;')
            self.btnStatusTip.setStyleSheet('border-image: url("UiMain/image/bug.png");')
            temp = f"{logTime}:  {info[0]}\n{info[1]}"
            self.listWidEventLog.addItem(temp)
            with open("Log.log", 'a', encoding='utf-8') as f:  # 在log文件中记录日志
                f.write("\n\n" + temp)
        else:
            self.labStatusTip.setText(info)
            self.labStatusTip.setStyleSheet('color:black;')
            self.btnStatusTip.setStyleSheet('border-image: url("UiMain/image/warning.png");')
        self.widStatusTip.show()

    def timerEvent(self, e):
        self.flagCount -= 1
        if not self.flagCount:
            self.timer.stop()
            self.widStatusTip.hide()

    # def closeEvent(self, e):
    #     self.userData[]

    def moveCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class MenuSkin(QMenu, Ui_MenuSkin):
    def __init__(self, myApp):
        super(MenuSkin, self).__init__()
        self.setupUi(self)
        self.myApp = myApp
        self.tInit = QThread()
        self.tInit.started.connect(self.thread_ui)
        # self.tInit.finished.connect(self.tInit.deleteLater)
        self.tInit.start()

    def thread_ui(self):
        """加载换肤的按钮和图片"""
        listFileName = os.listdir('UiMain/image/skin')
        rowTab1 = 0
        rowTab2 = 0
        columnTab1 = 0
        columnTab2 = 0
        for i, n in enumerate(listFileName):
            fileExtension = n[-3:]  # 得到图片扩展名
            btn = QPushButton()
            btn.setFixedSize(50, 50)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet(f'border-image: url("UiMain/image/skin/{listFileName[i]}")')

            btn.clicked.connect(self.slot_btns(listFileName[i]))
            if fileExtension != 'gif':
                self.gridTab1.addWidget(btn, rowTab1, columnTab1)
                columnTab1 += 1
                if columnTab1 == 5:
                    rowTab1 += 1
                    columnTab1 = 0
            else:
                self.gridTab2.addWidget(btn, rowTab2, columnTab2)
                columnTab2 += 1
                if columnTab2 == 5:
                    rowTab2 += 1
                    columnTab2 = 0

            if n == listFileName[-1]:  # 在QTabWidget每一页最后设置一个添加图片按钮
                for i in range(2):
                    btnAddSkin = QPushButton()
                    btnAddSkin.setFixedSize(50, 50)
                    btnAddSkin.setObjectName('btnAddSkin')  # 静态和动态选项的两个添加图片btn对象名设置成一样的
                    btnAddSkin.setCursor(Qt.PointingHandCursor)
                    btnAddSkin.clicked.connect(self.slot_btnAddSkin)
                    if i == 0:
                        self.gridTab1.addWidget(btnAddSkin, rowTab1, columnTab1)
                    else:
                        self.gridTab2.addWidget(btnAddSkin, rowTab2, columnTab2)

    def slot_btnAddSkin(self):
        """添加皮肤功能"""
        imgExtension = "*.jpg;*.jpeg;;*.png;;*.gif;;所有图片格式(*.jpg;*.png;*.gif)"
        fileDialog = QFileDialog()
        dstFileList, _ = fileDialog.getOpenFileNames(self, "选取文件", "C:/", imgExtension)
        for dstFile in dstFileList:
            fPath, fName = os.path.split(dstFile)
            splitName = fName.split('.')  # 此变量得到数据后就固定了，下面的循环不影响此变量
            flag = 1
            while True:
                newFileName = fName
                savePath = "F:\PycharmProjects\PyQt5\LearningForChildren\IUiMain/image/skin/" + newFileName
                whetherSame = os.path.exists(savePath)  # 这句是判断路径是否正确,可以判断是否存在相同的文件名
                if whetherSame:
                    sequenceNum = f"({flag}).{splitName[1]}"
                    fName = f"{splitName[0]}{sequenceNum}"
                    flag += 1
                else:
                    shutil.copyfile(dstFile, savePath)  # 复制原图片路径到指定路径
                    break
        self.thread_ui()
        self.show()
        # fileDialog.setOptions(QFileDialog.DontUseNativeDialog) # 不管用，这面的设置后可以设置样式了，但不知道怎么改btn名字
        # fileDialog.getOpenFileNames(self, "选取文件", "C:/", imgExtension, options=QFileDialog.DontUseNativeDialog)

    def slot_btns(self, fileName):
        """换肤功能里面每个皮肤按钮的换肤设置"""

        def _connect():  # 用label做界面背景可以设置gif动画
            if fileName[-3:] == 'gif':
                movie = QMovie(f"UiMain/image/skin/{fileName}")
                movie.start()
                self.myApp.labMainBackground.setMovie(movie)
            else:
                if self.myApp.labMainBackground.movie():
                    self.myApp.labMainBackground.movie().deleteLater()
                self.myApp.labMainBackground.setStyleSheet("border-image:url('UiMain/image/skin/" + fileName + "');")
            # self.sender().deleteLater()

        return _connect
