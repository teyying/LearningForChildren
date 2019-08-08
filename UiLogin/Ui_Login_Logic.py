import cgitb
from json import load

from PyQt5.QtCore import Qt, QPoint, QRectF, pyqtSlot, QSize, QEventLoop, QTimer, QPointF, QEvent
from PyQt5.QtGui import QMovie, QIcon, QBrush, QBitmap, QPainter, QPixmap, QPainterPath, QTransform, QPen, QMouseEvent
from PyQt5.QtWidgets import QAction, QLineEdit, QListView, QLabel, QMenu, QDialog, QGraphicsWidget, QGraphicsScene, \
    QGraphicsLinearLayout, QGraphicsView, QApplication, QGraphicsProxyWidget
from UiLogin.Ui_Login import Ui_Login
from UiLogin.Ui_Register import Ui_Register
from UiLogin.menuKeyBoard import Ui_menuKeyBoard

cgitb.enable(format='text')  # 解决pyqt5异常只要进入事件循环,程序就崩溃,而没有任何提示


# class Ui_Login_Logic(QDialog, Ui_Login):
#     def __init__(self, parent):
#         super(Ui_Login_Logic, self).__init__()
#         self.setupUi(self)
#         self.setWindowFlags(Qt.FramelessWindowHint)  # 去掉标题栏的代码,这种顶部就不会出现空白,但是不能移动，需自己处理
#         self.installEventFilter(self)
#         self.flagMove = False
#         self.labLoginError.hide()  # 账号密码错误提示。提前隐藏。
#
#         # 用遮罩的方法给窗体设置圆角
#         self.whiteMask = QBitmap(self.size())  # 创建位图，窗体大小
#         self.whiteMask.fill(Qt.white)  # 填充位图全白，相当于把窗口擦掉了，后面再用画刷显示出来。
#         p = QPainter(self.whiteMask)
#         p.setBrush(QBrush(Qt.black))  # 设置画刷
#         p.drawRoundedRect(QRectF(0.0, 0.0, 400, 300), 5.0, 5.0)  # 窗体的宽和高，给矩形添加圆角
#         self.setMask(self.whiteMask)  # 设置遮罩
#
#         self.movie = QMovie('UiLogin/image/0-1.gif')
#         self.labBg.setMovie(self.movie)
#         self.movie.start()
#         self.btnExit.clicked.connect(exit)  # 这种才是彻底的关闭所有程序
#         self.btnVipLogin.clicked.connect(lambda: parent.isVipLogin(True))
#         self.btnVisitorLogin.clicked.connect(lambda: parent.isVipLogin(False))
#
#         self.userData = load(open('UserData.json', 'r', encoding='utf-8'))  # 加载用户数据
#         # 账号输入下拉列表的设置
#         self.comboUserID.setView(QListView())  # 先随便设置一个QListView()，使下拉列表可以设置qss样式
#         self.actLeftUserID = QAction(QIcon("UiLogin/image/3.png"), '', self.comboUserID.lineEdit())
#         self.comboUserID.lineEdit().addAction(self.actLeftUserID, QLineEdit.LeadingPosition)  # 左侧图标
#         self.comboUserID.lineEdit().setPlaceholderText('账号')  # 设置默认提示语
#         self.comboUserID.lineEdit().setMaxLength(11)
#         self.comboUserID.setIconSize(QSize(40, 40))
#         self.comboUserID.lineEdit().setClearButtonEnabled(True)
#         self.comboUserID.installEventFilter(self)
#
#         # 密码框的设置
#         self.actLeftPswd = QAction(QIcon("UiLogin/image/1.png"), '', self.lineEdUserPswd)
#         self.actRightPswd = QAction(QIcon("UiLogin/image/17.png"), '', self.lineEdUserPswd)
#         self.actRightPswd.triggered.connect(lambda: self.menuKeyBoard.exec(self.mapToGlobal(QPoint(93, 233))))
#         self.menuKeyBoard = MyMenu(self)
#
#         self.lineEdUserPswd.addAction(self.actLeftPswd, QLineEdit.LeadingPosition)  # 左侧图标
#         self.lineEdUserPswd.addAction(self.actRightPswd, QLineEdit.TrailingPosition)  # 右侧图标
#         self.lineEdUserPswd.installEventFilter(self)
#
#         # 一些控件的信号与槽的绑定
#         self.btnSignIn.clicked.connect(lambda: print('剑灵'))
#         self.loadUserData()
#     def loadUserData(self):
#         self.userData = load(open('UserData.json', 'r', encoding='utf-8'))
#         for k, v in self.userData.items():
#             self.comboUserID.addItem(QIcon(self.getCircularPix(v['头像'])), f"{k}\n{v['昵称']}")
#         # 添加完item，下拉列表要设置初始为空，这样item中的icon就不会设置到下拉列表的lineEdit上了
#         self.comboUserID.setCurrentIndex(-1)
#
#     @pyqtSlot(str)
#     def on_comboUserID_activated(self, text):
#         """选择下拉项后，重新设置显示为空项，再改变lineEdit的text"""
#         self.comboUserID.setCurrentIndex(-1)  # 下拉列表要设置初始为空，这样item中的icon就不会设置到下拉列表的lineEdit上了
#         id, nickname = text.split('\n')  # 添加到item的用户数据都是id+换行+昵称['123', '小明']，如果没有昵称是['123', '']
#         self.labUserpic.setStyleSheet(f"border-image: url('image/userPic/{self.userData[id]['头像']}')")
#         self.comboUserID.lineEdit().setText(id)  # 自己单独通过下拉列表下的lineEdit设置选择item后显示内容
#         if self.userData[id]['记住密码']:
#             self.lineEdUserPswd.setText(self.userData[id]['密码'])
#             self.cBoxKeepPswd.setChecked(True)
#         self.setFocus()
#
#     def getCircularPix(self, userPic):
#         """返回一个圆形的QPixmap"""
#         size = self.comboUserID.iconSize()
#         pixTarget = QPixmap(size)  # 最终图片对象，设置尺寸和控件一样大
#         pixTarget.fill(Qt.transparent)  # 最终图片对象背景先填充为透明
#         # 加载要画在最终图片对象上的图片，并缩放和控件一样大
#         pixBg = QPixmap("image/userPic/"+userPic).scaled(size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
#         painter = QPainter(pixTarget)
#         # 抗锯齿
#         painter.setRenderHint(QPainter.Antialiasing, True)
#         painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
#         painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
#
#         path = QPainterPath()
#         path.addRoundedRect(0, 0, size.height(), size.width(), (size/2).height(), (size/2).width())  # 画圆形路径
#         painter.setClipPath(path)  # 设置QPainter为此路径
#         painter.drawPixmap(0, 0, pixBg)  # 在圆形区域内0，0的位置，把加载的图片画上
#         return pixTarget
#
#     def eventFilter(self, obj, e):
#         if e.type() == e.MouseButtonPress:  # 只为了提前拦截下拉列表总是先进入FocusIn事件
#             self.comboUserID.setStyleSheet('font-size:13px;color:#838383;')
#
#         if obj == self:
#             if e.type() == e.MouseButtonPress:
#                 if e.button() == Qt.LeftButton:
#                     self.setFocus()  # 主要处理焦点在账号和密码框内时，左键窗口的焦点位置，让输入框失去焦点
#                     self.flagMove = True
#                     self.posMove = e.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
#                     e.accept()
#                 elif e.button() == Qt.RightButton:  # 如果焦点在密码框里，右键窗口的焦点位置，账号框会得到焦点并全选
#                     if self.lineEdUserPswd.hasFocus():
#                         self.comboUserID.setFocus()
#                         self.comboUserID.lineEdit().selectAll()
#             if self.flagMove and e.type() == e.MouseMove:
#                 self.move(e.globalPos() - self.posMove)  # 更改窗口位置
#                 e.accept()
#             if e.type() == e.MouseButtonRelease:
#                 self.flagMove = False
#
#         if obj == self.comboUserID:  # 只要点击下拉箭头，总会先进FocusIn再进FocusOut
#             if e.type() == e.FocusIn:  # 改变图标，默认字符设置为空，再改变字符尺寸变大和颜色，不然"账号"会变17px,黑色,影响视频效果
#                 self.actLeftUserID.setIcon(QIcon("UiLogin/image/4.png"))
#                 self.comboUserID.lineEdit().setPlaceholderText('')
#                 self.comboUserID.setStyleSheet('font-size:17px;color:black;')
#                 self.labLoginError.hide()
#             # 如果失去焦点，并且下拉列表的ListView事实意义上不是显示的
#             if e.type() == e.FocusOut and not self.comboUserID.view().isVisible():  # 恢复图标，恢复默认字符，再恢复字符尺寸变小和颜色
#                 self.comboUserID.lineEdit().setPlaceholderText('账号')
#                 self.comboUserID.setStyleSheet('font-size:13px;color:#838383;')
#                 self.actLeftUserID.setIcon(QIcon("UiLogin/image/3.png"))
#             return False
#
#         if obj == self.lineEdUserPswd:  # 改变图标，默认字符设置为空，再改变字符尺寸变大和颜色，就不影响视觉效果了
#             if e.type() == e.FocusIn:
#                 self.actLeftPswd.setIcon(QIcon("UiLogin/image/2.png"))
#                 self.lineEdUserPswd.setPlaceholderText('')
#                 self.lineEdUserPswd.setStyleSheet('font-size:16px;color:black;')
#                 self.labLoginError.hide()
#             if e.type() == e.FocusOut:  # 失去焦点：恢复图标，恢复默认字符，再恢复字符尺寸变小和颜色
#                 self.actLeftPswd.setIcon(QIcon("UiLogin/image/1.png"))
#                 self.lineEdUserPswd.setPlaceholderText('密码')
#                 self.lineEdUserPswd.setStyleSheet('font-size:13px;color:#838383;')
#             return False
#         else:
#             return False
#
class MyMenu(QMenu, Ui_menuKeyBoard):
    """自定义的QMenu类，通过QAction设置MyMenu打开自己做的软键盘"""

    def __init__(self, parent):
        super(MyMenu, self).__init__()
        self.p = parent
        self.setupUi(self)
        self.flagMouseLeave = True  # 鼠标是否移入QMenu的标记，为了处理menu中点击空白地方会关闭的bug
        self.setFixedSize(415, 110)
        self.setStyleSheet('background-color: #1B93D9')
        self.installEventFilter(self)

        self.flagShift = 0
        self.flagCapsLock = 0
        self.listNumSymbolBtn = []
        self.listLetterBtn = []
        self.strStyleSheet = 'QPushButton {background-color:#cde6c7;} QPushButton:hover {background:#48D1BC} ' \
                             'QPushButton:pressed {background:qlineargradient(spread:pad, x1:0.494, y1:1, x2:0.482955,' \
                             'y2:0.046, stop:0 rgba(0, 191, 162, 255), stop:1 rgba(255, 255, 255, 255));}'
        for btn in self.children()[2:]:  # 前两个是布局
            text = btn.text()
            btn.clicked.connect(self.slot_btnsFromMenu)
            btn.setStyleSheet(self.strStyleSheet)  # btn按下显示渐变色
            if len(text) == 2:
                self.addLab(text, btn)  # 为了处理btn中不能两个字符一个低一个高,往btn里添加了两个lab，btn没有富文本功能
                btn.setText('')  # self.addLab中的两个lab已经显示text了，所以要把btn的text清除(还可以让这btn文字全透明)
                self.listNumSymbolBtn.append(btn)

            elif text == '×':
                btn.setStyleSheet('QPushButton {background : transparent;} QPushButton:hover {background:#FF5439;}')
                btn.setToolTip('关闭键盘')

            elif text not in ['Caps Lock', 'Shift', '←']:
                self.listLetterBtn.append(btn)

    def slot_btnsFromMenu(self):
        sender = self.sender()

        if sender == self.btnCapsLock:
            if self.flagCapsLock == 0:
                for btn in self.listLetterBtn:
                    btn.setText(btn.text().upper())
                self.btnCapsLock.setStyleSheet('background-color : #48D1BC;')
                self.flagCapsLock = 1
            elif self.flagCapsLock == 1:
                for btn in self.listLetterBtn:
                    btn.setText(btn.text().lower())
                self.btnCapsLock.setStyleSheet(self.strStyleSheet)
                self.flagCapsLock = 0

        elif sender == self.btnShift:
            if self.flagShift == 0:
                for btn in self.listLetterBtn:
                    btn.setText(btn.text().upper())
                for btn1 in self.listNumSymbolBtn:
                    textBtn1 = btn1.children()[0].text()[-8]  # text()竟然是'<font size=4 color=black>*</font>'，所以取-8
                    textBtn2 = btn1.children()[1].text()[-8]
                    if textBtn2 == ';':
                        textBtn2 = '&lt;'
                    btn1.children()[0].setText(f'<font size=4>{textBtn1}</font>')
                    btn1.children()[1].setText(f'<font size=4 color=black>{textBtn2}</font>')
                self.btnShift.setStyleSheet('background-color : #48D1BC;')
                self.flagShift = 1
            elif self.flagShift == 1:
                for btn in self.listLetterBtn:
                    btn.setText(btn.text().lower())
                for btn1 in self.listNumSymbolBtn:
                    textBtn1 = btn1.children()[0].text()[-8]  # text()竟然是'<font size=4 color=black>*</font>'，所以取-8
                    textBtn2 = btn1.children()[1].text()[-8]
                    if textBtn2 == ';':
                        textBtn2 = '&lt;'
                    btn1.children()[0].setText(f'<font size=4 color=black>{textBtn1}</font>')
                    btn1.children()[1].setText(f'<font size=4>{textBtn2}</font>')
                self.btnShift.setStyleSheet(self.strStyleSheet)
                self.flagShift = 0

        elif sender in self.listNumSymbolBtn:
            text = sender.children()[0].text()[-8]
            text1 = sender.children()[1].text()[-8]
            if text1 == ';':
                text1 = '<'  # 这里要插入到密码框，不是要显示，所以不能再用'&lt;'
            if self.flagShift == 0:
                self.p.lineEdUserPswd.insert(text)
            elif self.flagShift == 1:
                self.p.lineEdUserPswd.insert(text1)

        elif sender in self.listLetterBtn:
            self.p.lineEdUserPswd.insert(sender.text())

        elif sender == self.btnBackspace:
            self.p.lineEdUserPswd.backspace()  # 删除最后一个字符

        elif sender == self.btnQuit:
            self.close()

    def addLab(self, text, parent):
        """专为btn添加两个lab，处理btn中不能两个字符一个低一个高,btn没有富文本功能"""
        lab = QLabel(parent)
        lab.setGeometry(1, 0, 12, 24)
        lab.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        lab1 = QLabel(f'<font size=4>{text[1]}</font>', parent)  # 虽然可以用上标<sub>3</sub>,但是字太小了，不能改变大小
        lab1.setGeometry(13, 0, 12, 24)
        lab1.setAlignment(Qt.AlignTop)
        lab.setEnabled(False)  # 不设置禁用，按钮点击之后没有回弹效果，并且触发不了点击信号。
        lab.setText(f'<font size=4 color=black>{text[0]}</font>')  # 禁用之后字体颜色会变灰，需设置一下颜色
        lab1.setEnabled(False)
        lab.setStyleSheet('background:transparent')
        lab1.setStyleSheet('background:transparent')

        if text == ',<':  # 符号"<",会被html识别为标签，所以要用实体符号"&lt;"代替
            lab1.setText('<font size=4>&lt;</font>')

    def eventFilter(self, obj, e):
        if e.type() == e.MouseButtonPress or e.type() == e.MouseButtonDblClick:  # 鼠标按下。为了处理menu中点击空白地方会关闭的bug
            if self.flagMouseLeave:  # 当标记为真时，说明鼠标离开了menu
                self.close()
            else:
                return True  # 返回True，拦截关闭事件
        if e.type() == e.Enter:
            self.flagMouseLeave = False
        if e.type() == e.Leave:  # 鼠标离开menu
            self.flagMouseLeave = True
        if e.type() == e.Close:  # 处理menu关闭后，不让密码框获得焦点
            self.p.setFocus()

        return False


