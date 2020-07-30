from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_WordCloud_pyqt import Ui_MainWindow  # 【UI】指的是UI文件的文件名
from About import Ui_About
from Plotly_PyQt5 import Plotly_PyQt5  # 主逻辑  #导入pyechart
# from UI_matpltest import Ui_MainWindow
import pyecharts.globals
import os
import sys

class PyQtLogic_about(QMainWindow, Ui_About):
    def __init__(self):
        super(PyQtLogic_about, self).__init__()  #
        self.setupUi(self)  # #




class PyQtLogic(QMainWindow, Ui_MainWindow):  # 构造函数，QMainWindows来自于 from

    def __init__(self):
        super(PyQtLogic, self).__init__()  # #首先找到子类（my转成QWidget的对象，然后被转化的self调用自己的init函数
        self.setupUi(self)  # #直接继承界面类，调用类的setupUi方法

        # 创建实例对象
        self.pye = Plotly_PyQt5()  # pyechart
        welcome=os.getcwd()+"./welcome/index.html"
        self.qwebengine_Graph.load(QUrl.fromLocalFile(welcome))
        self.pyecolor=''
        # self.qwebengine.setGeometry(QRect(50, 20, 1200, 600)

    def aboutthis(self):
        #关于此项目
         self.aboutdial=PyQtLogic_about()
         self.aboutdial.show()






    def alter(self,file, old_str, new_str):
        """
        替换文件中的字符串
        :param file:文件名
        :param old_str:就字符串
        :param new_str:新字符串
        :return:
        """
        file_data = ""
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                if old_str in line:
                    line = line.replace(old_str, new_str)
                file_data += line
        with open(file, "w", encoding="utf-8") as f:
            f.write(file_data)

    #alter("file1", "09876", "python")

    def Tree_plotData(self):
        self.Treedatafile, _ = QFileDialog.getOpenFileName(self,
                                                            '打开文件',
                                                            "./template/",
                                                            "Excel files (*.xlsx)")


    def Tree_plot(self):
        # qwebengine 是对象，.load(QUrl.fromLocalFile是方法 调用self.pye.pyechart_Tree_plot()以获得参数
        # 通过pye 访问方法
        self.pyeParainit()  # 初始化所需参数
        htmlfile = self.pye.pyechart_Tree_plot(self.Treedatafile, self.pyePara)
        if self.oib == 0:
            self.qwebengine_Tree.load(QUrl.fromLocalFile(htmlfile))
        else:
            os.startfile(htmlfile)

    def Geo_plotData(self):
        self.Geodatafile, _ = QFileDialog.getOpenFileName(self,
                                                          '打开文件',
                                                          "./template/",
                                                          "Excel files (*.xlsx)")

    def Geo_plot(self):
        # qwebengine 是对象，.load(QUrl.fromLocalFile是方法 调用self.pye.pyechart_Geo_plot()以获得参数
        # 通过pye 访问方法
        self.pyeParainit()  # 初始化所需参数
        #htmlfile = self.pye.pyechart_Geo_plot(self.Geodatafile,self.pyePara)
        htmlfile = self.pye.pyechart_Geo_plot()
        if self.oib == 0:
            self.qwebengine_Geo.load(QUrl.fromLocalFile(htmlfile))
        else:
            os.startfile(htmlfile)


    def Graph_plotDataTemp(self):
        currDir = os.getcwd()
        file = currDir + "./template/关系图.xlsx"
        os.startfile(file)  # 加一个r，以避免转义字符

    def Graph_plotData(self):
        self.Graphdatafile, _ = QFileDialog.getOpenFileName(self,
                                                          '打开文件',
                                                          "./template/",
                                                          "Excel files (*.xlsx)")

    def Graph_plot(self):
        # qwebengine 是对象，.load(QUrl.fromLocalFile是方法 调用self.pye.pyechart_Graph_plot()以获得参数
        # 通过pye 访问方法
        self.pyeParainit()  # 初始化所需参数
        htmlfile = self.pye.pyechart_Graph_plot(self.Graphdatafile,self.pyePara)
        if self.oib == 0:
            self.qwebengine_Graph.load(QUrl.fromLocalFile(htmlfile))
        else:
            os.startfile(htmlfile)

    def Sankey_plotData(self):
        self.Sankeydatafile, _ = QFileDialog.getOpenFileName(self,
                                                            '打开文件',
                                                            "./template/",
                                                            "Excel files (*.xlsx)")

    def Sankey_plot(self):
        # qwebengine 是对象，.load(QUrl.fromLocalFile是方法 调用self.pye.pyechart_Sankey_plot()以获得参数
        # 通过pye 访问方法
        self.pyeParainit()  # 初始化所需参数
        htmlfile = self.pye.pyechart_Sankey_plot(self.Sankeydatafile, self.pyePara)
        if self.oib == 0:
            self.qwebengine_Sankey.load(QUrl.fromLocalFile(htmlfile))
        else:
            os.startfile(htmlfile)


    def Sunburst_plotData(self):
        self.Sunburstdatafile, _ = QFileDialog.getOpenFileName(self,
                                                            '打开文件',
                                                            "./template/",
                                                            "Excel files (*.xlsx)")

    def Sunburst_plot(self):
        # qwebengine 是对象，.load(QUrl.fromLocalFile是方法 调用self.pye.pyechart_Sunburst_plot()以获得参数
        # 通过pye 访问方法
        self.pyeParainit()  # 初始化所需参数
        htmlfile = self.pye.pyechart_Sunburst_plot(self.Sunburstdatafile, self.pyePara)
        if self.oib == 0:
            self.qwebengine_Sunburst.load(QUrl.fromLocalFile(htmlfile))
        else:
            os.startfile(htmlfile)

    # ----------------------------------------------------------
    def Pie_plot(self):
        self.pyeParainit()  # 初始化所需参数
        htmlfile = self.pye.pyechart_Pie_plot(self.piedatafile, self.pyePara)
        if self.oib == 0:
            self.qwebengine_Pie.load(QUrl.fromLocalFile(htmlfile))
        else:
            os.startfile(htmlfile)
    def Pie_plotData(self):
        self.piedatafile, _ = QFileDialog.getOpenFileName(self,
                                                          '打开文件',
                                                          "./template/",
                                                          "Excel files (*.xlsx)")

    def Pie_plotDataTemp(self):
        currDir = os.getcwd()
        file = currDir + "./template/Pie.xlsx"
        os.startfile(file)  # 加一个r，以避免转义字符
    # ----------------------------------------------------------

    def Line_plot(self):
        self.pyeParainit()  # 初始化所需参数
        htmlfile = self.pye.pyechart_Line_plot(self.Linedatafile, self.pyePara)
        if self.oib == 0:
            self.qwebengine_Line.load(QUrl.fromLocalFile(htmlfile))
        else:
            os.startfile(htmlfile)
    def Line_plotData(self):
        self.Linedatafile, _ = QFileDialog.getOpenFileName(self,
                                                          '打开文件',
                                                          "./template/",
                                                          "Excel files (*.xlsx)")
    def Scatter_plot(self):
        self.pyeParainit()  # 初始化所需参数
        htmlfile = self.pye.pyechart_Scatter_plot(self.Scatterdatafile, self.pyePara)
        if self.oib == 0:
            self.qwebengine_Scatter.load(QUrl.fromLocalFile(htmlfile))
        else:
            os.startfile(htmlfile)
    def Scatter_plotData(self):
        self.Scatterdatafile, _ = QFileDialog.getOpenFileName(self,
                                                          '打开文件',
                                                          "./template/",
                                                          "Excel files (*.xlsx)")
    def EffectScatter_plot(self):
        self.pyeParainit()  # 初始化所需参数
        htmlfile = self.pye.pyechart_EffectScatter_plot(self.EffectScatterdatafile, self.pyePara)
        if self.oib == 0:
            self.qwebengine_EffectScatter.load(QUrl.fromLocalFile(htmlfile))
        else:
            os.startfile(htmlfile)
    def EffectScatter_plotData(self):
        self.EffectScatterdatafile, _ = QFileDialog.getOpenFileName(self,
                                                          '打开文件',
                                                          "./template/",
                                                          "Excel files (*.xlsx)")
    def Bar_plot(self):
        self.pyeParainit()  # 初始化所需参数
        htmlfile = self.pye.pyechart_Bar_plot(self.Bardatafile, self.pyePara)
        if self.oib == 0:
            self.qwebengine_Bar.load(QUrl.fromLocalFile(htmlfile))
        else:
            os.startfile(htmlfile)
    def Bar_plotData(self):
        self.Bardatafile, _ = QFileDialog.getOpenFileName(self,
                                                          '打开文件',
                                                          "./template/",
                                                          "Excel files (*.xlsx)")
    def PictorialBar_plot(self):
        self.pyeParainit()  # 初始化所需参数
        htmlfile = self.pye.pyechart_PictorialBar_plot(self.PictorialBardatafile, self.pyePara)
        if self.oib == 0:
            self.qwebengine_PictorialBar.load(QUrl.fromLocalFile(htmlfile))
        else:
            os.startfile(htmlfile)
    def PictorialBar_plotData(self):
        self.PictorialBardatafile, _ = QFileDialog.getOpenFileName(self,
                                                          '打开文件',
                                                          "./template/",
                                                          "Excel files (*.xlsx)")
    def colorchanged(self):
        self.Templatecolor.setChecked(0)

    def parainit(self):
        # self.para.a=1 错误用法，不存在这样的属性
        # self.a=1 正确用法，动态创建属性
        self.tc = self.Templatecolor.isChecked()
        self.swf = self.StatisWordFreq.isChecked()
        self.pscale = self.scale.value()
        self.number = self.spinBox.value()
        self.pheight = self.height.value()
        self.pwidth = self.width.value()
        self.pstopwords = self.stopwords.toPlainText()
        self.pcontour_width = self.contour_width.value()
        self.prelative_scaling = self.relative_scaling.value()
        self.pcolormap = self.colormap.currentText()
        sfont = self.FoncobotBox.currentText()

        if sfont == "宋体":
            self.font_path = "simsun.ttc"

        elif sfont == "楷体":
            self.font_path = "simkai.ttf"

        elif sfont == "行书":
            self.font_path = "STXINGKA.TTF"
        elif sfont == "Courier New":
            self.font_path = "cour.ttf"



        list = [('tc', self.tc),
                ('scale', self.pscale),
                ('font_path', self.font_path),
                ('number', self.number),
                ('width', self.pwidth),
                ('height', self.pheight),
                ('stopwords', self.pstopwords),
                ('contour_width', self.pcontour_width),
                ('colormap', self.pcolormap),
                ('relative_scaling', self.prelative_scaling),
                ('swf', self.swf)
                ]

        self.para = dict(list)  # 将列表转化为字典
        print(self.para)
    def TreeorMap(self):
        self.TreemapB.setChecked(False) #手动互斥
    def MaporTree(self):
        self.TreeB.setChecked(False) #手动互斥

    def pyeParainit(self):
        pyetheme = self.theme.currentText()
        pyetitle = self.title.text()
        pyewidth = str(self.Pwidth.value()) + "px"
        pyeheight = str(self.Pheight.value()) + "px"
        self.oib = self.open_in_brower.isChecked()
        if self.layoutcombox.currentText()=="环绕":
            layout="circular"
        else:
            layout="force"
        if self.Treelayout.currentText()=='正交':
            Tlayout= "orthogonal"
        else:
            Tlayout='radial'

        pyefont_size = self.font_size.value()
        pyefont_family =self.font_family.currentText()
        pyesubtitle =self.subtitle.text()
        pyegravity=self.gravity.value()
        pyerepulsion=self.repulsion.value()
        Tsymbol=self.Treesymbol.currentText()
        Tsymbol_size=self.symbol_size.value()
        TB=self.TreeB.isChecked()
        TmB=self.TreemapB.isChecked()
        Tstate=[TB,TmB]
        pyeleaf_depth=self.leaf_depth.value()
        off=self.offline.isChecked()
        on=self.online.isChecked()

        path = pyecharts.globals.__file__
        if on :
            self.alter(path, "./js/", "https://assets.pyecharts.org/assets/")
        elif off:
            self.alter(path,"https://assets.pyecharts.org/assets/","./js/")

        pyeline_width=self.line_width.value()
        pyeopacity=self.opacity.value()
        pyecurve=self.curve.value()
        pyepositon=self.position.currentText()
        pyex2y=self.x2y.isChecked()
        pyeDataZoom=self.DataZoom.isChecked()
        pyeToolBox=self.ToolBox.isChecked()
        pyeVisualMap=self.VisualMap.isChecked()
        pyeXAxis=self.XAxis.text()
        pyeYAxis=self.YAxis.text()
        pyeTimeLineOn=self.TimeLineOn.isChecked()






        dict1 = {'theme': pyetheme,
                 'title': pyetitle,
                 'width': pyewidth,
                 'height': pyeheight,
                 "layout":layout,
                 "font_size":pyefont_size,
                 "font_family":pyefont_family,
                 "subtitle":pyesubtitle,
                 "color":self.pyecolor,
                 "gravity":pyegravity,
                 "repulsion":pyerepulsion,
                 'Tlayout':Tlayout,
                 'Tsymbol':Tsymbol,
                 'Tsymbol_size':Tsymbol_size,
                 'Tstate':Tstate,
                 'leaf_depth':pyeleaf_depth,
                 'line_width':pyeline_width,
                 'opacity':pyeopacity,
                 'curve':pyecurve,
                 'positon':pyepositon,
                 'x2y':pyex2y,
                 'DataZoom':pyeDataZoom,
                 'ToolBox':pyeToolBox,
                 'VisualMap':pyeVisualMap,
                 'XAxis':pyeXAxis,
                 'YAxis':pyeYAxis,
                 'TimeLineOn':pyeTimeLineOn
                 }

        self.pyePara = dict1
        print(self.pyePara)

    def textbutton(self):
        # 双引号可以不加转义字符
        # 返回两个参数，文件名和文件类型
        self.txtfile, _ = QFileDialog.getOpenFileName(self,
                                                      '打开文件',
                                                      "./text/",
                                                      "txt files (*.txt)")
        print(self.txtfile)
        folder_path, file_name = os.path.split(self.txtfile)
        self.txtlineEdit.setText(file_name)

    def imagebutton(self):

        self.imgfile, _ = QFileDialog.getOpenFileName(self,
                                                      '打开文件',
                                                      "./images/",
                                                      "Image files (*.jpg *.png *.gif)")
        folder_path, file_name = os.path.split(self.imgfile)
        self.imglineEdit.setText(file_name)

    def Cloudplot(self):  # 调用格式 self.对象.MatplotlibWidget(QWidget)类中定义的方法
        self.parainit()

        if self.swf == 1:  # 如果按照词频来绘制
            self.statistics.mpl.wordfreqplot(self.txtfile)
            self.tabWidget_2.setCurrentIndex(1)

        # self.mpl  是MyMplCanvas() 对象
        print(self.para)

        self.customwidget.mpl.wordcloud_plot(self.txtfile, self.imgfile, self.para)
        self.mytips.setPlainText("正在生成图像，请稍等...")

    def saveimg(self):
        fileName2, ok2 = QFileDialog.getSaveFileName(self,
                                                     "文件保存",
                                                     "./",
                                                     "Image Files (*.png)")
        self.customwidget.mpl.wc.to_file(fileName2)
    def Color_set(self):
        col = QColorDialog.getColor()
        self.pyecolor=col.name()
        print(col)
        print(col.name)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # pyqt窗口必须在QApplication方法中使用
    window = PyQtLogic()  # 实例化类

    #window.show()  # windows调用show方法
    window.show()
    sys.exit(app.exec_())  # #消息结束的时候，结束进程，并返回0，接着调用sys.exit(0)退出程序
