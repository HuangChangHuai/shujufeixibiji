# -*- coding=utf-8 -*-
# Author  : 大白的浅
# Time    : 2019/1/10 1:37
# 描述    : 210773579@qq.com
"""数据清洗

    在数据分析时，海量的原始数据存在着大量的不完整、不一致、有异常的数据，严重影响
到数据分析的结果，所以进行数据清洗显得尤为重要。数据清洗是数据价值链中最关键的步骤。
垃圾数据，即使是通过最好的分析，也将产生错误的结果，并误导业务本身。
    因此，在数据分析过程中，数据清洗占据很大的工作量。
    数据清洗就是处理缺失数据以及清除无意义的信息，如删除原始数据集中的无关数据、
重复数据，平滑噪声数据，筛选掉与分析主题无关的数据，处理缺失值、异常值。
"""

'''重复值处理

Pandas模块中去掉重复数据的步骤如下：

（1）利用DataFrame中的duplicated方法返回一个布尔型的Series，显示是否有重复行，
        没有重复行显示为Fasle，有重复行的则从重复的第二行起显示为True。
（2）再利用DataFrame中的drop_duplicates方法返回一个移除了重复行的DataFrame。

duplicated方法的格式如下：
obj.duplicated(self, subset = None, keep = ‘first’)
参数说明：
    subset：用于识别重复的列标签或列标签序列；
    keep = ‘first’：表示除第一次出现外，其余相同的数据被标记为重复；
    keep = ‘last’：表示除最后一次出现外，其余相同的数据被标记为重复；
    keep = False：表示相同的数据被标记为重复；
'''
import numpy
import pandas

data = [['张三',23,'男',55],['李四',21,'女',60],
        ['王二',26,'女',65],['张三',26,'女',68]]
mydata1 = pandas.DataFrame(data, index=['a','b','c','d'],
                           columns=['name','age','sex','weight'])
# print(mydata1.duplicated('name'))
# print(mydata1.drop_duplicates('name'))









'''缺省值处理

    从统计上说，缺失的数据可能会产生有偏估计，从而使样本数据不能很好地代表总体，
而现实中的绝大部分数据都包含缺失值，因此，处理缺失值非常的重要。
    处理缺失值分为两个步骤，缺失数据的识别和缺失数据的处理。

1、缺失数据的识别
    Pandas使用浮点值NaN表示浮点和非浮点数组里的缺失数据，并使用isnull()方法，
和notnull()方法来判断缺失情况。
'''
data = pandas.read_csv('huang.csv')
# print('原数据: \n',data.head()) #如果缺失,那个位置打印NaN
# print('isnull输出: \n', data.isnull())  #如果缺失,那个位子True
# print('notnull输出: \n', data.notnull()) #如果缺失,那个位子False





'''
2、缺失数据的处理
对于缺失数据的处理方式，有数据补齐、删除对应行、不处理几种方式。

（1）dropna()：去除数据结构中值得为空白的行。
  可以指定参数how = ‘all’，表示只有行里的数据全部都是空时才丢弃。如果想以相同的
方式按列丢弃，可以传入axis=1。
'''
newdata = data.dropna()
newdata = data.dropna(axis=1)

'''
（2）fillna()：有其它数据来代替NaN。
    有时候，直接删除数据会影响分析的结果，可以对数据进行填补。
A、用前一个数据值替代，fillna(method = ‘pad’)
B、用后一个数据值替代，fillna(method = ‘bfill)
C、用平均数来替代，fillna(df.mean())
D、df.fillna(df.mean()[‘填补列名’:’计算均值的列名’])：使用别的列的均值进行处理
E、Df.fillna({‘列名1’:值1,’列名2’:值2})：可以传入一个字典，对不同的值填充不同
    的值。
'''
# newdata = data.fillna('?')
# newdata = data.fillna(method='pad')
# newdata = data.fillna(method='bfill')
# newdata = data.fillna(data.mean())
newdata = data.fillna({'数学':100,'物理':99})
print(newdata)





'''异常值处理

1、清除字符型数据左右指定的字符，默认为空格
    应用strip()函数删除左右两边的空格；
    应用rstrip()函数删除左右两边的空格；
    应用lstrip()函数删除左右两边的空格；
'''
# print(data['姓名'].str.strip())
# print(data['姓名'].str.rstrip())
# print(data['姓名'].str.lstrip())





'''
   2、真正的异常值是指那些远离正常值的观测值，也就是不群的观测。导致异常值的出
现一般是人为的记录错误或者是设备的故障等。异常值的出现会对模型的创建和预测产生
严重的后果。

   当然，异常值也不一定是坏事，有些情况下，通过寻找异常值就能给企业带来良好的
发展，如销毁“钓鱼”网站、关闭“薅羊毛”用户的权限等。
   对于异常值的检测，一般采用两种方法：一种是n个标准差法，另一种是箱线图判别法。
'''




































































































