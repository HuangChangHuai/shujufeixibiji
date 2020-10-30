# -*- coding=utf-8 -*-
# Author  : 大白的浅
# Time    : 2019/1/8 13:19
# 描述    : 210773579@qq.com

'''Pandas

    Pandas是Python的一个数据分析包，它最初是被作为金融数据分析工具而开发出来的，
所以，它对时间序列提供了非常好的支持。它所包含的数据结构和数据处理工具的设计使
得在Python中进行数据清洗和分析非常的方便，
    Padas做为强大的数据处理模块，它可以帮助数据分析师轻松地解决数据的预处理问题，
如数据类型的转换、缺失值处理、描述性统计分析、数据汇总等。
    Pandas提供了高级数据结构和函数，这些数据结构和函数的设计使得利用结构化、
表格化数据的工作快速、简单、有表现力。它将表格和关系型数据库的灵活数据操作能力
与numpy的高性能数组计算的理念相结合，它提供了复杂的索引函数，
使得数组重组、切块、切片、聚合、子集选择更为容易。
    Pandas经常是和其它的数值计算工具结合使用，如numpy、Scipy以及数据可视化工
matplotlib。
    Pandas采用了很多的numpy代码风格，不同的是Pandas是用来处理表格型或者异质型
数据的，
而numpy则是更适合用来处理同质型的数值类型数据。
Pandas的数据结构是Series、DataFrame、Panel。


（1）Series：一维数组系列，也可称序列，与Numpy中的一维数组类似，
二者也与Python中基本的数据结构list相近。用于存储一行或一列的数据，
以及与之相关的索引的集合。

（2）DataFrame：二维的表格型数据结构，用于存存储多行多列的数据集合，
可以将DataFrame理解为Series的容器。类似于excel的二维表格。

（3）Panel：三维数组，可以理解为DataFrame的容器。
序列可以理解为数据集中的一个字段，数据框是指含有至少两个字段。

'''



'''序列

Series对象本质上是一个numpy数组，因此，numpy数组处理函数可以直接对Series
进行处理。它是一种一维的数组型型对象，它包含一个值序列，并且包含了一个值序列，
并且包含了数据标签，称之为索引。所以，Series除了可以使用位置作为下标存取元素
之外，还可以使用标签存取元素，这一点和字典类似。
每一个Series对象实际上都由下面两个数组组成：

（1）index：它是从numpy数组继承的index对象，保存标签信息；
（2）values：保存值的数组。
注意：
（1）Series是一种类似于一维数组的对象；
（2）它的数据类型没有限制，可以保存多种数据类型；
（3）它有索引，把索引当做数据的标签看看待，类似于字典；
（4）它同时具有数组和字典的功能，因此也支持字典的一些方法。

如果需要对序列进行数学函数的运算，一般选用numpy模块，pandas模块在这方面比较
缺乏。如果要对序列做统计运算，既可以用numpy模块，也可以用序列的方法，
而且，序列的方法更加丰富。
'''


'''构建

可以用以下的方式构造一个序列:
序列也可以使用以下语法定义,默认的索引是0,1,2,3,4,5....
Series([data1, data2, data3,...], index=[index1, index2, index3,....])

（1）通过同质的列表或者元组构建；
（2）通过字典构建；
（3）通过Numpy中的一维数组构建；
（4）通过DataFrame中的某一列构建；
'''

import numpy
import pandas

myseries1 = pandas.Series([2.8, 3.01, 8.99, 8.59, 5.28])
myseries2 = pandas.Series({'北京':2.8, '上海':3.01, '广东':8.99,
                           '江苏':8.59, '浙江':5.28})
# print(myseries1)
# print(myseries2)

'''
   序列的打印结果有两列，第一列属于序列的行索引，可理解为行号，自动从0开始，
第二列才是序列的实际值。通过字典构建的序列，它的第一列不再是行号，而是具体
的行名称，对应到字典中的键，第二列是序列的实际值，对应到字典中的值。
   我们可以通过序列的索引属性indexs和values属性分别获取序列对象的索引和值。
   从另外一个角度考虑Series，可以认为它是一个长度固定且有序的字典，因为它将
索引和数据值按位置配对，在可能会使用字典的上下文当中，也可以使用Series。


Series对象本身及其索引index都有name属性。
'''
import pandas

data = pandas.Series(['AA','BB','CC','DD'], index=['a','b','c','d'])
data.name = 'huang_testseries'
data.index.name = 'label'
# print(data)





'''访问

   序列与一维数组有极高的相似性，获取一维数组元素的所有索引方法都可以应用
在序列上，而且数组的数学和统计函数也同样可以应用到序列上，
而且，序列还有更多的其它处理方法。
'''
# print('行号风格的序列: \n', myseries1[[0,3,4]])
# print('行名称风格的序列：\n', myseries2[[0,3,4]])
# print('行名称风格的序列：\n', myseries2[['上海','江苏','浙江']])
# print('通过numpy方法：\n', numpy.log(myseries1))
# print('通过numpy方法：\n', numpy.mean(myseries1))
# print('通过序列的方法：\n', myseries1.mean())




'''追加

序列不可以追加单个元素，但可以追加序列。
'''
myseries3 = pandas.Series(['一', '二', '三', '四', '五'],
                          index=[1,2,3,4,5])

#不能追加单个元素
# #myseries3.append('六')

myseries4 = pandas.Series(['六'])
myseries5 = myseries3.append(myseries4)
# print(myseries5)





'''删除

通过索引名或者索引号删除，删除多个条目可以把索引放在一个列表当中。
'''
series1 = pandas.Series(['一','二','三','四','五'],
                        index=['first','second','third','forth','fifth'])

series2 = pandas.Series(['一','二','三','四','五'])
# print(series1)

series3 = series1.drop('second')
# print(series3)

series4 = series2.drop(0)
# print(series4)





'''更新

访问直接赋值
'''





'''排序

    Series的sort_index(ascending=True)方法可以对index进行排序，
ascending参数用于控制升序或降序，默认为升序。
'''




























































