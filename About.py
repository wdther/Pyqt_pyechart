# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(638, 481)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/images/动物/狐狸.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(About)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setStyleSheet("")
        self.lcdNumber.setProperty("intValue", 5)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setProperty("intValue", 2)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout.addWidget(self.lcdNumber_2)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumber_3.setProperty("intValue", 0)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.horizontalLayout.addWidget(self.lcdNumber_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        About.setCentralWidget(self.centralwidget)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "关于"))
        self.textEdit.setHtml(_translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">前言：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">本项目主要是对Wordcloud和Pyechart做了一些参数上的封装使得没有编程基础的人也可以绘制一些美观的图。本项目开始于Python程序设计公选课，中间因为考试的原因中断。考试结束后将代码整理至Github开源。因为是因为我的重心转向了Qt，而python将成为我的脚本语言工具，而不是用来开发复杂的GUI。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">第三方资源：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">①图标 图标资源大多来源于 </span><a href=\"https://www.easyicon.net/\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">easyicon</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.easyicon.net/\"><span style=\" font-size:12pt; text-decoration: underline; color:#000000;\">②背景图  因为我没有美术功底，所以背景图取至免版权图库 </span></a><a href=\"https://pixabay.com/\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">Pixabay</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pixabay.com/\"><span style=\" font-size:12pt; text-decoration: underline; color:#000000;\">③词云文本 。文档中带有四份文本《月光》《北岛诗集》《一直特立独行的猪》《我的孤独是一座花园》均来源于网络，如有侵权，请联系我删除。</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; text-decoration: underline; color:#0000ff;\"><br /></p></body></html>"))
import wcqt_rc
