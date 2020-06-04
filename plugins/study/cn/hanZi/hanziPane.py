# -*- coding: utf-8 -*-

"""
-------------------------------------
Created on 2020/4/29 16:59
@author: Teyying
@site: https://github.com/teyying
@email: 165227316@qq.com
-------------------------------------
@file: hanziPane.py
@description:
@problem:
-------------------------------------

"""
from sys import argv, exit
from json import load, dump
from os import getcwd
from os import listdir
from os.path import splitext

from PyQt5.QtCore import QRegExp, QBasicTimer, QTimer
from PyQt5.QtGui import QRegExpValidator, QMovie
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QApplication

from plugins.study.cn.hanzi.resource.hanziUi import Ui_HanZi

import cgitb

cgitb.enable(format='text')


class HanZiPane(QWidget, Ui_HanZi):
    def __init__(self, parent=None):
        super(HanZiPane, self).__init__(parent)
        self.setupUi(self)
        # self.pEventLog = parent.eventLog
        try:
            style = open("resource/hanzi.css", encoding='utf8').read()
        except FileNotFoundError as e:
            style = open("main/resource/hanzi.css", encoding='utf8').read()
        self.setStyleSheet(style)  # qss文件引入

        try:
            self.file = open("plugins\study\cn\hanZi\hanZi.json", encoding='utf8')
        except FileNotFoundError as e:
            self.file = open("hanzi.json", encoding='utf8')
        self.infoHanzi = load(self.file)  # type: dict  # 加载json数据
        self.file.close()

        for k in self.infoHanzi:  # 从Json文件中读取key(汉字)并把每个汉字作为button的text
            self.createButton(k)  # 创建汉字按钮

        self.buttons = dict()
        # imagesPath = "plugins/study/cn/hanzi/images/hanzi"
        self.imagesPath = "resource/images/hanzi"

        self.lineEdit.setValidator(QRegExpValidator(QRegExp("[\u4E00-\u9FA5]+")))  # 正则匹配,只能输入汉字
        self.vbar = self.scrollArea.verticalScrollBar()
        self.timer = QBasicTimer()  # 初始化一个定时器,用于滚动条自动滚动

    # 创建汉字按钮
    def createButton(self, text: str):
        btn = QPushButton(text)
        btn.setFixedSize(100, 100)
        btn.clicked.connect(self.slot_btns_hanzi)

        count = self.gridLeft.count()
        row = count // 5  # 行索引，其实就是整除的值
        column = count % 5  # 列索引，其实就是余数（remainder）
        self.gridLeft.addWidget(btn, row, column)

    def slot_btns_hanzi(self):
        """让指定的QLabel显示gif图片,还有一个线程,线程是符合条件启动的"""
        text = self.sender().text()
        movie = QMovie(f"{self.imagesPath}/{text}.gif")  # 显示笔画演示GIF
        self.labGif.setMovie(movie)
        movie.setSpeed(180)  # 设置播放速度,原始速度有点慢
        movie.start()
        # 显示拼音
        self.labPinYin.setText(self.infoHanzi[text][0])

        if self.checkBox.checkState():  # 复选框被选择时,状态是2,没被选择时,状态是0
            # 用线程来语音读汉字(为线程写一个函数),不然每次点击读汉字时,笔画演示就会顿一下
            from threading import Thread
            t = Thread(target=self.threadVoice, args=(text,))  # 传的参数必须加逗号
            t.setDaemon(True)
            t.start()

    # 调用Win语音引擎
    def threadVoice(self, btnText):
        """
        用线程来语音读汉字,不然每次点击读汉字时,笔画演示就会顿一下
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

    # 添加汉字按钮
    def appendText(self):
        text = self.lineEdit.text().strip()  # type: str
        if not text:
            QMessageBox.information(self, f"提示", f"请输入要添加的汉字", QMessageBox.Ok)
            return

        self.vbar.setValue(self.scrollArea.maximumHeight())  # 把滚动条定位到底部，直观的看清楚添加和删除的汉字的
        reply = QMessageBox.question(self, f"{text}汉字", f"确定要{text}汉字[{text}]吗?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            existingText = set(self.infoHanzi.keys()) & set(text)  # json数据存在的汉字
            wantToAddText = set(text) - existingText  # 想要添加的汉字

            filenames = set(listdir("resource/images/hanzi"))  # 已经存在的gif文件名
            newFilenames = set(f'{i}.gif' for i in wantToAddText)  # 给每一个字符添加扩展名(方便进行交集计算)
            # 已经存在的gif汉字图片,但是没有笔画、拼音等其它信息，只需要爬取gif以外的信息(删除汉字时，只会删除其它信息数据，并不会删除gif图片)
            self.existingName = filenames & newFilenames  # 算出交集

            self.crawl(newFilenames)  # 调用写好的方法爬取汉字gif笔画演示图片
            # self.crawl(wantToAddText)  # 调用写好的方法爬取汉字gif笔画演示图片
            # 树睡拿屡喽垃圾
            QMessageBox.information(self, f"提示", f"添加成功：{wantToAddText},\n数据中已有的汉字：{existingText}。", QMessageBox.Ok)

    # 删除汉字按钮
    def removeText(self):
        text = self.lineEdit.text()  # type: str
        nonexistentText = set()
        deletedText = set()
        for s in text:
            if s in self.btns:  # 有此汉字时删除
                self.btns[s].deleteLater()
                del self.btns[s], self.infoHanzi[s]  # 删除数据
                deletedText.add(s)
            else:
                nonexistentText.add(s)
        # 删除完数据，重新写入json文件
        dump(self.infoHanzi, open(self.file.name, 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
        QMessageBox.information(self, f"提示", f"删除成功：{deletedText},\n数据中没有的汉字：{nonexistentText}", QMessageBox.Ok)

    # 爬取汉字数据
    def crawl(self, text: set):
        from requests import get
        from re import findall, S

        for filename in text:
            s = filename[0]
            print(s, '1111111111111111111')
            url = f'https://hanyu.baidu.com/zici/s?wd={s}&from=zici'
            # url = f'https://hanyu.baidu.com/zici/s?wd=垃&from=zici'
            response = get(url)  # html = response.text.encode('utf8','ignore')
            html = response.content.decode('utf8', 'ignore')  # 直接html = response.text出现中文乱码，取不出带声调的拼音
            # read_mp3 = findall(r'herf="#" url="(.*?)"', html, S)[0] # 读音MP3下载地址
            bihua_str = findall(r'id="stroke_count">(.*?)/span>', html, S)[0]  # 笔画数
            bihua_str = findall(r'<span>(.*?)<', bihua_str, S)[0]
            pinyin_str = findall(r'id="pinyin">(.*?)/b>', html, S)[0]
            pinyin_str = findall(r'<b>(.*?)<', pinyin_str, S)[0]  # 带声调的拼音
            if filename not in self.existingName:
                gif_url = findall(r'data-gif="(.*?)"', html, S)[0]  # 得到gif图片地址
                gif = get(gif_url)
                gif_wbdate = gif.content  # 二进制数据

                with open(f'{self.imagesPath}/{filename}', 'wb') as f:
                    f.write(gif_wbdate)  # 把下载的二进制数据写入文件并保存（保存爬取的的图片）
            self.infoHanzi[s] = [pinyin_str, bihua_str]
            self.createButton(s)
        dump(self.infoHanzi, open(self.file.name, 'w', encoding='utf-8'), indent=4, ensure_ascii=False)

    def timerEvent(self, e):
        """滚动条自动滚动的计时器"""
        self.vbar.setValue(self.vbar.value() + 10)  # 每次滚动10像素
        if self.vbar.value() == self.vbar.maximum():
            self.btnStart.setText('开始滚动')
            self.timer.stop()


if __name__ == '__main__':
    app = QApplication(argv)
    window = HanZiPane()
    window.show()
    exit(app.exec_())