class TestGraphicWidget(QGraphicsWidget):
    def __init__(self, parent):
        super(TestGraphicWidget, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)  # Qt.Window  FramelessWindowHint
        self.resize(400, 300)
        self.p = parent

    def closeEvent(self, e):
        self.p.close()


class Login(QDialog, Ui_Login):
    def __init__(self, parent):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.installEventFilter(self)
        self.flagMove = False
        self.labLoginError.hide()  # 账号密码错误提示。提前隐藏。

        # 用遮罩的方法给窗体设置圆角
        self.whiteMask = QBitmap(self.size())  # 创建位图，窗体大小
        self.whiteMask.fill(Qt.white)  # 填充位图全白，相当于把窗口擦掉了，后面再用画刷显示出来。
        p = QPainter(self.whiteMask)
        p.setBrush(QBrush(Qt.black))  # 设置画刷
        p.drawRoundedRect(QRectF(0.0, 0.0, 400, 300), 5.0, 5.0)  # 给矩形添加圆角
        self.setMask(self.whiteMask)  # 设置遮罩

        self.movie = QMovie('UiLogin/image/0-1.gif')
        self.labBg.setMovie(self.movie)
        self.movie.start()
        self.btnMini.clicked.connect(parent.showMinimized)  # 这种才是彻底的关闭所有程序
        self.btnExit.clicked.connect(exit)  # 这种才是彻底的关闭所有程序
        self.btnVipLogin.clicked.connect(lambda: parent.p.isVipLogin(True))
        self.btnVisitorLogin.clicked.connect(lambda: parent.p.isVipLogin(False))

        self.userData = load(open('UserData.json', 'r', encoding='utf-8'))  # 加载用户数据
        # 账号输入下拉列表的设置
        self.comboUserID.setView(QListView())  # 先随便设置一个QListView()，使下拉列表可以设置qss样式
        self.actLeftUserID = QAction(QIcon("UiLogin/image/3.png"), '', self.comboUserID.lineEdit())
        self.comboUserID.lineEdit().addAction(self.actLeftUserID, QLineEdit.LeadingPosition)  # 左侧图标
        self.comboUserID.lineEdit().setPlaceholderText('账号')  # 设置默认提示语
        self.comboUserID.lineEdit().setMaxLength(11)
        self.comboUserID.setIconSize(QSize(40, 40))
        self.comboUserID.lineEdit().setClearButtonEnabled(True)
        self.comboUserID.installEventFilter(self)

        # 密码框的设置
        self.actLeftPswd = QAction(QIcon("UiLogin/image/1.png"), '', self.lineEdUserPswd)
        self.actRightPswd = QAction(QIcon("UiLogin/image/17.png"), '', self.lineEdUserPswd)
        self.actRightPswd.triggered.connect(lambda: self.menuKeyBoard.exec(self.mapToGlobal(QPoint(93, 233))))
        self.menuKeyBoard = MyMenu(self)

        self.lineEdUserPswd.addAction(self.actLeftPswd, QLineEdit.LeadingPosition)  # 左侧图标
        self.lineEdUserPswd.addAction(self.actRightPswd, QLineEdit.TrailingPosition)  # 右侧图标
        self.lineEdUserPswd.installEventFilter(self)

        # 一些控件的信号与槽的绑定
        # self.btnSignIn.clicked.connect(lambda: print('剑灵'))
        self.btnSignIn.clicked.connect(parent.transeformR)

        self.loadUserData()

    def loadUserData(self):
        self.userData = load(open('UserData.json', 'r', encoding='utf-8'))
        for k, v in self.userData.items():
            self.comboUserID.addItem(QIcon(self.getCircularPix(v['头像'])), f"{k}\n{v['昵称']}")
        # 添加完item，下拉列表要设置初始为空，这样item中的icon就不会设置到下拉列表的lineEdit上了
        self.comboUserID.setCurrentIndex(-1)

    @pyqtSlot(str)
    def on_comboUserID_activated(self, text):
        """选择下拉项后，重新设置显示为空项，再改变lineEdit的text"""
        self.comboUserID.setCurrentIndex(-1)  # 下拉列表要设置初始为空，这样item中的icon就不会设置到下拉列表的lineEdit上了
        id, nickname = text.split('\n')  # 添加到item的用户数据都是id+换行+昵称['123', '小明']，如果没有昵称是['123', '']
        self.labUserpic.setStyleSheet(f"border-image: url('image/userPic/{self.userData[id]['头像']}')")
        self.comboUserID.lineEdit().setText(id)  # 自己单独通过下拉列表下的lineEdit设置选择item后显示内容
        if self.userData[id]['记住密码']:
            self.lineEdUserPswd.setText(self.userData[id]['密码'])
            self.cBoxKeepPswd.setChecked(True)
        self.setFocus()

    def getCircularPix(self, userPic):
        """返回一个圆形的QPixmap"""
        size = self.comboUserID.iconSize()
        pixTarget = QPixmap(size)  # 最终图片对象，设置尺寸和控件一样大
        pixTarget.fill(Qt.transparent)  # 最终图片对象背景先填充为透明
        # 加载要画在最终图片对象上的图片，并缩放和控件一样大
        pixBg = QPixmap("image/userPic/" + userPic).scaled(size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        painter = QPainter(pixTarget)
        # 抗锯齿
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        path = QPainterPath()
        path.addRoundedRect(0, 0, size.height(), size.width(), (size / 2).height(), (size / 2).width())  # 画圆形路径
        painter.setClipPath(path)  # 设置QPainter为此路径
        painter.drawPixmap(0, 0, pixBg)  # 在圆形区域内0，0的位置，把加载的图片画上
        return pixTarget

    def eventFilter(self, obj, e):
        if e.type() == e.MouseButtonPress:  # 只为了提前拦截下拉列表总是先进入FocusIn事件
            self.comboUserID.setStyleSheet('font-size:13px;color:#838383;')

        if obj == self:
            if e.type() == e.MouseButtonPress:
                if e.button() == Qt.LeftButton:
                    self.setFocus()  # 主要处理焦点在账号和密码框内时，左键窗口的焦点位置，让输入框失去焦点
                    self.flagMove = True
                    self.posMove = e.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
                    e.accept()
                elif e.button() == Qt.RightButton:  # 如果焦点在密码框里，右键窗口的焦点位置，账号框会得到焦点并全选
                    if self.lineEdUserPswd.hasFocus():
                        self.comboUserID.setFocus()
                        self.comboUserID.lineEdit().selectAll()
            if self.flagMove and e.type() == e.MouseMove:
                self.move(e.globalPos() - self.posMove)  # 更改窗口位置
                e.accept()
            if e.type() == e.MouseButtonRelease:
                self.flagMove = False

        if obj == self.comboUserID:  # 只要点击下拉箭头，总会先进FocusIn再进FocusOut
            if e.type() == e.FocusIn:  # 改变图标，默认字符设置为空，再改变字符尺寸变大和颜色，不然"账号"会变17px,黑色,影响视频效果
                self.actLeftUserID.setIcon(QIcon("UiLogin/image/4.png"))
                self.comboUserID.lineEdit().setPlaceholderText('')
                self.comboUserID.setStyleSheet('font-size:17px;color:black;')
                self.labLoginError.hide()
            # 如果失去焦点，并且下拉列表的ListView事实意义上不是显示的
            if e.type() == e.FocusOut and not self.comboUserID.view().isVisible():  # 恢复图标，恢复默认字符，再恢复字符尺寸变小和颜色
                self.comboUserID.lineEdit().setPlaceholderText('账号')
                self.comboUserID.setStyleSheet('font-size:13px;color:#838383;')
                self.actLeftUserID.setIcon(QIcon("UiLogin/image/3.png"))
            return False

        if obj == self.lineEdUserPswd:  # 改变图标，默认字符设置为空，再改变字符尺寸变大和颜色，就不影响视觉效果了
            if e.type() == e.FocusIn:
                self.actLeftPswd.setIcon(QIcon("UiLogin/image/2.png"))
                self.lineEdUserPswd.setPlaceholderText('')
                self.lineEdUserPswd.setStyleSheet('font-size:16px;color:black;')
                self.labLoginError.hide()
            if e.type() == e.FocusOut:  # 失去焦点：恢复图标，恢复默认字符，再恢复字符尺寸变小和颜色
                self.actLeftPswd.setIcon(QIcon("UiLogin/image/1.png"))
                self.lineEdUserPswd.setPlaceholderText('密码')
                self.lineEdUserPswd.setStyleSheet('font-size:13px;color:#838383;')
            return False
        else:
            return False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)  # 像素光滑
        painter.setRenderHint(QPainter.Antialiasing, True)  # 反锯齿


