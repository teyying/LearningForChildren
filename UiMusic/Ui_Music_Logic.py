from sys import argv
from PyQt5.Qt import *
from PyQt5.QtCore import QUrl

from UiMusic.Ui_Music import Ui_Music


class Ui_Music_Logic(QWidget, Ui_Music):
    def __init__(self):
        super(Ui_Music_Logic, self).__init__()
        self.setupUi(self)
        self.player = QMediaPlayer()  # 必须实例化。下载了解码器，不知道是否真的需要。

        [btn.clicked.connect(self.slot_btns) for btn in self.widget.children()[1:]]

    def slot_btns(self):
        toolTip = self.sender().toolTip()
        if toolTip == '播放':
            self.sender().setToolTip('暂停')
            url = QUrl.fromLocalFile("1.mp3")
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        elif toolTip == '暂停':
            self.sender().setToolTip('播放')
            self.player.stop()


if __name__ == '__main__':
    app = QApplication(argv)
    window = Ui_Music_Logic()  # 实例化主窗口
    window.show()
    exit(app.exec_())