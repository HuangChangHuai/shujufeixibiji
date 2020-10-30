# -*- coding=utf-8 -*-
# Author  : 大白的浅
# Time    : 2019/1/12 15:34
# 描述    : 210773579@qq.com
'''   关系型数据\

    在众多的可视化图形中,有一类图形专门用来探究两个或者三个变量之间的关系,例如,
散点图用于发现两个数值变量之间的关系,气泡图用于展现三个数值之间的关系,
热力图则体现了两个离散变量之间的组合关系
'''

'''  1 散点图

    如果需要研究两个数值之间是否存在某种关系,例如正向的线性关系,或者是趋势性
的非线性关系,那个散点图将是最佳的选择

'''
#  matplotlib模块
 #matlplotlib模块中的scatter函数可以非常方便的绘制两个数值型变量的散点图

# import pandas as pd
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import random
#
# # 设置中文字体
# mpl.rcParams['font.sans-serif'] = ['SimHei']
#
# data = pd.DataFrame(
# {'销售额':[2000,2300,2600,2900,3000,3300,3500,3900,4000,4300,4500,4700],
# '利润': [250,280,290,310,340,360,370,380,410,420,430,450]},
#                     index = [1,2,3,4,5,6,7,8,9,10,11,12]
#                  )
# print(data)
#
# plt.scatter(x=data['销售额'],
#             y=data['利润'],
#             label = '办公用品',
#             color = 'steelblue',
#             alpha= 0.8
# )
#
# plt.xlabel('销售额（万元）')
# plt.ylabel('利润（万元）')
#
# plt.title("销售额利润散点图")
# plt.legend()
# plt.show()






# pandas模块


# import pandas as pd
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import random
#
# # 设置中文字体
# mpl.rcParams['font.sans-serif'] = ['SimHei']
#
# data = pd.DataFrame({'销售额':[2000,2300,2600,2900,3000,3300,3500,3900,4000,4300,4500,4700],
#                      '利润': [250,280,290,310,340,360,370,380,410,420,430,450]},
#                     index = [1,2,3,4,5,6,7,8,9,10,11,12]
#                  )
# print(data)
#
# data.plot(x = '销售额',
#           y = '利润',
#           kind = 'scatter')
#
# plt.xlabel('销售额（万元）')
# plt.ylabel('利润（万元）')
#
# plt.title("销售额利润散点图")
# plt.show()







''' seaborn模块

    尽管使用matplotlib 和 pandas可以非常方便地绘制出散点图,但是绘制分组散点图
会稍微复杂一点了,如果使用seaborn模块中的lmplot函数,那就非常方便了,而且,他还可
以根据散点图添加线性拟合线,
    lmplot函数还可以指定lowess参数拟合局部多项式回归,指定logistic参数拟合逻辑
回归,指定order参数做多项式回归,指定robust做鲁棒回归
'''

# import pandas
# import matplotlib
# import matplotlib.pyplot as  plt
# import seaborn
#
# #设置中文字体
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
#
# data = pandas.DataFrame({'销售额':[2000,2300,2600,2900,3000,3300,3500,3900,4000,4300,4500,4700],
#                      '利润': [250,280,290,310,340,360,370,380,410,420,430,450]},
#                     index = [1,2,3,4,5,6,7,8,9,10,11,12])
#
# seaborn.lmplot(x='销售额',
#                y='利润',
#                data=data,
#                legend=False,
#                truncate=True)
# plt.xlabel('销售额(万元)')
# plt.ylabel('利润(万元)')
# plt.title("销售额利润散点图")
# plt.show()









""" 2 气泡图

    散点图一般用来反应两个离散型数据变量的关系，如果还想通过散点图添加第三个
数值变量的信息，一般可以使用用气泡图。气泡图的实质就是通过第三个数值型变量控
制每个散点的大小，点越大，代表第三维的数值越高，反之亦然。
"""
# import pandas
# import matplotlib
# import matplotlib.pyplot as plt
# import random
#
# #设置中文字体
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
#
# data = pandas.DataFrame({'销售额':[random.randint(7000,9000) for i in range(12)],
#                      '利润': [random.randint(500, 2000) for i in range(12)],
#                      '利润率': [random.randint(1, 100)*5 for i in range(12)]},
#                     index = [1,2,3,4,5,6,7,8,9,10,11,12])
# # print(data)
#
# plt.scatter(x=data['销售额'],
#             y=data['利润'],
#             s=data['利润率'],
#             label='办公用品',
#             color='steelblue',
#             alpha=0.8)
#
# plt.xlabel('销售额（万元）')
# plt.ylabel('利润（万元）')
# plt.title("销售额利润利润率气泡表")
# plt.legend()
# plt.show()
'''
pandas与seaborn中没有绘制气泡图的方法或函数。
Python中的bokeh模块，也可以实现绘制气泡图的功能。
'''









""" 3  热力图

    热力图,也叫交叉填充图,它的用法是现实列联表的可视化,通过图形的方式展现两个
离散变量之间的组合关系
    seaborn中的heatmap函数,可以完成热力图的绘制
"""
# import pandas
# import matplotlib
# import matplotlib.pyplot as plt
# import seaborn
# import random
#
# #设置中文字体
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
#
# data = pandas.DataFrame({'2016':[random.randint(500,2000) for i in range(12)],
#                      '2017': [random.randint(500, 2000) for i in range(12)],
#                      '2018': [random.randint(500, 2000) for i in range(12)],
#                      '2019': [random.randint(500, 2000) for i in range(12)],
#                      '2020': [random.randint(500, 2000) for i in range(12)],},
#                     index = [1,2,3,4,5,6,7,8,9,10,11,12])
# # print(data)
#
# seaborn.heatmap(data=data,
#                 linewidths=1,
#                 cmap='PuBuGn', #填充颜色
#                 annot=True, #显示数值
#                 fmt='' #不用科学计数法
#                 )
# plt.title("近五年每月销售额热力表")
# plt.show()




































































