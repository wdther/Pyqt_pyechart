# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:29:55 2017

@author: Administrator
"""

import os
# ------------------------------------------
import pandas as pd

from pyecharts import options as opts
# from pyecharts.charts import Pie
# from pyecharts.charts import TreeMap
# from pyecharts.charts import Graph
# from pyecharts.charts import Sunburst
# from pyecharts.charts import Bar
# from pyecharts.charts import Sankey
# from pyecharts.charts import Tree
from pyecharts.commons import utils
from pyecharts.globals import ThemeType,RenderType,ChartType, SymbolType
from pyecharts.faker import Faker
# -----------------------------------------


import numpy as np
import matplotlib.pyplot as plt


class Plotly_PyQt5():
    def __init__(self):
        # 设置存储html文件的文件夹
        plotly_dir = 'plotly_html'
        if not os.path.isdir(plotly_dir):
            os.mkdir(plotly_dir)
        # 使用os.sep的话，就不用考虑这个了，os.sep根据你所处的平台，自动采用相应的分隔符号
        # os.getcwd() 方法用于返回当前工作目录。
        # plotly_dir给定文件名
        self.path_dir_plotly_html = os.getcwd() + os.sep + plotly_dir
        # ---------------------储存主题名——————————————————
        self.themedict = {"WHITE": ThemeType.WHITE, "LIGHT": ThemeType.LIGHT, "DARK": ThemeType.DARK,
                          "CHALK": ThemeType.CHALK,
                          "ESSOS": ThemeType.ESSOS, "INFOGRAPHIC": ThemeType.INFOGRAPHIC,
                          "MACARONS": ThemeType.MACARONS, "PURPLE_PASSION": ThemeType.PURPLE_PASSION,
                          "ROMA": ThemeType.ROMA, "ROMANTIC": ThemeType.ROMANTIC, "SHINE": ThemeType.SHINE,
                          "VINTAGE": ThemeType.VINTAGE, "WALDEN": ThemeType.WALDEN, "WESTEROS": ThemeType.WESTEROS,
                          "WONDERLAND": ThemeType.WONDERLAND}
        self.symboldict = {'空心圆': 'emptyCircle', '圆': 'circle', '矩形': 'rect',
                      '圆角矩形': 'roundRect', '三角形': 'triangle', '钻石形': 'diamond', '针形': 'pin', '箭头形': 'arrow'}
    def Tree_dict(self,df): #用于共享计算树结构数据
        from Tree import MyTree
        from pyecharts.charts import Tree
        Eroot = df['root'].dropna().values.tolist()
        df.fillna(0, inplace=True)

        co = df.columns.values.tolist()  # ['level1', 'level2', 'level3', 'value']

        co_num = len(co)  # 列数
        row_num = len(df)
        Vars = []
        nodes = {}

        Ename = df['name'].dropna().values.tolist()
        Evalue = df['value'].dropna().values.tolist()
        for i in range(0, len(Ename)):
            Vars.append(MyTree(Ename[i], Evalue[i]))

            nodes.setdefault(Ename[i], Vars[i])

        for i in range(co_num - 1, 2, -1):  # 列数

            for j in range(row_num - 1):  # 行数
                co_v = df.values[j]  # 获取该行的数据,一整行
                if co_v[i - 1] != 0 and co_v[i] != 0:
                    A = co_v[i - 1]
                    B = co_v[i]
                    print(A, B)
                    # 检索字典获得变量
                    Var_A = nodes[A]
                    Var_B = nodes[B]

                    Var_A.add_link(Var_B)

                    # print(co_v[i])
        # 打印所有根节点
        dic = []
        for i in range(0, len(Eroot)):
            Var_str = Eroot[i]  # 返回字符串
            Var_root = nodes[Var_str]  # 返回变量
            dic.append(Var_root.to_dict())  #
            dic2 = []
            [dic2.append(i) for i in dic if not i in dic2]  # 去除重复元素
            #dic = [dic2[0]]  # 只有一个根节点,封装为列表(树图的情形）

            dic=dic2
        return dic

    def Common_code(self,chart,path_plotly,para):
        datazoom_opts=[]
        toolbox_opts=[]
        visualmap_opts=[]
        if para['DataZoom']:
            datazoom_opts=opts.DataZoomOpts()
        if para['ToolBox']:
            toolbox_opts=opts.ToolboxOpts(
                feature=opts.ToolBoxFeatureOpts(
                    save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(background_color="white", pixel_ratio=2)
                ))
        if para['VisualMap']:
            visualmap_opts=opts.VisualMapOpts()

        chart.set_global_opts(
            title_opts=opts.TitleOpts(title=para["title"], subtitle=para["subtitle"]),
            legend_opts=opts.LegendOpts(item_width=50, item_height=25),  # 图例，默认25/14
            visualmap_opts=visualmap_opts,
            datazoom_opts=datazoom_opts,
            toolbox_opts= toolbox_opts,
            yaxis_opts=opts.AxisOpts(name=para['YAxis']),
            xaxis_opts=opts.AxisOpts(name=para['XAxis']),
        )
        #chart.set_global_opts( visualmap_opts=opts.VisualMapOpts(orient="horizontal"))
        chart.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position=para['positon'],
                                                        font_size=para["font_size"],
                                                        font_family=para["font_family"]),
                            linestyle_opts=opts.LineStyleOpts(width=para['line_width'],opacity=para['opacity'],
                                                              curve=para['curve']
                            )
                            )
        if not para['TimeLineOn']:
            chart.render(path_plotly)


    def pyechart_Geo_plot(self):
        from pyecharts.charts import Geo
        file_name = '地理图.html'
        path_plotly = self.path_dir_plotly_html + os.sep + file_name  # 文件路径，前面是文件夹后面是文件名
        #costumeTheme = self.themedict[para['theme']]
        #df= pd.read_excel(filedata, sheet_name='Sheet1')

        c = (
            Geo()
                .add_schema(
                maptype="china",
                itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"),
            )
                .add(
                "",
                [("广州", 55), ("北京", 66), ("杭州", 77), ("重庆", 88)],
                type_=ChartType.EFFECT_SCATTER,
                color="white",
            )
                .add(
                "geo",
                [("广州", "上海"), ("广州", "北京"), ("广州", "杭州"), ("广州", "重庆")],
                type_=ChartType.LINES,
                effect_opts=opts.EffectOpts(
                    symbol=SymbolType.ARROW, symbol_size=6, color="blue"
                ),
                linestyle_opts=opts.LineStyleOpts(curve=0.2),
            )
        )

        return path_plotly  # 返回该HTML文件路径


    def pyechart_Graph_plot(self,filedata, para):  # 指定文件名，包括扩展名
        from pyecharts.charts import Graph
        from pyecharts.globals import CurrentConfig
        print(CurrentConfig.ONLINE_HOST)

        file_name = '关系图.html'
        path_plotly = self.path_dir_plotly_html + os.sep + file_name  # 文件路径，前面是文件夹后面是文件名
        #print(path_plotly)
        costumeTheme = self.themedict[para['theme']]
        df= pd.read_excel(filedata, sheet_name='Sheet1')

        Ename = df['name'].dropna().values.tolist()

        Esource = df['source'].dropna().values.tolist()
        Etarget = df['target'].dropna().values.tolist()
        Elabel=df['relation'].dropna().values.tolist()
        Evalue=df['value'].dropna().values.tolist()
        print(Elabel)
        Esymbol_size=df['size'].dropna().values.tolist()
        Ecategory=df['category'].dropna().values.tolist()
        #print(Ecategory)
        nodes_data = []
        links_data = []
        category=[]
        for i in range(0, len(Ename)):
            nodes_data.append({'name': Ename[i],
                           'symbolSize':int(Esymbol_size[i]),
                            'symbol':"circle" , ## ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'
                             'category':Ecategory[i]})
            category.append({'name':Ecategory[i]})
        #print(nodes_data)
        for i in range(0, len(Esource)):
            links_data.append({'source': Esource[i],
                               'target': Etarget[i],
                               'value':Evalue[i]
                               })

        a = str(Elabel)
        GEO = "function (params) { a= " + a + ";return a[params.dataIndex];}"
        #GEO = "function (params) { return params.dataIndex;}"   #数据索引 #renderer为svg时清晰一点，但是无法保存为图片
        c = (
            Graph(init_opts=opts.InitOpts(theme=costumeTheme, renderer="canvs",width=para['width'], height=para['height']))  #
                .add(
                "",  #series_name, # 系列名称，用于 tooltip 的显示，legend 的图例筛选。
                nodes=nodes_data,
                links=links_data,
                categories=category,
                gravity=para["gravity"],
                repulsion=para["repulsion"],
                edge_symbol=["","arrow"], #可以单一指定
                is_draggable=True, #允许拖动，只在力引导有用
                layout=para['layout'], ## 'circular' 采用环形布局。# 'force' 采用力引导布局
                is_rotate_label=True,
                linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),  #标签在上方显示，以防止被遮挡 top/middle,edge的上方是箭头的起点
                label_opts=opts.LabelOpts(is_show=True, color=para["color"],position="top",font_size=para["font_size"], font_family=para["font_family"]),
                edge_label=opts.LabelOpts(
                    is_show=True, color=para["color"],position="middle",font_size=para["font_size"], font_family=para["font_family"],formatter=utils.JsCode(GEO)),

            ))
        chart=c
        self.Common_code(chart, path_plotly, para)
        return path_plotly  # 返回该HTML文件路径


        # 创建关系图对象

    def pyechart_Sankey_plot(self,filedata,para):
        from pyecharts.charts import Sankey
        file_name = '桑基图.html'
        path_plotly = self.path_dir_plotly_html + os.sep + file_name  # 文件路径，前面是文件夹后面是文件名
        # print(path_plotly)
        costumeTheme = self.themedict[para['theme']]
        df = pd.read_excel(filedata, sheet_name='Sheet1')

        Ename = df['name'].dropna().values.tolist()

        Esource = df['source'].dropna().values.tolist()
        Etarget = df['target'].dropna().values.tolist()
       # Elabel = df['relation'].dropna().values.tolist()
        Evalue = df['value'].dropna().values.tolist()
        #print(Elabel)
        #Esymbol_size = df['size'].dropna().values.tolist()
        #Ecategory = df['category'].dropna().values.tolist()
        # print(Ecategory)
        nodes_data = []
        links_data = []
        category = []
        for i in range(0, len(Ename)):
            nodes_data.append({'name': Ename[i]})

                               ## ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'


        # print(nodes_data)
        for i in range(0, len(Esource)):
            links_data.append({'source': Esource[i],
                               'target': Etarget[i],
                               'value': Evalue[i]
                               })

        print(nodes_data)
        c = (
            Sankey(init_opts=opts.InitOpts(theme=costumeTheme, renderer="canvs",width=para['width'], height=para['height']))
               # .set_colors(colors)
                .add(
                "sankey",
                nodes=nodes_data,
                links=links_data,
                pos_bottom="10%",
                focus_node_adjacency="allEdges",
                orient="vertical",
                linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
                label_opts=opts.LabelOpts(is_show=True, color=para["color"],position="top",font_size=para["font_size"], font_family=para["font_family"]),
            )
            #     .set_global_opts(
            #     title_opts=opts.TitleOpts(title=para["title"], subtitle=para["subtitle"]),
            #     legend_opts=opts.LegendOpts(item_width=50, item_height=25),  # 图例，默认25/14
            #     toolbox_opts=opts.ToolboxOpts(
            #         feature=opts.ToolBoxFeatureOpts(
            #             save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(background_color="white", pixel_ratio=2)
            #         )),
            #     # visualmap_opts=opts.VisualMapOpts(),
            #     tooltip_opts = opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
            # )
            #     .render(path_plotly)
        )

        chart = c
        self.Common_code(chart, path_plotly, para)
        return path_plotly  # 返回该HTML文件路径

    def pyechart_Tree_plot(self,filedata,para):
        from pyecharts.charts import Tree,TreeMap
        file_name = '树图.html'
        path_plotly = self.path_dir_plotly_html + os.sep + file_name  # 文件路径，前面是文件夹后面是文件名
        costumeTheme = self.themedict[para['theme']]
        costomSymbol=self.symboldict[para['Tsymbol']]
        # -----------------------------------------------------------------------


        #df = pd.read_excel(r"E:\5-程序设计\A-编程语言\01Python\自定义\Pyecharts\组合\template\树.xlsx", sheet_name='Sheet1')
        df = pd.read_excel(filedata, sheet_name='Sheet1')
        dic=self.Tree_dict( df)

        print(dic)
        if para['Tstate'][0]:
            Tr = (
                # 数据特点：可以没有value值
                Tree(init_opts=opts.InitOpts(theme=costumeTheme, renderer="canvs", width=para['width'],
                                             height=para['height']))
                    .add("", dic,
                         layout=para['Tlayout'],
                         collapse_interval=2,
                         orient="LR",
                         symbol=costomSymbol,
                         symbol_size=para['Tsymbol_size'],
                         # label_opts=opts.LabelOpts(is_show=True, color=para["color"], position="top",
                         #                           font_size=para["font_size"],
                         #                           font_family=para["font_family"])
                          )
                )
            chart=Tr

        elif para['Tstate'][1]:
            c = (
                TreeMap(init_opts=opts.InitOpts(theme=costumeTheme, renderer="canvs", width=para['width'],
                                             height=para['height']))
                    .add(
                    series_name="演示数据",
                    data=dic,
                    leaf_depth=para['leaf_depth'], #节点深度,开启下钻，不完全显示

                )
            )
            chart=c
        #  add() missing 2 required positional arguments: 'series_name' and 'data'

        self.Common_code(chart, path_plotly, para)
        return path_plotly  # 返回该HTML文件路径

    def pyechart_Sunburst_plot(self,filedata, para):
        from pyecharts.charts import Sunburst
        file_name = '旭日图.html'
        path_plotly = self.path_dir_plotly_html + os.sep + file_name  # 文件路径，前面是文件夹后面是文件名
        costumeTheme = self.themedict[para['theme']]
        # -----------------------------------------------------------------------
        df = pd.read_excel(filedata, sheet_name='Sheet1')
        dic = self.Tree_dict(df)
        sunburst = (
            Sunburst(init_opts=opts.InitOpts(theme=costumeTheme, width=para['width'], height=para['height']))  # costumeTheme=self.themedict[para['theme']]
                .add(series_name="", data_pair=dic, radius=[0, "90%"])
                .set_global_opts(
                title_opts=opts.TitleOpts(title=para["title"], subtitle=para["subtitle"]),
                toolbox_opts=opts.ToolboxOpts(
                    feature=opts.ToolBoxFeatureOpts(
                        save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(background_color="white")
                    )),
                #visualmap_opts=opts.VisualMapOpts(),
            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=True, color=para["color"], position="inside",
                                              font_size=para["font_size"],
                                              font_family=para["font_family"]))
                .render(path_plotly)
        )
        return path_plotly  # 返回该HTML文件路径

        # -----------------------------------------------------------------------
        # .render(path_plotly)  # 绝对式的文件名,存储在指定文件夹下
        # -----------------------------------------------------------------------

    def pyechart_Pie_plot(self, filedata, para):
        from pyecharts.charts import Pie
        file_name = '南丁格尔玫瑰图.html'
        path_plotly = self.path_dir_plotly_html + os.sep + file_name  # 文件路径，前面是文件夹后面是文件名
        costumeTheme = self.themedict[para['theme']]
        # -----------------------------------------------------------------------
        # 准备数据

        df = pd.read_excel(filedata, sheet_name='sheet1')
        # # 提取数据
        v = df['provinces'].values.tolist()
        d = df['num'].values.tolist()
        color_series = df['color_series'].values.tolist()

        # 降序排序
        df.sort_values(by='num', ascending=False, inplace=True)

        # 实例化Pie类
        pie1 = Pie(init_opts=opts.InitOpts(theme=costumeTheme, width=para['width'], height=para['height']))
        # 设置颜色
        pie1.set_colors(color_series)
        # 添加数据，设置饼图的半径，是否展示成南丁格尔图
        pie1.add("", [list(z) for z in zip(v, d)],
                 radius=["10%", "135%"],
                 center=["50%", "65%"],
                 rosetype="area"
                 )
        # 设置全局配置项
        pie1.set_global_opts(
                title_opts=opts.TitleOpts(title=para["title"], subtitle=para["subtitle"]),
                toolbox_opts=opts.ToolboxOpts(
                    feature=opts.ToolBoxFeatureOpts(
                        save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(background_color="white")
                    ))
                #visualmap_opts=opts.VisualMapOpts(),
            )
        # 设置系列配置项
        pie1.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="inside", font_size=12,
                                                       formatter="{b}:{c}天", font_style="normal",  # css的格式
                                                       font_weight="normal", font_family="宋体"
                                                       ),
                             )
        # 生成html文档
        pie1.render(path_plotly)
        return path_plotly  # 返回该HTML文件路径

        # -----------------------------------------------------------------------
        # -----------------------------------------------------------------------
        # .render(path_plotly)  # 绝对式的文件名,存储在指定文件夹下
        # -----------------------------------------------------------------------

    def pyechart_Line_plot(self,filedata, para):
        from pyecharts.charts import Line
        file_name = '折线图.html'
        path_plotly = self.path_dir_plotly_html + os.sep + file_name  # 文件路径，前面是文件夹后面是文件名
        costumeTheme = self.themedict[para['theme']]
        # -----------------------------------------------------------------------

        Line = (
            Line(init_opts=opts.InitOpts(theme=costumeTheme, width=para['width'], height=para['height']))  # ThemeType.LIGHT para['theme']
        )
        chart=Line
        df = pd.read_excel(filedata, sheet_name='Sheet1')
        columns = df.columns.values.tolist()
        xlabel = columns[0]
        xdata = df[xlabel].values.tolist()

        chart.add_xaxis(xaxis_data=xdata)
        for i in range(1, len(columns)):
            ylabel = columns[i]
            ydata = df[ylabel].values.tolist()
            chart.add_yaxis(series_name=ylabel, y_axis=ydata)
        if para['x2y']:
            chart.reversal_axis()
        self.Common_code(chart, path_plotly, para)

        print('成功绘制折线图')
        return path_plotly  # 返回该HTML文件路径
        # -----------------------------------------------------------------------
    def pyechart_Scatter_plot(self,filedata, para):
        from pyecharts.charts import Scatter
        file_name = '散点图.html'
        path_plotly = self.path_dir_plotly_html + os.sep + file_name  # 文件路径，前面是文件夹后面是文件名
        costumeTheme = self.themedict[para['theme']]
        # -----------------------------------------------------------------------

        Scatter = (
            Scatter(init_opts=opts.InitOpts(theme=costumeTheme, width=para['width'], height=para['height']))
        )
        chart=Scatter

        df = pd.read_excel(filedata, sheet_name='Sheet1')

        columns = df.columns.values.tolist()
        xlabel = columns[0]
        xdata = df[xlabel].values.tolist()

        chart.add_xaxis(xaxis_data=xdata)
        for i in range(1, len(columns)):
            ylabel = columns[i]
            ydata = df[ylabel].values.tolist()
            chart.add_yaxis(series_name=ylabel, y_axis=ydata)
        if para['x2y']:
            chart.reversal_axis()

        self.Common_code(chart, path_plotly, para)

        print('成功绘制散点图')
        return path_plotly  # 返回该HTML文件路径
        # -----------------------------------------------------------------------
    def pyechart_EffectScatter_plot(self, filedata,para):
        from pyecharts.charts import EffectScatter
        file_name = '散点涟漪图.html'
        path_plotly = self.path_dir_plotly_html + os.sep + file_name  # 文件路径，前面是文件夹后面是文件名
        costumeTheme = self.themedict[para['theme']]
        # -----------------------------------------------------------------------

        EffectScatter = (
            EffectScatter(init_opts=opts.InitOpts(theme=costumeTheme, width=para['width'], height=para['height']))  # ThemeType.LIGHT para['theme']
        )
        chart=EffectScatter

        df = pd.read_excel(filedata, sheet_name='Sheet1')

        columns = df.columns.values.tolist()
        xlabel = columns[0]
        xdata = df[xlabel].values.tolist()

        chart.add_xaxis(xaxis_data=xdata)
        for i in range(1, len(columns)):
            ylabel = columns[i]
            ydata = df[ylabel].values.tolist()
            chart.add_yaxis(series_name=ylabel, y_axis=ydata)
        if para['x2y']:
            chart.reversal_axis()
        self.Common_code(chart, path_plotly, para)

        print('成功绘制散点涟漪图')
        return path_plotly  # 返回该HTML文件路径
        # -----------------------------------------------------------------------
    def pyechart_Bar_plot(self,filedata, para):
        from pyecharts.charts import Bar, Timeline
        file_name = '条形图.html'
        path_plotly = self.path_dir_plotly_html + os.sep + file_name  # 文件路径，前面是文件夹后面是文件名
        costumeTheme = self.themedict[para['theme']]
        df = pd.read_excel(filedata, sheet_name='Sheet1')
        # -----------------------------------------------------------------------
        if not para['TimeLineOn']:
            bar = (
                Bar(init_opts=opts.InitOpts(theme=costumeTheme, width=para['width'], height=para['height']))
            # ThemeType.LIGHT para['theme']
            )
            chart = bar
            columns = df.columns.values.tolist()
            xlabel = columns[0]
            xdata = df[xlabel].values.tolist()

            chart.add_xaxis(xaxis_data=xdata)
            for i in range(1, len(columns)):
                ylabel = columns[i]
                ydata = df[ylabel].values.tolist()
                chart.add_yaxis(series_name=ylabel, y_axis=ydata)
            if para['x2y']:
                chart.reversal_axis()
            self.Common_code(chart, path_plotly, para)
        else:
            Timewhole = df['时间'].values.tolist()
            Timevalid = df['时间'].dropna().tolist()

            index = []
            for i in Timevalid:
                index.append(Timewhole.index(i))
            index.append(len(df))
            print(index)

            columns = df.columns.values.tolist()

            Timel = Timeline().add_schema(
                symbol='arrow',
                play_interval=1000  # 单位为毫秒
            )

            for j in range(len(index) - 1):

                chart = Bar()

                # 数据切片
                m = index[j]
                n = index[j + 1]
                xlabel = columns[1]
                xdata = df[xlabel].values.tolist()[m:n]

                chart.add_xaxis(xaxis_data=xdata)

                for i in range(2, len(columns)):
                    ylabel = columns[i]
                    ydata = df[ylabel].values.tolist()[m:n]
                    chart.add_yaxis(series_name=ylabel, y_axis=ydata)
                if para['x2y']:
                    chart.reversal_axis()

                Timel.add(chart, "{}".format(Timevalid[j]))
                self.Common_code(chart, path_plotly, para)
                Timel.render(path_plotly)


        print('成功绘制条形图')
        return path_plotly  # 返回该HTML文件路径

        # -----------------------------------------------------------------------
    def pyechart_PictorialBar_plot(self,filedata, para):
        from pyecharts.charts import PictorialBar
        file_name = '象形条形图.html'
        path_plotly = self.path_dir_plotly_html + os.sep + file_name  # 文件路径，前面是文件夹后面是文件名
        costumeTheme = self.themedict[para['theme']]
        # -----------------------------------------------------------------------

        PictorialBar = (
            PictorialBar(init_opts=opts.InitOpts(theme=costumeTheme, width=para['width'], height=para['height']))  # ThemeType.LIGHT para['theme']
        )
        chart=PictorialBar
        df = pd.read_excel(filedata, sheet_name='Sheet1')

        columns = df.columns.values.tolist()
        xlabel = columns[0]
        xdata = df[xlabel].values.tolist()

        chart.add_xaxis(xaxis_data=xdata)
        for i in range(1, len(columns)):
            ylabel = columns[i]
            ydata = df[ylabel].values.tolist()
            chart.add_yaxis(series_name=ylabel, y_axis=ydata, symbol=para['Tsymbol'],
                             symbol_size = 18,symbol_repeat = "fixed",symbol_offset = [0, 0]
            )
        if para['x2y']:
            chart.reversal_axis()

        self.Common_code(chart, path_plotly, para)
        print('成功绘制象形条形图')
        return path_plotly  # 返回该HTML文件路径
        # -----------------------------------------------------------------------


print('直接运行此文件看不到窗口')


'''
导入excel 文件
df= pd.read_excel('C:/data/rose.xlsx',sheet_name='1')
# # 提取数据
v = df['provinces'].values.tolist()
d = df['num'].values.tolist()
color_series = df['color_series'].values.tolist()
随机颜色：color_series = randomcolor(len(provinces))


'''
