# -*- coding=utf-8 -*-
# Author  : 大白的浅
# Time    : 2019/1/10 2:02
# 描述    : 210773579@qq.com

"""数据抽取
"""
'''字段抽取

    字段抽取是指抽出某列上指定位置的数据做成新的列，其命令格式如下：
slice(start, stop)
    start：表示开始位置；
    stop：表示结束位置；
  比方抽取手机号字段的前3位，识别服务商品牌，中间4位作为识别号码地区，
最后4位显示用户看。
'''
import pandas

#导入的电话号码可能是个数值类型
data = pandas.read_csv('huang.csv')
data['手机'] = data['手机'].astype(str)

bands = data['手机'].str.slice(0,3)
areas = data['手机'].str.slice(3,7)
users = data['手机'].str.slice(7,11)
# print(bands)






'''字段拆分

字段拆分是指按着指定的字符sep，拆分已有的字符串，其命令格式如下：
split(sep, n, expand = true)
sep：表示用于分隔字符串的分隔符；
n：表示分割后新增的列数；
expand：表示是否展开为数据框，默认为false。
返回值： expand为true，返回DataFrame; expand为false，返回Series;
'''
data = pandas.read_excel('huai.xlsx')
# print(data.head())
# print(data['name'])

newdata = data['IP'].str.split('.',2,True)
newdata = columns = ['IP1', 'IP2', 'IP3-4']
# print(newdata)
#不知道为什么没有实现这个效果:
#    IP1  IP2   IP3-4
# 0  202  134  122.29
# 1  202  133  132.26
# 2  202  132  142.24
# 3  202  131  152.22





'''重置索引

重置索引是指指定某列为索引,以便于对其他数据进行操作,其命令格式如下:
 df.set_index('列名')
'''





'''条件抽取数据

    记录抽取指根据一定的条件，对数据进行抽取。其命令格式如下：
df[condition]
说明:
    condition：表示过滤条件。
    返回值：DataFrame
    常用的condition类型有：
        （1）比较运算：==、<、>、<=、>=、!=
        （2）范围运算：between(left, right)
        （3）空置运算：pandas.isnull(column)
        （4）字符匹配：str.contains()
        （5）逻辑运算：&、|、not
'''
huang = pandas.read_csv('huang.csv')
# print(huang[huang['化学']>95])
# print(huang[huang['历史'].between(90,95)])
# print(huang[(huang['化学'] > 99) & (huang['历史']>85)])







'''索引抽取数据

    在Pandas模块中实现数据框子集的获取可以使用iloc、loc和ix三种方法，这三种方
法既可以对数据进行筛选，也可以实现对变量进行挑选，
它们的语法可以表示成[rows_select, cols_select]

1、通过索引名:
df.loc[行标签, 列标签]
    注意，这里的标签不是索引。
    第一个参数是行标签，第二个参数是列标签，它是可选参数，默认是所有的标签。   
    如果两个参数都为列表，则返回DataFrame，否则返回Series。
    
    同时抽取多行时，行的索引必须使用列表的形式，而不能简单地用逗号分隔，
如抽取第一行和第二行，
    应该用df.loc[[1, 2]]，而不要用df.loc[1, 2]



2、通过索引号:
df.iloc[行索引号，列索引号]
    iloc只能通过行号和列号进行数据筛选，读者可以将iloc中的i理解为“integer”，
即只能向[rows_select, cols_select]指定定整数列表。
    该索引方式与数组的索引方式类似，都是是从0开始，可以间隔取号。



3、Ix方法
Ix是iloc和loc的结合体，根据索引号或者索引名都可以，
但是当索引名是int类型时，只能用索引名索引。

'''







'''数据修改:

    修改数据是常有的事，比如数据串中的有些需要整体替换，有些需要个别修改等情况
经常会出现。

1、整体替换
    整行整列的替换，很容易做到。
    df[‘数学’] = score_2，score_2就是将要被填进去的数据列，可以是列表，
也可以是Series。


2、单值替换
    命令格式：df.replace(‘B’, ’A’)
    用A替换B
'''
Data = pandas.DataFrame({'班级':[2,1,2,1,2,1,2,1,2,1],
                     '姓名':['  张一','张二','张三','张四','张五','张六','张七','张八','张九','张十'],
                     '性别':['男', '男', '女', '女', '女', '女', '男', '男', '女', '男'],
                     '语文':[60,65,57,83,76,84,90,'作弊',67,88],
                     '数学':[91,95,'缺考',88,84,83,87,100,68,79],
                     '历史':[91,93,92,95,94,92,90,89,98,97]})
# print(Data)

newdata1 = Data.replace('缺考',0)
# print(newdata1)
newdata2 = newdata1.replace('作弊',-1)
# print(newdata2)





'''指定列的单值替换

命令格式:   df.replace({‘数学’: ‘缺考’}, 0)
            df.replace({‘数学’: ‘缺考’ , ‘英语’ : ‘作弊’}, 0)
第一个语句是用0来代替数学成绩中的缺考，后一个语句还用0来代替英语中的作弊。



多值替换:

格式: df.replace(['huang','huai'], ['peng','dan'])
#用peng和dan来代替huang和huai
'''






'''重置索引

1, set_index

data.set_index(keys, drop=True, append=False, inplace = False)
说明:
    append = True时,保留原索引并添加新索引;
    drop = False时,保留被作为索引的列;默认情况下,设置为索引的列会从数据框中删除;
    inplace=True时,在原数据集上修改; 
    
2,reset_index
    还原索引,使索引重新变为默认的整形索引;
    它是set_index的逆运算
'''






