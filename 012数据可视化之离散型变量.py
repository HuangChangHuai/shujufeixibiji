# -*- coding=utf-8 -*-
# Author  : 大白的浅
# Time    : 2019/1/11 21:03
# 描述    : 210773579@qq.com
"""
        离散型变量
"""

""" 1,饼图

    饼图，也叫饼状图，
    是一个划分为几个扇区的圆形统计图表，
    用于描述量、频率、或百分比之间的相对关系。
    在饼图中，每个扇区的弧长（圆心角和面积）大小为其所表示的数量的比例。
这些扇区合在一起刚好是一个完整的圆形，这些扇区就好像拼成一个切开的饼形图案。
"""
#1.1 matplotlib模块
    # 首先要导入matplotlib模块的子模块pyplot，然后利用模块中的pie函数。


#示例:
import matplotlib.pyplot as plt

# #处理中文乱码:
# plt.rcParams['font.sans-serif'] = ['SimHei']
# #构造数据
# data = [255,455,638,565,784,948,520,666]
# labels = ['王者','星耀','钻石','铂金','黄金','白银','青铜','黑铁']
# #绘制饼状图:
# plt.pie(x=data,             #数据
#         labels= labels,     #标签
#         autopct= '%.3f%%',   #格式
#         colors=['green','blue','pink','silver',
#                 'yellow','lightblue','lightgreen','lightyellow'])
# plt.title('英雄联盟玩家段位分布图')
# plt.show()
#



#
# #示例二:
# import matplotlib.pyplot as plt
#
# # 处理中文乱码
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# # 标准化处理，确保饼图是个正圆，否则是椭圆
# plt.axes(aspect='equal')
#
# #构造数据
# data = [255,455,638,565,784,948]
# labels = ['博士','硕士','本科','大专','高中','其它']
# # 设置突出显示的部分
# explode = [0,0.1,0,0,0.15,0]
#
# #绘制饼图
# plt.pie(x = data,                # 数据
#         labels = labels,         # 标签
#         autopct = '%.2f%%',      # 格式
#         explode = explode ,      # 突出显示某个部分
#         pctdistance = 0.8,       # 百分比标签到圆心的距离
#         labeldistance = 1.1,     # 标签到圆心的距离
#         startangle = 180,        # 饼图初始角度
#         radius = 1.2,            # 饼图半径
#         shadow= True,            # 阴影效果
#         wedgeprops = {'linewidth':1.5, 'edgecolor':'silver'}, # 内外边界属性值
#         textprops = {'fontsize':10, 'color':'white'}        # 设置文本标签属性值
#         )
# plt.title('活动人员学历构成')
# plt.show()
'''注意:
（A）如果绘制的图中涉及中文及数字中的负号，需要通过rcParams进行了控制；
（B）不加修饰的饼图更像是一个椭圆，所以需要利用axes函数强制为正圆。
'''






#
# # 2,pandas模块
#   #示例
# import pandas
# import matplotlib.pyplot as plt
#
# #处理中文乱码
# plt.rcParams['font.sans-serif'] = ['SimHei']
#
# data =  pandas.Series({'博士':255,'硕士':455,'本科':638,
#                        '大专':565,'高中':784,'其它':948})
# data.name = '学历构成'
# data.plot(kind = 'pie',
#           autopct = '%.2f%%',
#           radius = 1,
#           startangle = 180,
#           title = '活动人员学历构成',
#           wedgeprops={'linewidth':1.5, 'edgecolor':'silver'}, # 内外边界属性值
#           textprops = {'fontsize':10, 'color':'white'}      # 设置文本标签属性值
#          )
# #显示
# plt.show()










"""2, 条形图

    条形图亦称条图、条状图、棒形图、柱状图，是一种以长方形的长度为变量的
统计图表。
    长条图用来比较两个或者两个以上的数值（不同时间或者不同条件），只有一个变量，
通常利用最小的数据集分析。
    长条图也可横向排列，也可用多维表达方式。
"""



# 1,matplotlib模块
'''
matplotlib.pyplot.bar(left, height, alpha=1, 
                      width=0.8, color=, edgecolor=, label=, lw=3)
                      
1. left：    x轴的位置序列，一般采用range函数产生一个序列，但是有时候可以
                是字符串
2. height：  y轴的数值序列，也就是柱形图的高度，一般就是我们需要展示的数据；
3. alpha：   透明度，值越小越透明
4. width：   为柱形图的宽度，一般这是为0.8即可；
5. color或facecolor：柱形图填充的颜色；
6. edgecolor：图形边缘颜色

7. label：   解释每个图像代表的含义，这个参数是为legend()函数做铺垫的，
                表示该次bar的标签  
8. linewidth or linewidths or lw：边缘or线的宽
'''
# import numpy
# import matplotlib as mpl
# import matplotlib.pyplot as plt
#
# #设置中文字体
# mpl.rcParams['font.sans-serif'] = ['SimHei']
#
# xdata = ["北京","上海","广州","深圳","南京","重庆","长沙"]
# ydata = [2300, 1900, 1500, 1300, 1100, 2500, 800]
#
# plt.bar(xdata, ydata, alpha=0.5,width=0.3,
#         color='lightblue',edgecolor='silver',label='人口数',lw=3)
# plt.legend(loc='upper left')
# plt.xlabel('This is x axis', fontsize=15)
# plt.ylabel('万人', fontsize=15)
# plt.title('各个城市人口柱状图', fontsize=15)
#
# #如果想自己给x轴的bar加上标签,rotation控制倾斜角度
# plt.xticks(rotation=90)
# plt.yticks(numpy.arange(0, 2500, 300))
#
# plt.show()
#





'''2,pandas模块'''
# import pandas
# import matplotlib as mpl
# import matplotlib.pyplot as plt
#
# #设置中文字体
# mpl.rcParams['font.sans-serif'] = ['SimHei']
#
# data = pandas.Series([2300,1900,1500,1300,1100,2500,800],
#                      index=["北京","上海","广州","深圳","南京","重庆","长沙"])
#
# data.plot(kind = 'bar',
#           width=0.4,
#           rot=0,
#           color='steelblue',
#           title='城市人口柱状图')
# plt.show()
#








'''3, seaborn模块'''
# import seaborn as sns
# import matplotlib as mpl
# import matplotlib.pyplot as plt
#
# #设置中文字体
# mpl.rcParams['font.sans-serif'] = ['SimHei']
#
# xdata = ["北京","上海","广州","深圳","南京","重庆","长沙"]
# ydata = [2300,1900,1500,1300,1100,2500,800]
#
# sns.barplot(y=ydata,
#             x=xdata,
#             color='steelblue')
# plt.xlabel('Ylabel')
# plt.ylabel('万人')
# plt.title('各城市人口柱状图')
# plt.show()


































































































































