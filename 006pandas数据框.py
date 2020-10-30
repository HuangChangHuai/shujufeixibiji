# -*- coding=utf-8 -*-
# Author  : 大白的浅
# Time    : 2019/1/8 14:37
# 描述    : 210773579@qq.com
'''构建

    数据框实际上是一个数据集，它的行代表一条观测，数据集的列代表各个变量，
在一个数据框中可以存放不同的数据类型，而数组和序列没有这样的优势，
它们只能存放同质的数据。

构造一个数据框可以用如下的方式：

（1）通过套嵌列表或元组构造；
（2）通过字典构造；
（3）通过二维数组构造；
（4）通过导入外部数据构造；
'''
import numpy
import pandas

mydata1 = pandas.DataFrame([['张三', 23, '男'], ['李四', 21, '女']])
mydata2 = pandas.DataFrame({'姓名':['张三', '李四', '王二'],
                            '年龄':[23,21,26],
                            '性别':['男','女','女']})
mydata3 = pandas.DataFrame(numpy.array([['张三',23,'男'],
                                        ['李四',21,'女'],
                                        ['王二',26,'女']]))
# print('嵌套列表构造: \n',mydata1)
# print('字典构造: \n', mydata2)
# print('二维数组构造: \n', mydata3)

'''

   构建的DataFrame会为自动为Series分配索引，并且列会按着排序的顺序排列。
DataFrame也可能通过index来设置各行的索引。
如果DataFrame的索引和列拥有name属性，
   它也是一个values属性和columns属性
'''






'''访问

访问列：    变量名[列名]
访问行：    变量名[n: m]
访问块：    变量名.loc[[行名],[列名]]
            变量名.iloc[n1: n2,m1: m2]
            变量名.iloc[[],[]]     
指定位置：   变量名.at[行名，列名]
'''
import numpy
import pandas

data = [['张三', 23, '男', 55], ['李四', 21, '女', 60],
        ['王二', 26,'男',65], ['李淮', 18, '男', 68]]
mydata_a = pandas.DataFrame(data, index=['a','b','c','d'],
                            columns=['name','age','sex','weight'])

# print('原数据: \n', mydata_a)
#
## print('访问单列: \n', mydata_a['name'])
## print('访问多列: \n', mydata_a[['name', 'age']])
##
## print('访问行: \n',mydata_a[0:2])
## print('loc 访问块: \n',mydata_a.loc[['a', 'b'], ['name', 'weight']])
## print('iloc访问块1: \n', mydata_a.iloc[0:2, 1:4])
## print('iloc访问块2: \n', mydata_a.iloc[[0,1,3], [1,3]])
##
## print('访问指定位置: \n',mydata_a.at['a','name'])





'''增加

1、增加列
如果被赋值的列不存在，则会生成一个新的列。
mydata1['phone'] = ['131********','132********',
                    '133********','134********']

2、增加行
mydata1.loc['e'] = ['尹红',26,'女',68]

3、append方法
   append方法可以添加数据到一个dataframe中，注意append方法不会影响原来
的dataframe，会返回一个新的dataframe。所以要拿一个新的变量来接收它

语法：
    DataFrame.append(otherData, ignore_index=False, verify_integrity=False)
 其中otherData参数是要添加的新数据，支持多种格式。
    ignore_index 参数默认值为False，如果为True，会对新生成的dataframe使用
新的索引（自动产生），忽略原来数据的索引。
    verify_integrity参数默认值为False，如果为True，当ignore_index为False时，
会检查添加的数据索引是否冲突，如果冲突，则会添加失败。
'''
data2 = [['张三1',23,'男',55],['李四1',21,'女',60],
         ['王二1',26,'女',65],['赵大1',26,'女',68]]

mydata_b = pandas.DataFrame(data2, index=['f','g','h','i'],
                            columns=['name','age','sex','weight'])

# # print(mydata_b)
# mydata_c = mydata_a.append(mydata_b)
# print(mydata_c)
#
# mydata_d = mydata_a.append(mydata_b.loc['h'])
#
# print(mydata_d)






'''删除


    可以利用drop方法根据行标签删除值，如果删除多个，可以把行标签放在一个
列表中。
    也可以能过传递axis=1或者axis=’columns’从删除列。del方法可以用于移除
DataFrame的列，del frame[name]。
'''
import numpy
import pandas

data_a = [['张三',23,'男'],['李四',21,'女'],['王二',26,'女']]
mydata_A = pandas.DataFrame(data_a, index=['A','B','C'],
                            columns=['name', 'age', 'sex'])

# print('原数据: \n',mydata_A)

mydata_B = mydata_A.drop('B')
# print('删除行B数据: \n', mydata_B)
# print('原数据: \n',mydata_A)

mydata_C = mydata_A.drop('sex',axis= 1) #没有axis会报错, KeyError: "['sex'] not found in axis"
# print('删除性别数据: \n',mydata_C)
# print('原数据: \n',mydata_A)


del mydata_A['age']
# print('删除年龄数据: \n',mydata_A)




'''更新

1、修改指定行或单元格数据

#其中i是行号，j是列号，都是从0开始
df.iloc[i][j]= xxx

# 这样把指定列的所有数据都设置为同一个值。注如果指定的列不存在，会新增加列。
df['a'] = 12  

    DataFrame中选择的列是数据的视图，不是拷贝，如果需要复制，则应当显式地使
用Series的copy方法。
'''





"""基本操作

"""
'''重建索引

    1、Series可以使用reindex方法重新排序，如果调用reindex重排数据，使得它
符合新的索引，如果索引值不存在，就会引入缺失数据值。
'''
import pandas

dataA = pandas.Series([1.1,2.2,3.3,4.4,5.5], index=['b','a','c','e','d'])
# print(dataA)

dataB = dataA.reindex(['a','b','c','d','e','f'])
# print(dataB)




'''DataFrame

    reindex可以改变 行索引, 列索引, 也可以同时改变二者,
当仅传入一个序列时,结果中的行会重建索引
'''
dataC = [['张三',23,'男'],['李四',21,'女'],['王二',26,'女']]


mydataC = pandas.DataFrame(dataC, index=['d','c','a'],
                           columns=['name','age','sex'])
# print('原数据: \n',mydataC)

mydataD = mydataC.reindex(['a','b','c','d'])
# print('reindex处理: \n',mydataD)


state = ['sex', 'name', 'age']
mydataE = mydataC.reindex(columns = state)
# print('columns数据: \n',mydataE)




mydataF = mydataC.loc[['a','c','d'],state]
print('loc数据: \n',mydataF)

































































































