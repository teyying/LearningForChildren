from PyQt5.QtCore import Qt, QRectF, pyqtSlot
from PyQt5.QtGui import QBitmap, QPainter, QBrush, QCursor
from PyQt5.QtWidgets import QDialog, QWidget

from UiMain.Ui_DialogChoose import Ui_DialogChoose


class Ui_DialogChoose_Logic(QDialog, Ui_DialogChoose):
    def __init__(self):
        super(Ui_DialogChoose_Logic, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏标题栏
        self.flag = False
        self.flagMove = False

        # 用遮罩的方法给窗体设置圆角
        self.whiteMask = QBitmap(self.size())  # 创建位图，窗体大小
        self.whiteMask.fill(Qt.white)  # 填充位图全白，相当于把窗口擦掉了，后面再用画刷显示出来。
        p = QPainter(self.whiteMask)
        brush = QBrush(Qt.black)  # 创建画刷并设置成黑色，这样黑色区域内的窗口就显示出来了。
        p.setBrush(brush)  # 设置画刷
        rectF = QRectF(0.0, 0.0, 400, 200)  # 画一个矩形
        p.drawRoundedRect(rectF, 5.0, 5.0)  # 给矩形添加圆角
        self.setMask(self.whiteMask)  # 设置遮罩

    def setInfo(self, parent, title, info):
        # 为了突出显示此弹窗，让主界面背景变暗，创建了一个新QWidget继承主界面，模态弹窗exec方法后面，再删除掉此widget
        self.widTemp = QWidget(parent)
        self.widTemp.resize(parent.size())
        self.widTemp.setStyleSheet('background-color:rgba(0, 0, 0, 100);')
        self.widTemp.show()
        self.label_2.setText(title)
        self.label.setText(info)  # 设置显示信息
        self.setStyleSheet('QWidget#DialogChoose {border-image: url("UiMain/image/dialogChoose.png");}\n'
                           'QPushButton {border-radius:5px;background:rgba(255,255,255,150);}\n'
                           'QPushButton:hover {background:rgba(255,255,255,200);}\n'
                           'QPushButton:pressed {margin-left:5px;margin-top:5px;}')
        self.exec()
        self.widTemp.deleteLater()  # exec()方法后，删除掉刚创建的QWidget
        return self.flag

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.flag = True
        self.close()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.flagMove = True
            self.m_Position = e.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            e.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, e):
        if Qt.LeftButton and self.flagMove:
            self.move(e.globalPos() - self.m_Position)  # 更改窗口位置
            e.accept()

    def mouseReleaseEvent(self, e):
        self.flagMove = False
        self.setCursor(QCursor(Qt.CustomCursor))  # 更改鼠标图标为系统默认