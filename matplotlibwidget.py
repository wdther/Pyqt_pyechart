import sys
import os.path
import random
import matplotlib

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
import PyQt5.sip
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import jieba
import jieba.posseg as psg
from wordcloud import wordcloud, ImageColorGenerator
import imageio
import numpy as np

#计算方法类，没有创建fig对象，便于统一
class barchart():
    # def __init__(self, parent=None):
    #

    def wordfreq(self,content): #content open().read() 得到的文件
        #分离出感兴趣的名词，放在 lst_words 里
        lst_words = []
        for x in psg.cut(content):
            # 保留名词、人名、地名，长度至少两个字
            if x.flag in ['n', 'nr', 'ns'] and len(x.word) > 1:
                lst_words.append(x.word)
        word_frequency = {}
        for word in lst_words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

        word_sort = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
        return word_sort  #得到词频列表

    def wordfreqsum(self,txtfile):
        #txtfile = "./text/我的孤独是一座花园.txt"
        (filepath, tempfilename) = os.path.split(txtfile)
        (filename, extension) = os.path.splitext(tempfilename)

        self.title=filename
        txt = open(txtfile, encoding='UTF-8').read()
        wf=self.wordfreq(txt)

        #提取前十个频率
        wf=wf[0:10]

        self.wfreq=dict(wf) #利用dict关键字，创建一个字典对象dict(wf)


        self.labels=[]
        self.nums=[]
        for i in range(0,10):

            self.nums.append(wf[i][1])
            self.labels.append(wf[i][0])

class MyMplCanvas(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""

    def __init__(self, parent=None):
        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        # self.fig, self.axes = plt.subplots(1, 1)
        # self.fig.figsize=(900,760)

        self.fig = plt.figure(figsize=(7.8, 7.6), dpi=100)
        self.fig.set_tight_layout(True)

        self.axes = self.fig.add_subplot(111)
        # self.axes.set_axis_off()

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def autolabel(self,rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            self.axes.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    def plotchart(self,labels,nums,title):
        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars
        rects1 = self.axes.bar(x - width / 2, nums, width, label=title,color='teal')

        self.autolabel(rects1)


        # Add some text for labels, title and custom x-axis tick labels, etc.
        self.axes.set_ylabel('词频')
        self.axes.set_title('词频前十名')
        self.axes.set_xticks(x)
        self.axes.set_xticklabels(labels)
        self.axes.legend()
        self.fig.tight_layout()

        self.draw()

    def wordfreqplot(self,txtfile):
        #txtfile = "./text/我的孤独是一座花园.txt"
        self.bct=barchart()
        self.bct.wordfreqsum(txtfile)

        #取参数
        labels=self.bct.labels
        nums=self.bct.nums
        title=self.bct.title
        self.wfreq=self.bct.wfreq #词频字典

        self.plotchart(labels,nums,title)
        print(self.wfreq)
        #当函数调用完，self.bct 对象就被清除了吗,为什么这个参数没有共享，似乎因为他们来自不同的对象
        #虽然是同一个类属性，但是由不同对象创建
        #self.statistics.mpl.wordfreqplot(self.txtfile)
        #self.customwidget.mpl.wordcloud_plot(self.txtfile,self.imgfile,self.para)





    def wordcloud_plot(self, txtfile, imgfile, para):

        # txtfile = "./text/我的孤独是一座花园.txt"
        # imgfile = "./images/动物/1225574.png"
        self.bct = barchart()
        self.bct.wordfreqsum(txtfile)
        self.wfreq = self.bct.wfreq  # 词频字典

        txt = open(txtfile, encoding='UTF-8').read()
        txtlist = jieba.lcut(txt)
        string = " ".join(txtlist)
        para['stopwords'] = jieba.lcut(para['stopwords'])

        mk = imageio.imread(imgfile)

        # 设定参数


        self.wc = wordcloud.WordCloud(width=para["width"],
                                      height=para['height'],
                                      background_color='white',
                                      font_path=para['font_path'],
                                      mask=mk,
                                      max_words=para['number'],
                                      scale=para['scale'],
                                      stopwords=para['stopwords'],
                                      contour_width=para['contour_width'],
                                      relative_scaling=para['relative_scaling'],
                                      colormap=para['colormap'])  # matplotlib colormap

        if para['swf'] ==0:
            self.wc.generate(string)  # 先生成对象，然后考虑着色
        else:

            print(self.wfreq)
            self.wc.generate_from_frequencies(self.wfreq)



        #清除原来的图像
        self.axes.clear()

        if para['tc'] == 0:
            self.axes.imshow(self.wc)
        else:
            image_colors = ImageColorGenerator(mk)
            wc_color = self.wc.recolor(color_func=image_colors)
            self.axes.imshow(wc_color)

        self.draw()

    def bgplot(self):
        bg = "./result/狐狸.png"
        background = imageio.imread(bg)
        self.axes.imshow(background)

    def static_plot(self):


        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.axes.set_ylabel('静态图：Y轴')
        self.axes.set_xlabel('静态图：X轴')
        self.axes.grid(True)


class MatplotlibWidget(QWidget):  # 这个类将导入UI文件
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.mplinitUi()

    def mplinitUi(self):
        self.layout_mpl = QVBoxLayout(self)
        self.mpl = MyMplCanvas()  # 调用初始化函数，mpl是绘图类
        self.mpl_ntb = NavigationToolbar(self.mpl, self)  # 添加完整的 toolbar
        self.layout_mpl.addWidget(self.mpl)
        self.layout_mpl.addWidget(self.mpl_ntb)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    ui.show()
    sys.exit(app.exec_())