"""透视表

透视表就是应用 pandas.piovt_table 方法:
pivot_table(values, index, columns, aggfunc, fill_value)
参数说明：
    values：表示数据透视表中的值；
    index：表示数据透视表中的行；
    column：表示数据透视表中的列；
    aggfunc：统计函数，fill_value表示NA值的统一替换。
    fill_valve：指定一个标量，用于填充缺失值
"""

#1,最简单的透视,一个数据框,一个索引,选用'班级'做索引吗,
#       默认的统计函数采用的是平均值
mydata = pandas.DataFrame({
    '班级':[2,1,2,1,2,1,2,1,2,1],
    '性别': ['男', '男', '女', '女', '女', '女', '男', '男', '女', '男'],
    '姓名':['张一','张二','张三','张四','张五','张六','张七','张八','张九','张十'],
    '语文':[60,65,57,83,76,84,90,75,67,88],
    '数学':[91,95,93,88,84,83,87,100,68,79],
    '历史':[91,93,92,95,94,92,90,89,98,97],
    '总分':[242,253,242,266,254,259,267,264,233,264],
    '评价':['中','中','中','优','良','优','优','优','中','优']})
# print(mydata)
# print('----------------分割线----------------')
# print(pandas.pivot_table(mydata, index=['班级']))




#2,选用两个索引, '班级'和 '性别', 它已经开始通过将 '班级'列和 '性别'列进行对应分组,
#   来实现数据聚合和总结
# print(pandas.pivot_table(mydata,index=['班级', '性别']))
# print(pandas.pivot_table(mydata,index=['班级', '性别', '总分']))





#3,如果我们只关心 '总分'和'数学', '历史'和'语文'不感兴趣,可设置values属性

# print(pandas.pivot_table(mydata, index=['班级','性别'], values=['总分','数学']))





# 4,如果除开平均数,我对其他的统计数据也有兴趣,可以设置 aggfunc 参数,
# aggfunc可以包含很多函数:
import numpy
# print(pandas.pivot_table(mydata, index=['班级','性别'],
#                          values=['语文','数学','历史'],
#                          aggfunc=[numpy.mean, numpy.sum]))#mean()计算平均值
'''为了对你选择的不同值执行不同的函数,你可以向aggfunc传递一个字典,字典的键就会
作为函数名的标签,那必须将标签做的更加简洁'''
#这是什么意思....





#5, 'columns'属性的应用:
# print(pandas.pivot_table(mydata, index=['班级','评价'],
#                          values=['语文','数学'],
#                          columns=['性别'],
#                          aggfunc=[numpy.mean]))







"""合并链接

1, 记录合并

    记录合并就是指两个结构相同的数据框合并成一个数据框，也就是在一个数据框中
追加另一个数据的数据记录。
命令格式：
Concat([dataframe1 , dataframe2,……])
    返回一个新的数据框
"""






'''2,字段合并

字段合并是指同一个数据框中的不同列进行合并，形成新的列。
命令格式：
X = x1 + x2 + ……
    返回值是Series，要求合并成的序列长度一致。



data = data.astype(str)
phone = data['bands'] + data['areas'] +data['tells']
data['phone'] = phone
'''







'''3、字段匹配

    字段匹配是指不同结构的数据框，按着一定的条件进行匹配合并。有两个数据表，
第一个表中有学号、姓名，第二个表中有学号、手机号，现需要整理一份数据表，
包含学号、姓名、手机号，此时就可以用到merge函数。

命令格式：
Merge(x , y , left_on , right_on)
    X表示第一个数据框；
    y表示第二个数据框；
    left_on表示第一个数据框中用于匹配的列；
    right_on表示第二个数据框用于匹配的列。返回DataFrame
'''
data1 = pandas.DataFrame({'班级':[2,1,2,1,2,1,2,1,2,1],
                     '姓名':['  张一','张二','张三','张四','张五','张六','张七','张八','张九','张十'],
                     '性别':['男', '男', '女', '女', '女', '女', '男', '男', '女', '男'],
                     '语文':[60,65,57,83,76,84,90,75,67,88],
                     '数学':[91,95,93,88,84,83,87,100,68,79]
                     })

data2 = pandas.DataFrame({'班级':[2,1,2,1,2,1,2,1,2,1],
                     '姓名':['  张一','张二','张三','张四','张五','张六','张七','张八','张九','张十'],
                     '性别':['男', '男', '女', '女', '女', '女', '男', '男', '女', '男'],
                     '物理':[60,65,57,83,76,84,90,75,67,88],
                     '地理':[91,95,93,88,84,83,87,100,68,79]
                     })

# print(pandas.merge(data1,data2, left_on='姓名',right_on='姓名'))







"""     分组聚合

    数据分组是指根据数据分析对象的特征，按着一定的数据指标，把数据划分为不同
的区间来进行研究，以揭示其内在的联系和规律性。简单地说，就是新增一列，
将原来的数据按照其性质归入新的类别中。

其命令格式如下：
cut(series , bins , ritht = True , labels = null)
    其中：
        series表示需要分组的数据；
        bins表示分组的依据数据；
        right表示分组的时候右边是否闭合；
        labels表示分组的自定义标签，可以不自定义；
        
        
bins = [min(data.English)-1 , 60,70,80,max(data.English)+1]
labs = ['不及格','及格','中等','良好','优秀']
demo = pd.cut(data.English ,bins ,right = False ,labels = labs)

#代码和前面的素材不一样
        
        
"""




















































































































































































