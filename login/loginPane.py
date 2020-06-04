# -*- coding: utf-8 -*-

"""
-------------------------------------
Created on 2020/4/3 16:47
@author: Teyying
@site: https://github.com/teyying
@email: 165227316@qq.com
-------------------------------------
@file: loginPane.py
@description:
@problem:
-------------------------------------

"""

from sys import argv, exit
from PyQt5.Qt import *
from login.resource.loginUi import Ui_Form

import cgitb

cgitb.enable(format='text')


class LoginPane(QLabel, Ui_Form):
    checkLoginSignal = pyqtSignal(str, str)
    showRegisterPaneSignal = pyqtSignal()
    showKeyboardPaneSignal = pyqtSignal()
    returnPressedSignal = pyqtSignal()  # 这个信号连接了登录的click方法，在QtDesigner设置好的
    addAccountItemSignal = pyqtSignal(QWidget)

    def __init__(self):
        super(LoginPane, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)

        # 用遮罩的方法给窗体设置圆角
        whiteMask = QBitmap(self.size())  # 创建位图，窗体大小
        whiteMask.fill(Qt.white)  # 填充位图全白，相当于把窗口擦掉了，后面再用黑色画刷显示出来。
        self.p = QPainter(whiteMask)
        self.p.setRenderHint(QPainter.Antialiasing)  # 使用抗锯齿的方式渲染
        self.p.setBrush(QBrush(Qt.black))  # 设置画刷
        self.p.drawRoundedRect(QRectF(0.0, 0.0, self.width(), self.height()), 5.0, 5.0)  # 给矩形添加圆角
        self.setMask(whiteMask)  # 设置遮罩

        # 添加阴影
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # shadowEffect = QGraphicsDropShadowEffect(self)
        # shadowEffect.setColor(Qt.red)
        # # 阴影的大小(要和self的水平布局边距对应)
        # shadowEffect.setBlurRadius(15)
        # shadowEffect.setOffset(0, 0)
        # self.setGraphicsEffect(shadowEffect)
        try:
            style = open("resource/login.css", encoding='utf8').read()
        except FileNotFoundError as e:
            style = open("login/resource/login.css", encoding='utf8').read()

        self.setStyleSheet(style)  # qss文件引入
        # self.setStyleSheet(open("resource/login.css", encoding='utf8').read())  # qss文件引入
        self.setUserAvatar(QPixmap(":/login/images/login_icon_user_avatar.png"))
        self.loadGifBackGround()
        self.checkForNull()
        self.flagMove = False

    def setupUi(self, Form):
        """继承Ui_Form的setupUi方法，并在此方法内添加界面控件"""
        super().setupUi(Form)
        # 密码框的设置（账号输入下拉列表的设置在comboBox文件中)
        path = ":/login/images/login_icon_password_left_normal.png"
        self.lePassword.addAction(QAction(QIcon(path), '', self), QLineEdit.LeadingPosition)  # 左侧图标
        icon = QIcon()
        icon.addPixmap(QPixmap(":/login/images/login_icon_password_right_normal.png"), QIcon.Normal, QIcon.Off)
        icon.addPixmap(QPixmap(":/login/images/login_icon_password_right_active.png"), QIcon.Active, QIcon.Off)
        self.actPasswordRight = QAction(icon, '', self)
        self.actPasswordRight.triggered.connect(self.showKeyboardPaneSignal)
        self.lePassword.addAction(self.actPasswordRight, QLineEdit.TrailingPosition)  # 右侧图标
        self.lePassword.installEventFilter(self)

        # 信号与槽设置
        self.addAccountItemSignal[QWidget].connect(lambda a: self.comboAccount.addAcountItem(a))

    def showRegisterPane(self):
        self.showRegisterPaneSignal.emit()

    def inserPassword(self, s):
        self.lePassword.insert(s)

    def checkForNull(self):
        if self.comboAccount.currentText() and self.lePassword.text():
            self.btnLogin.setDisabled(False)
        else:
            self.btnLogin.setDisabled(True)

    def checkLogin(self):
        account = self.comboAccount.currentText()
        password = self.lePassword.text()
        self.checkLoginSignal.emit(account, password)

    def setUserAvatar(self, pixmap):
        self.labUserAvatar.setScaledContents(True)  # 可以在设计师中设置
        self.labUserAvatar.setPixmap(pixmap)

    def loadGifBackGround(self):
        # try:
        #     path = open("resource/login.css", encoding='utf8').read()
        # except FileNotFoundError as e:
        #     path = open("login/resource/login.css", encoding='utf8').read()

        movie = QMovie(':/login/images/login_bg.gif')
        movie.setParent(self)
        movie.setScaledSize(QSize(self.width(), 110))
        self.setAlignment(Qt.AlignTop)
        self.setMovie(movie)
        movie.start()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter:
            self.returnPressedSignal.emit()
        return super().keyPressEvent(e)

    def mousePressEvent(self, e):
        # print(self.signalsBlocked())
        if e.button() == Qt.LeftButton:
            self.setFocus()  # 主要处理焦点在账号和密码框内时，左键窗口的焦点位置，让输入框失去焦点
            self.flagMove = True
            self.posMove = e.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            e.accept()
        elif e.button() == Qt.RightButton:  # 如果焦点在密码框里，右键窗口的焦点位置，账号框会得到焦点并全选
            if self.lePassword.hasFocus():
                self.comboAccount.setFocus()
                self.comboAccount.lineEdit().selectAll()

    def mouseMoveEvent(self, e):
        if Qt.LeftButton and self.flagMove:
            self.move(e.globalPos() - self.posMove)  # 更改窗口位置
            e.accept()

    def mouseReleaseEvent(self, e):
        self.flagMove = False

    def eventFilter(self, obj, e):
        if obj == self.lePassword:
            if e.type() == e.FocusIn:
                path = ":/login/images/login_icon_password_left_hover.png"
                self.lePassword.actions()[0].setIcon(QIcon(path))
            elif e.type() == e.FocusOut:
                path = ":/login/images/login_icon_password_left_normal.png"
                self.lePassword.actions()[0].setIcon(QIcon(path))
        return False

    def closeEvent(self, *args, **kwargs):
        self.deleteLater()

if __name__ == '__main__':
    app = QApplication(argv)
    window = LoginPane()
    window.show()
    exit(app.exec_())
