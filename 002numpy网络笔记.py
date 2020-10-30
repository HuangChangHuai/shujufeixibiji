# -*- coding=utf-8 -*-
# Author  : 大白的浅
# Time    : 2019/1/8 0:35
# 描述    : 210773579@qq.com
import numpy

'''数据类型对象(dtype)

数据类型对象描述了对应于数组的固定内存块的解释,取决于以下方面:
    -数据类型 (整数, 浮点型 或者 Python对象)
    -数据大小
    -字节序 (小端或大端)
    -在结构化类型的情况下,字段的名称,每个字段的数据类型和每个字段占用的
        内存块部分
    -如果数据类型是子序列,它的形状和数据类型

字节顺序取决于数据类型的前缀 < 或 >:
     < 意味着编码是小端(最小有效字节存储在最小地址中);
     > 意味着编码是大端(最大有效字节存储在最小地址中)


#dtype 可由一个语法构造:
numpy.dtype(object, align, copy)
     参数为:
        object: 被转换为数据类型的对象
        align: 如果为True,则向字段添加间隔,使其类似于C的结构体
        copy: 生成dtype对象的新副本，如果为flase，结果是内建数据类型对象的引用

'''
'''数据类型及描述

1.	bool_ 存储为一个字节的布尔值（真或假）
2.	int_ 默认整数，相当于 C 的long，通常为int32或int64
3.	intc 相当于 C 的int，通常为int32或int64
4.	intp 用于索引的整数，相当于 C 的size_t，通常为int32或int64
5.	int8 字节（-128 ~ 127）
6.	int16 16 位整数（-32768 ~ 32767）
7.	int32 32 位整数（-2147483648 ~ 2147483647）
8.	int64 64 位整数（-9223372036854775808 ~ 9223372036854775807）
9.	uint8 8 位无符号整数（0 ~ 255）
10.	uint16 16 位无符号整数（0 ~ 65535）
11.	uint32 32 位无符号整数（0 ~ 4294967295）
12.	uint64 64 位无符号整数（0 ~ 18446744073709551615）
13.	float_ float64的简写
14.	float16 半精度浮点：符号位，5 位指数，10 位尾数
15.	float32 单精度浮点：符号位，8 位指数，23 位尾数
16.	float64 双精度浮点：符号位，11 位指数，52 位尾数
17.	complex_ complex128的简写
18.	complex64 复数，由两个 32 位浮点表示（实部和虚部）
19.	complex128 复数，由两个 64 位浮点表示（实部和虚部）

NumPy 数字类型是dtype（数据类型）对象的实例，每个对象具有唯一的特征。
    这些类型可以是np.bool_，np.float32等。


'''


# 示例一:
# 使用数组标量类型
import numpy

dt = numpy.dtype(numpy.int32)
# print(dt) #int32


# 示例二:
# int8, int16, int32, int64 可替换为等价的字符串'i1', 'i2', 'i4',以及其他
dt1 = numpy.dtype('i4')
# print(dt1) #int32


# 示例三:
# 使用端记号
dt2 = numpy.dtype('>i4')
# print(dt2) #>i4


# 示例四:
# 首先创建结构化数据类型
dt3 = numpy.dtype([('age', numpy.int8)])
# print(dt3) #[('age', 'i1')]


# 示例五:
# 现在将其应用于ndarray对象
dt4 = numpy.dtype([('age', numpy.int8)])
a = numpy.array([(10,), (20,), (30,)], dtype=dt2)  # 这里几个dt有不同的效果
# print(a)


# 示例六:
# 文件名称可用于访问 age 列的内容
dt = numpy.dtype([('age', numpy.int8)])
a = numpy.array([(10,), (20,), (30,)], dtype=dt)
# print(a['age']) #[10 20 30]


# 示例七:
# 以下示例定义名为 student 的结构化数据类型，其中包含字符串字段name，整数字段age
# 和浮点字段marks。 此dtype应用于ndarray对象。
student = numpy.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
# print(student) #[('name', 'S20'), ('age', 'i1'), ('marks', '<f4')]


# 示例八:
student = numpy.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
a = numpy.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
# print(a) #[(b'abc', 21, 50.) (b'xyz', 18, 75.)]


'''每个内建类型都有一个唯一定义它的字符代码:
'b' : 布尔值
'i' : 符号整数
'u' : 无符号整数
'f' : 浮点
'c' : 复数浮点
'm' : 时间间隔
'M' : 日期间隔
'O' : Python对象
'S','a' :字节码
'U' : Unicode
'V' : 原始数据(void) 
'''