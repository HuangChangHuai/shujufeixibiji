# -*- coding=utf-8 -*-
# Author  : 大白的浅
# Time    : 2019/1/12 1:01
# 描述    : 210773579@qq.com
'''
        数值型变量
'''

'''1, 直方图
    
    直方图一般用来观察数据的分布形态，横坐标代表数值的均匀分段，纵坐标代表每
个段内的观测数量，一般直方图都会与核密度图搭配使用，目的是为了更加清晰地掌握
数据的分布特征。
'''


# 1,matplotlib模块

# import pandas
# import matplotlib
# import matplotlib.pyplot as plt
# import random
#
# # 设置中文字体
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
#
# data = pandas.DataFrame({'age':[random.randint(0, 100) for i in range(100)]})
# plt.hist(x=data['age'],   #数据
#          bins=20,      #列数
#          range=(0, 100),    #范围
#          color='steelblue',  #颜色
#          edgecolor = 'silver')   #边界颜色
#
# plt.xlabel('年龄段(每5岁一小段)')
# plt.ylabel('人数')
# plt.title('各年龄段人数分布直方图')
# plt.show()
#





# # 2,pandas模块
#
# import pandas
# import matplotlib
# import matplotlib.pyplot as plt
# import random
#
# #设置中文字体
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
#
# data = pandas.Series([random.randint(0, 100) for i in range(100)])
#
# data.plot(kind='hist',
#           bins=20,
#           color='steelblue',
#           edgecolor='silver',
#           label='直方图')
#
# # data.plot(kind = 'kde',color = 'red',label = '核密度图')
#
# plt.xlabel('年龄段（每5岁一小段）')
# plt.ylabel('人数')
# plt.title('各年龄段人数分布直方图')
#
# plt.show()
#
#





# # 3、seaborn模块
#
# import pandas as pd
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import seaborn as sbn
# import random
#
# # 设置中文字体
# mpl.rcParams['font.sans-serif'] = ['SimHei']
#
# data = pd.Series([random.randint(0, 100) for i in range(100)])
#
# sbn.distplot(data,
#             bins = 20,
#             kde = False,
#             hist_kws = {'color':'black'},
#             label = '年龄分布'
# )
#
# plt.xlabel('年龄段（每5岁一小段）')
# plt.ylabel('人数')
# plt.title('各年龄段人数分布图')
#
# plt.show()







"""   2, 热核密度图
"""
# #1, pandas模块
# import pandas
# import matplotlib
# import matplotlib.pyplot as plt
# import random
#
# #设置中文字体
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
#
# data = pandas.Series([random.randint(0, 100) for i in range(100)])
#
# data.plot(kind='kde',
#           color='steelblue',
#           label='核密度图')
# plt.xlabel('年龄段 (每5周岁一小段)')
# plt.ylabel('人数')
# plt.title('各年龄段人数分布核密度图')
# plt.show()



#seaborn模块

# import pandas as pd
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import seaborn as sbn
# import random
#
# # 设置中文字体
# mpl.rcParams['font.sans-serif'] = ['SimHei']
#
# data = pd.Series([random.randint(0, 100) for i in range(100)])
#
# sbn.distplot(data,
#             bins = 20,
#             kde = True,
#             hist_kws = {'color':'steelblue'},
#             label = '年龄分布')
#
# plt.xlabel('年龄段（每5岁一小段）')
# plt.ylabel('人数')
# plt.title('各年龄段人数分布图')
#
# plt.show()






""" 3, 箱线图
"""
# 缺省





""" 4, 小提琴图
"""
# 缺省






""" 5, 折线图

    对于时间序列数据而言，一般都会使用折线图反映数据背后的超势。通常折线的
横坐标指代日期数据，纵坐标代表某个数值型变量，当然，还可以使用第三个离散变
量对折线图进行分组处理。
    Python中的matplotlib模块和pandas模块实现折线图的绘制。但是seaborn模块也
可以绘制，它的tsplot函数非常不合理，所以不介绍。
"""

#1, matplotlib模块
    # Matplotlib模块中的plot函数可以绘制折线图。
# import pandas
# import matplotlib
# import matplotlib.pyplot as plt
# import random
#
# #设置中文字体
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
#
# data = pandas.Series([random.randint(0, 37) for i in range(7)],
#                  index = ['周一','周二','周三','周四','周五','周六','周日'])
# plt.plot(data.index,
#          data,
#          linestyle='-',
#          linewidth=2,
#          color='steelblue',
#          marker='o',
#          markersize=4,
#          markeredgecolor='brown')
# plt.ylabel('温度')
# plt.title('一周温度变化图')
# plt.show()





# 2,pandas模块

import pandas
import matplotlib
import matplotlib.pyplot as plt
import random

#设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
data = pandas.Series([random.randint(0, 37) for i in range(31)])
data.plot()

plt.ylabel('温度')
plt.xlabel('日期')
plt.title('一月温度变化图')
plt.show()













































