# -*- coding=utf-8 -*-
# Author  : 大白的浅
# Time    : 2019/1/10 0:54
# 描述    : 210773579@qq.com
"""数据导入

"""
'''文本数据

1,txt文件的读取

pandas.read_table()
 --函数的参数:
    filepath_or_buffer: 指定txt文件或者csv文件所在的路径;
    sep: 原数据集中个字段之间的分隔符,默认是Tab制表符;
    header: 是否需要将原数据集中的第一行做为表头,默认第一行用作字段名称;
    names: 如果原数据集没有字段,可以通过该参数在数据集读取时给数据框添加具体的表头;
    index_col: 指定原数据集中的某些列作为数据框的行索引;
    usecols: 指定需要读取原数据集中的那些变量名;
    dtype: 读取数据时,可以为原数据集的第?个字段设置不同的数据类型;
    converters: 通过字段格式,为数据集中的某些字字段设置转换函数;
    skiprows: 读取数据时,指定需要跳过的原数据集开头的行数;    
    skipfooter: 读取数据时,指定需要跳过的原数据集末尾的行数;    
    nrows: 指定读取数据的行数;
    na_values: 指定原数据集中的哪些特征的值做为缺省值;
    skip_blank_lines：读取数据时是否需要跳过空白行，默认为True；
    parse_dates：如果参数值为true，则尝试解析数据框的行索引；如果参数为列表，
            则尝试解析对应的日期列；如果参数是套嵌列表，则将某些列合并为日期列；
            如果参数是字典，则解析对应的列，并生成字段名；
    thousands：指定千分位符；
    comment：指定注释符；
    encoding：如果文件中含有中文，有时需要指定字符编码；
'''
import pandas

huang = pandas.read_table('huang.txt',encoding='utf8')
# print(huang.columns)
# print(huang.head())





'''csv文件的读取

pandas.read_csv()
参数同上
'''
huang = pandas.read_csv('huang.csv')
# print(huang.columns)
# print(huang.head()) #head()函数查看前五,有个参数默认是5,可自定查看个数






'''电子表格数据

'''
#pandas.read_excel()
'''函数的参数:

io：电子表格的具体路径；
sheetname：指定需要读取电子表格中的第几个sheet，既可以传递整数值，
            也可以传递名称；
header：是否需要将原数据集中的第一行做为表头，默认第一行用作字段名称；
skiprows：读取数据时，指定需要跳过原数据集开头的行数；
skipfooter：读取数据时，指定需要跳过原数据集末尾的行数；
index_col：指定原数据集中的某些列作为数据框的行索引；
names：如果原数据集没有字段，可以通过该打参数在数据集读取时给数据框添加具体的表头；
parse_cols：指定需要解析的字段；
na_values：指定原数据集中哪些特征的值做为缺省值；
parse_dates：如果参数值为true，则尝试解析数据框的行索引；如果参数为列表，
                则尝试解析对应的日期列；如果参数是套嵌列表，则将某些列合并为
                日期列；如果参数是字典，则解析对应的列，并生成字段名；
thousands：指定千分位符；
converters：通过字典格式，为数据集中的某些字字段设置转换函数；
convert_float：默认所有的数值内型都转换成浮点型。
'''
huang = pandas.read_excel('huang.xls')
# print(huang.columns)
print(huang.head())








"""数据库数据
"""
'''数据导出:

1, 导出为csv文件
obj.to_csv(file_path, sep=',', index=True, header=True)
参数:
    file_path：文件路径；
    sep为分隔符，默认是逗号；
    index表示是否导出行号，默认是True；
    header：表示是否导出列名，默认是True；


2, 导出为Excel文件
obj.to_excel(file_path,  index = True, header = True)
参数:
    file_path：文件路径；
    index表示是否导出行号，默认是True；
    header：表示是否导出列名，默认是True；
'''






'''类型转换

'''



















































