class Register(QDialog, Ui_Register):
    def __init__(self, parent):
        super(Register, self).__init__(parent)
        self.setupUi(self)
        self.btnBack.clicked.connect(parent.transeformR)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)  # 像素光滑
        painter.setRenderHint(QPainter.Antialiasing, True)  # 反锯齿


class Ui_Login_Logic(QDialog):
    def __init__(self, parent):
        super(Ui_Login_Logic, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.move(QPoint(0, 0))
        self.p = parent
        self.formflag = False
        self.flagMove = False

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(-50, -70, 500, 500)  # 这样界面第一次转换，和第一次打开下拉列表时就不会小幅变动位置

        self.oneWidget = Login(self)  # 创建部件
        self.twoWidget = Register(self)
        self.oneTestWidget = self.scene.addWidget(self.oneWidget)
        self.twoTestWidget = self.scene.addWidget(self.twoWidget)

        self.form = TestGraphicWidget(self)
        self.layout = QGraphicsLinearLayout(self.form)
        self.layout.setSpacing(0)
        self.layout.addItem(self.oneTestWidget)  # 将部件添加到布局管理器中
        self.layout.addItem(self.twoTestWidget)
        self.layout.removeItem(self.twoTestWidget)
        self.twoWidget.hide()

        self.scene.addItem(self.form)

        self.view = QGraphicsView(self.scene, self)
        self.view.setRenderHint(QPainter.Antialiasing)  # 使用抗锯齿的方式渲染
        self.view.setCacheMode(QGraphicsView.CacheBackground)  # 设置缓存背景，这样可以加快渲染速度
        self.view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.view.resize(QApplication.desktop().width(), QApplication.desktop().height())
        self.view.setStyleSheet("background: transparent;border:0px;")
        self.view.setWindowFlags(Qt.FramelessWindowHint)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.move(QPoint(0, 0))

        self.view.children()[0].setMouseTracking(False)  # 它的这个QWidget控件是顶层的，并且默认鼠标监听开启状态
        self.view.children()[0].installEventFilter(self)

    def setWindow(self):
        self.oneWidget.setVisible(self.formflag)
        self.twoWidget.setVisible(not self.formflag)
        if self.formflag:
            self.layout.removeItem(self.twoTestWidget)
            self.layout.addItem(self.oneTestWidget)
        else:
            self.layout.removeItem(self.oneTestWidget)
            self.layout.addItem(self.twoTestWidget)
        self.formflag = not self.formflag
        self.view.update()

    def transeformR(self):
        """有更加简便的写法，在翻牌游戏中的图片旋转"""
        def waitMethod():
            q = QEventLoop()
            t = QTimer()
            t.timeout.connect(q.quit)
            t.start(1)
            q.exec_()
            if t.isActive():
                t.stop()

        r = self.form.boundingRect()
        count = 30
        for i in range(1, count):
            self.form.setTransform(
                QTransform().translate(r.width() / 2, r.height() / 2).rotate(91.00 / count * i - 360 * 1, Qt.YAxis)
                    .translate(-r.width() / 2, -r.height() / 2))
            waitMethod()

        self.form.setTransform(QTransform().translate(r.width() / 2, r.height() / 2).rotate(270 - 360 * 1, Qt.YAxis)
                               .translate(-r.width() / 2, -r.height() / 2))
        self.setWindow()  # 放这效果圆滑多了

        for i in range(1, count):
            self.form.setTransform(
                QTransform().translate(r.width() / 2, r.height() / 2).rotate(270 + 93.00 / count * i - 360 * 1,
                                                                             Qt.YAxis)
                    .translate(-r.width() / 2, -r.height() / 2))
            waitMethod()

        self.view.update()

    def eventFilter(self, obj, e):
        if e.type() == e.MouseButtonPress:  # 只为了提前拦截下拉列表总是先进入FocusIn事件
            self.posMove = e.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            self.flagMove = True
            e.accept()
        if self.flagMove and e.type() == e.MouseMove:
            self.move(e.globalPos() - self.posMove)  # 更改窗口位置
            e.accept()
        if e.type() == e.MouseButtonRelease:
            self.flagMove = False
        return False
