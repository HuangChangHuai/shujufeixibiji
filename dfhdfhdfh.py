# -*- coding=utf-8 -*-
# Author  : 大白的浅
# Time    : 2019/1/8 18:22
# 描述    : 210773579@qq.com

import pandas  #导入pandas
import matplotlib.pyplot as plt
# 处理中文乱码
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
#构造数据

hqy_data = pandas.read_excel(r'G:\Huang\DataForGroup2.xls') #导入Excel，赋值给hqy_data
#hqy_df1 = hqy_data['姓名'] #导入姓名列赋值给hqy_df1
hqy_df2 = hqy_data['语文'] #导入语文列赋值给hqy_df2
hqy_df3 = hqy_data['数学']
hqy_df4 = hqy_data['英语']
hqy_df5 = hqy_data['化学']
hqy_df6 = hqy_data['生物']
hqy_df7 = hqy_data['物理']
hqy_df8 = hqy_data['历史']
hqy_df9 = hqy_data['地理']
concat = pandas.concat([hqy_df2,hqy_df3,hqy_df4,hqy_df5,hqy_df6,hqy_df7,hqy_df8,hqy_df9],axis=1)
#把姓名列和语文列拼接结果赋值给concat变量
labels = ['语文','数学','英语','化学','生物','物理','历史','地理']
# print(concat)

#绘制饼图
plt.pie(x = concat,                # 数据
        labels = labels,         # 标签
        autopct = '%.2f%%',       # 格式
        )
plt.show()
print()