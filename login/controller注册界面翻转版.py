# -*- coding: utf-8 -*-

"""
-------------------------------------
Created on 2020/4/4 20:01
@author: Teyying
@site: https://github.com/teyying
@email: 165227316@qq.com
-------------------------------------
@file: controller注册界面翻转版.py
@description:
@problem:
-------------------------------------

"""
from sys import argv, exit
from PyQt5.Qt import *
import cgitb

from login.accountItemPane import AccountItemPane
from login.keyboardPane import KeyboardPane
from login.loginPane import LoginPane
from login.registerPane import RegisterPane

cgitb.enable(format='text')


# todo 槽函数是否都加上slot，以及加上"__"私有方法
# todo 怎么取得comboBox 划过item时的信号，不知怎么得到此item
class Window(QGraphicsView):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setRenderHint(QPainter.SmoothPixmapTransform, True)  # 像素光滑
        self.setRenderHint(QPainter.Antialiasing)  # 使用抗锯齿的方式渲染
        self.setCacheMode(QGraphicsView.CacheBackground)  # 设置缓存背景，这样可以加快渲染速度
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.resize(QApplication.desktop().size())  # 设置view为系统桌面尺寸
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)  # 设置左上角对齐
        self.setStyleSheet("QGraphicsView {background: transparent;}")
        self.setupUi()

    def setupUi(self):
        # 实例化界面
        self.loginPane = LoginPane()
        self.registerPane = RegisterPane()

        # 设置场景，添加QGraphicsWidget元素，并在QGraphicsWidget设置QGraphicsLinearLayout布局，然后在
        # QGraphicsLinearLayout布局中添加登录和注册界面。这样就可以通过旋转QGraphicsWidget来达到登录界面
        # 以旋转的方式跳转到注册界面的效果
        self.scene = QGraphicsScene(self)
        # 如果QWidget没有设置固定大小，就设置QGraphicsWidget的
        self.graphicWidget = QGraphicsWidget()  # QGraphicsWidget继承自QGraphicsItem
        self.graphicWidget.setFlag(QGraphicsItem.ItemIsMovable)  # 设置可拖动，就实现界面移动效果了
        self.layout = QGraphicsLinearLayout(self.graphicWidget)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)  # 默认有10px
        self.layout.addItem(self.scene.addWidget(self.loginPane))  # 将部件添加到布局管理器中
        self.layout.addItem(self.scene.addWidget(self.registerPane))
        self.registerPane.hide()
        # self.scene.setSceneRect(-(self.width() / 2 - self.loginPane.width() / 2),
        #                         -(self.height() / 2 - self.loginPane.height() / 2), self.width(), self.height())
        self.setSceneRect(QRectF(self.rect()))  # 这两行处理居中显示。也可以用上一行注释掉方法的解决
        self.graphicWidget.setPos((self.width() / 2 - self.loginPane.width() / 2),
                                  (self.height() / 2 - self.loginPane.height() / 2))
        self.scene.addItem(self.graphicWidget)
        self.setScene(self.scene)
        self.loginPane.comboAccount.setFocus()  # 账号控件设置焦点后，登录界面的自定义信号

        # 用遮罩的方法给窗体设置圆角
        whiteMask = QBitmap(self.size())  # 创建位图，窗体大小
        whiteMask.fill(Qt.white)  # 填充位图全白，相当于把窗口擦掉了，后面再用黑色画刷显示出来。
        self.p = QPainter(whiteMask)
        self.p.setBrush(QBrush(Qt.black))  # 设置画刷
        self.p.drawRoundedRect(QRectF(0.0, 0.0, 400, 300), 5.0, 5.0)  # 给矩形添加圆角
        self.loginPane.setMask(whiteMask)  # 设置遮罩
        self.registerPane.setMask(whiteMask)  # 设置遮罩

        # 信号与槽设置
        self.registerPane.exitSignal.connect(self.transeformR)
        self.loginPane.showRegisterPaneSignal.connect(self.transeformR)
        self.loginPane.showKeyboardPaneSignal.connect(self.showKeyboardPane)
        self.loginPane.btnExit.clicked.connect(self.close)
        self.loginPane.checkLoginSignal.connect(self.fn)

        self.loginPane.addAccountItemSignal.emit(AccountItemPane(QPixmap(), '悄好', '123215221'))
        self.loginPane.addAccountItemSignal.emit(AccountItemPane(QPixmap(), '悄321好', '215221'))
        self.loginPane.addAccountItemSignal.emit(AccountItemPane(QPixmap(), '悄555好', '1232'))

    def fn(self, account, password):
        print(account, password)

    def showKeyboardPane(self):
        self.keyboardPane = KeyboardPane()
        self.keyboardPane.delPreStrSignal.connect(self.loginPane.lePassword.backspace)
        self.keyboardPane.insertCharSignal[str].connect(lambda s: self.loginPane.lePassword.insert(s))
        self.keyboardPane.move(QPoint(self.loginPane.cursor().pos().x() - 300, self.loginPane.cursor().pos().y() + 25))
        self.keyboardPane.show()

    def transeformR(self):
        """有更加简便的写法，在翻牌游戏中的图片旋转"""
        self.sender().blockSignals(True)  # 暂时阻止接收信号，旋转完成后再恢复接收。处理快速多次点击时，会重复旋转界面
        self.loginPane.setDisabled(True)  # 设置禁用状态为True,防止旋转时去移动窗口
        self.registerPane.setDisabled(True)
        self.setFocus()

        def waitMethod():
            q = QEventLoop()
            t = QTimer()
            t.timeout.connect(q.quit)
            t.start(1)
            q.exec_()
            if t.isActive():
                t.stop()

        r = self.graphicWidget.boundingRect()
        count = 30
        for i in range(1, count):
            self.graphicWidget.setTransform(
                QTransform().translate(r.width() / 2, r.height() / 2).rotate(91.00 / count * i - 360 * 1, Qt.YAxis)
                    .translate(-r.width() / 2, -r.height() / 2))
            waitMethod()

        self.graphicWidget.setTransform(
            QTransform().translate(r.width() / 2, r.height() / 2).rotate(270 - 360 * 1, Qt.YAxis)
                .translate(-r.width() / 2, -r.height() / 2))

        self.loginPane.setVisible(not self.loginPane.isVisible())
        self.registerPane.setVisible(not self.registerPane.isVisible())

        for i in range(1, count):
            self.graphicWidget.setTransform(
                QTransform().translate(r.width() / 2, r.height() / 2).rotate(270 + 93.00 / count * i - 360 * 1,
                                                                             Qt.YAxis)
                    .translate(-r.width() / 2, -r.height() / 2))
            waitMethod()

        self.sender().blockSignals(False)  # 恢复接收信号
        self.loginPane.setDisabled(False)
        self.registerPane.setDisabled(False)


if __name__ == '__main__':
    app = QApplication(argv)
    window = Window()
    window.show()
    exit(app.exec_())
