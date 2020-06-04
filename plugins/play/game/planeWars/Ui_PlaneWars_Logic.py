import cgitb
from random import choice
from sys import argv
from PyQt5.Qt import *
from PyQt5.QtCore import *
cgitb.enable(format='text')
from UiGames.UiPlaneWars.Ui_PlaneWars import Ui_PlaneWars



class Item(QGraphicsItem):
    def __init__(self, picPath='1.png'):
        super(Item, self).__init__()
        self.picPath = picPath
        self.x = choice(range(480))
        self.flag = 0


        # self.timer = QTimer()
        # self.timer.timeout.connect(self.slot_timer)  # QObject
        # self.timer.start(1000)
        #
        # self.t = QThread()
        # self.t.started.connect(lambda: self.timer.start(100))
        # self.t.finished.connect(self.t.deleteLater)
        # self.t.start()

    # def slot_timer(self):
    #     # self.moveBy(-20, 0)
    #     self.flag += 1
    #     self.update()
        # propertyName, duration, startValue, endValue = 'moveBy', 6000, (770, 304, 0, 0), (570, 104, 408, 408)
        # animation = QPropertyAnimation(self, propertyName.encode('ascii'), self)
    #     animation.setDuration(duration)
    #     animation.setStartValue(QRect(*startValue))
    #     animation.setKeyValueAt(0.2, QRect(*endValue))
    #     animation.setKeyValueAt(0.9, QRect(*endValue))
    #     animation.setEndValue(QRect(*startValue))
    #     animation.start(animation.DeleteWhenStopped)  # 动画结束后进行自清理

    def paint(self, painter, option, widget=None):
        painter.drawPixmap(940, self.x, 40, 40, QPixmap(self.picPath))

    def boundingRect(self):
        return QRectF(940, self.x, 40, 40)

class Ui_PlaneWars_Logic(QGraphicsView):
    def __init__(self):
        super(Ui_PlaneWars_Logic, self).__init__()
        self.resize(980, 520)
        self.setRenderHint(QPainter.Antialiasing)  # 使用抗锯齿的方式渲染
        self.setCacheMode(QGraphicsView.CacheBackground)  # 设置缓存背景，这样可以加快渲染速度
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)

        self.flag = True
        self.myScene = QGraphicsScene(self)
        self.myScene.setSceneRect(QRectF(self.rect()))  # 这样item的坐标0，0就在view左上角
        self.setScene(self.myScene)
        self.listItem = []
        self.itemGroup = QGraphicsItemGroup()
        self.myScene.addItem(self.itemGroup)
        for i in  range(5):
            enemy = Item()
            self.listItem.append(enemy)
            self.myScene.addItem(enemy)
            self.itemGroup.addToGroup(enemy)
        self.startTimer(0, Qt.VeryCoarseTimer)

    # def paintEvent(self, e):
    #     super().paintEvent(e)
        # self.itemGroup.moveBy(-10, 0)


    def timerEvent(self, e):
        self.itemGroup.moveBy(-100, 0)
        # for i in self.listItem:
        #     i.moveBy(-10, 0)


if __name__ == '__main__':
    app = QApplication(argv)
    window = Ui_PlaneWars_Logic()  # 实例化主窗口
    window.show()
    exit(app.exec_())