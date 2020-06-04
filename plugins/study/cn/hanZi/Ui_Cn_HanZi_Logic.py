from json import load, dump
from os import getcwd

from PyQt5.QtCore import QRegExp, QBasicTimer
from PyQt5.QtGui import QRegExpValidator, QMovie
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox

from UiCn.UiHanZi.Ui_Cn_HanZi import Ui_Cn_HanZi


class UiCn_HanZi_Logic(QWidget, Ui_Cn_HanZi):
    def __init__(self, parent):
        super(UiCn_HanZi_Logic, self).__init__(parent.widCenter)
        self.setupUi(self)
        self.pEventLog = parent.eventLog

        self.scrollArea.setStyleSheet('background:transparent;')  # 在这里可以直接把它的子控件也透明了（vbar)
        # 从Json文件中读取key(汉字)并把每个汉字作为button的text
        self.dataHanZi = load(open('cn/hanzi/hanzi.json', 'r', encoding='utf-8'))
        self.loadBtnsHanZi()  # 加载汉字按钮

        self.lineEdit.setValidator(QRegExpValidator(QRegExp("[\u4E00-\u9FA5]+")))  # 正则匹配,只能输入汉字
        [b.clicked.connect(self.slot_btns_widRight) for b in self.widRight.children() if isinstance(b, QPushButton)]
        self.vbar = self.scrollArea.verticalScrollBar()
        self.timer = QBasicTimer()  # 初始化一个定时器,用于滚动条自动滚动

    def loadBtnsHanZi(self, delBtn=False):
        """加载汉字按钮"""
        if delBtn:  # 因为不会其它更新数据的方法，只能用这种方法解决每次添加删除汉字实时显示
            from sip import delete
            for btn in self.widLeftScrollArea.children()[1:]:
                self.gridLeft.removeWidget(btn)  # 删除控件,并用sip库中的delete方法再删除一次才能把btn全清除
                delete(btn)
        row = 0
        column = 0
        for hanzi in self.dataHanZi:
            btn = QPushButton(hanzi)
            btn.setFixedSize(100, 100)
            btn.clicked.connect(self.slot_btns_hanzi)  # 用偏函数方法,不然所有按钮text会设置为最后一个字
            self.gridLeft.addWidget(btn, row, column)
            column += 1
            if column == 5:
                row += 1
                column = 0

    def slot_btns_hanzi(self):
        """让指定的QLabel显示gif图片,还有一个线程,线程是符合条件启动的"""
        text = self.sender().text()
        movie = QMovie(f"cn/hanzi/images/hanzi/{text}.gif")  # 显示笔画演示GIF
        self.labGif.setMovie(movie)
        movie.setSpeed(180)  # 设置播放速度,原始速度有点慢
        movie.start()
        # 显示拼音
        self.labPinYin.setText(self.dataHanZi[text][0])

        if self.checkBox.checkState():  # 复选框被选择时,状态是2,没被选择时,状态是0
            # 用线程来语音读汉字(为线程写一个函数),不然每次点击读汉字时,笔画演示就会顿一下
            from threading import Thread
            t = Thread(target=self.threadVoice, args=(text,))  # 传的参数必须加逗号
            t.setDaemon(True)
            t.start()

    def threadVoice(self, btnText):
        """
        此函数是self.connect函数里面的线程,用线程来语音读汉字,不然每次点击读汉字时,笔画演示就会顿一下
        需要下载pywin32模块
        """
        from win32com.client import Dispatch
        speaker = Dispatch("SAPI.SpVoice")  # 语音引擎
        speaker.Speak(btnText)

    def slot_btns_widRight(self):
        """
        首页,自动滚动以及增删汉字的槽函数.上下页的逻辑处理不用深究了,因为滚动条内带button元素,本就不适合上下翻页,
        文本框里的大篇文章倒是适合
        """
        text = self.sender().text()
        if text == '首页':
            self.timer.stop()  # 计时器停止
            self.scrollArea.verticalScrollBar().setValue(0)  # 滚动条回到最上面
            self.btnStart.setText('开始滚动')  # 为已经点击开始滚动按钮变为暂停滚动而添加这一行代码,这样恢复为开始
            # 滚动后,再点击时,就可以从头开始了,不然滚动条会接着上一次的位置滚动
        elif text in ('开始滚动', '暂停滚动', '继续滚动'):
            if text == '开始滚动':
                self.btnStart.setText('暂停滚动')
                self.timer.start(500, self)  # 计时器启动,时间速度为1秒
            elif text == '暂停滚动':
                self.timer.stop()
                self.btnStart.setText('继续滚动')
            elif text == '继续滚动':
                self.btnStart.setText('暂停滚动')
                self.timer.start(500, self)  # 计时器启动,时间速度为0.5秒

        elif text in ('添加', '删除'):
            getText = self.lineEdit.text()
            self.vbar.setValue(self.scrollArea.maximumHeight())  # 把滚动条定位到底部，直观的看清楚添加和删除的汉字的

            if getText:
                reply = QMessageBox.question(self, f"{text}汉字", f"你确定要{text}汉字[{getText}]吗?",
                                             QMessageBox.Yes | QMessageBox.No)
                if reply == 65536:  # 或者QMessageBox.Yes.经测试,选择yes返回16384,选择no返回65536
                    return  # 如果选择no,直接返回,否则执行下面代码

                self.successful = ''
                self.failed = ''
                if text == '添加':  # 没有此汉字时添加
                    self.crawlGif(getText)  # 调用写好的方法爬取汉字gif笔画演示图片
                elif text == '删除':
                    for i in getText:
                        if i in self.dataHanZi.keys():  # 有此汉字时删除
                            del self.dataHanZi[i]  # 删除数据
                            self.successful += i  # 因为只能点击一个按钮添加或删除,所以这变量不会在删除里同时执行+=i
                        else:
                            self.failed += i
                    # 删除完数据，重新写入json文件
                    dump(self.dataHanZi, open('cn/hanzi/hanzi.json', 'w', encoding='utf-8'), indent=4,
                         ensure_ascii=False)

                self.loadBtnsHanZi(True)  # 添加删除完汉字,重载一下界面
                QMessageBox.information(self, f"提示", f"[{self.successful}]\n{text}成功,\n\n[{self.failed}]\n{text}失败.",
                                        QMessageBox.Ok)

    def timerEvent(self, e):
        """滚动条自动滚动的计时器"""
        self.vbar.setValue(self.vbar.value() + 10)  # 每次滚动10像素
        if self.vbar.value() == self.vbar.maximum():
            self.btnStart.setText('开始滚动')
            self.timer.stop()

    def crawlGif(self, _str):
        '''
        爬取笔画演示的gif图片，以及拼音字母和笔画数
        :param _str: 要爬取笔画演示gif图片的字符串
        :return: 保存爬取的的图片在image/hanzi文件夹内
        '''
        from os import listdir
        from requests import get
        from re import findall, S
        listGif = listdir('cn/hanzi/images/hanzi')
        tempData = {}
        try:
            for i in _str:
                fileName = f'{i}.gif'
                if fileName not in listGif or i not in self.dataHanZi.keys():  # 如果gif图片和字符串数据都没有
                    url = f'https://hanyu.baidu.com/zici/s?wd={i}&from=zici'
                    response = get(url)  # html = response.text.encode('utf8','ignore')
                    html = response.content.decode('utf8', 'ignore')  # 直接html = response.text出现中文乱码，取不出带声调的拼音
                    # read_mp3 = findall(r'herf="#" url="(.*?)"', html, S)[0] # 读音MP3下载地址
                    bihua_str = findall(r'id="stroke_count">(.*?)/span>', html, S)[0]  # 笔画数
                    bihua_str = findall(r'<span>(.*?)<', bihua_str, S)[0]
                    pinyin_str = findall(r'id="pinyin">(.*?)/b>', html, S)[0]
                    pinyin_str = findall(r'<b>(.*?)<', pinyin_str, S)[0]  # 带声调的拼音
                    tempData[i] = [pinyin_str, bihua_str]
                    self.dataHanZi.update(tempData)  # 防止重复爬取已有数据
                    self.successful += i
                    # self.temp(i)
                    # 如果以前添加过此汉字并删除，不会删除gif图片,添加时如果在image目录中就不再爬取了
                    if fileName not in listGif:
                        gif_url = findall(r'data-gif="(.*?)"', html, S)[0]  # 得到gif图片地址
                        gif = get(gif_url)
                        gif_wbdate = gif.content  # 二进制数据
                        open(f'cn/hanzi/images/hanzi/{fileName}', 'wb').write(gif_wbdate)  # 把下载的gif放进文件夹内
                        listGif.append(fileName)  # 防止重复爬取已有数据
                else:
                    self.failed += i
            if tempData != {}:  # 重写json数据
                dump(self.dataHanZi, open('cn/hanzi/hanzi.json', 'w', encoding='utf-8'), indent=4,
                     ensure_ascii=False)
        except Exception as e:
            self.mainEventLog([f"{getcwd()}\\cn\\hanzi\\UiCn_HanZi_Logic.py >>>UiCn_HanZi_Logic.crawlGif", e])
