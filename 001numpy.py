# -*- coding=utf-8 -*-
# Author  : 大白的浅
# Time    : 2019/1/7 15:31
# 描述    : 210773579@qq.com

#numerical python (numpy) 数学的Python??

'''
    NumPy，是Numerical Python的简称，它是目前Python数值计算中最为重要的基
础包，是python数值计算的基石，它提供了多种数据结构、算法以及大部分涉及Python
数值计算所需要的接口。NumPy模块的核心就是基于数组的运算，相比于列表或其它数
据结构，数组的效率是最高的。NumPy的设计对含有大量数组的数据非常有效，它的方法
比是Python方法要快10倍到100倍。大多数的计算包都提供了基于NumPy的科学函数功能，
将NumPy的数组对象做为数据交换的数据容器。
    NumPy本身并不提供建模和数学函数，许多python的数值计算工具将numpy数组作
为基础数据结构，或者与Numpy进行无缝互操作。理解NumPy的数组以及基于数组的计算
将帮助你更高效地使用基于数组的工具，如Pandas。虽然NumPy提供了操作数值数据的
基础，但是大多数人还是想把Pandas做为统计分析的基石。
'''




#----------------------------------------------------------------------
'''数组创建

    通过 numpy 模块中的 array() 函数的实现数组的创建,如果向函数传入一个列表
或者元组,将构造简单的一维数组;
如果向函数传入对个嵌套列表或者数组,则可以构造出一个 二维数组
    一个 ndarray 或者说是一个多维数组,它是一个通过的多维数据容器,构造数组
的元素是同质的,数组中的每一个值都具有相同的数据类型
'''


'''一维数组

'''
import numpy

arr1 = numpy.array([1,2,3,4,5,6,7,8,9])
arr2 = numpy.array([5,4,3,2,1,'huang'])
# print('一维数组arr1:', arr1, type(arr1))
# print('一维数组arr2:', arr2, type(arr2))




'''二维数组

'''
arr3 = numpy.array([[1,2,3,4,5],[5,4,3,2,1],
                    ['a','b','c','d','e'],['e','d','c','b','a']])
# print('二维数组 arr3: \n', arr3)
# print(type(arr3))



'''三位数组

'''
arr4 = numpy.array([[[1,2,3],[4,5,6],[7,8,9]],
                    [['a','b','c'],['d','e','f'],['g','h','i']],
                    [[9,8,7],[6,5,4],[3,2,1]],
                    [['i','h','g'],['f','e','d'],['c','b','a']]
                    ])
# print('三维数组:\n',arr4)







#---------------------------------------------------------------------



'''numpy模块下的数组生成函数


array(p_object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
    --将输入数据转换为ndarray,可以是列表,元组,数组以及其他序列,默认复制
        所有数据
    --参数描述:
        object: 任何暴露数组结婚口方法的对象都会返回一个数组或任何(嵌套)序列;
        dtype: 数组的所需数据类型,可选;
        copy: 可选,默认为True,对象是否被复制;
        order: 'C'-按行, 'F'-按列, 'A'-任意;
        subok: 默认情况下,返回的数组被强制为基类数组,如果为True,则返回子类;
        
        

asarray(a, dtype=None, order=None)
    --将输入转换为ndarray,但如果输入已经是ndarray则不再复制
    
arange(start=None, stop=None, step=None, dtype=None)
    --python内建函数range的数组版,返回一个数组
    
ones(shape, dtype=None, order='C')
    --根据给定的形状和数据类型生成全1数组

ones_like(a, dtype=None, order='K', subok=True)
    --根据所给的数组生成一个一模一样的全1数组
    
zeros(shape, dtype=None, order='C')
    --根据给定的形状和数据类型生成全0数组
    
zeros_like(a, dtype=None, order='K', subok=True)
    --根据所给定的数组生成一个一模一样的全0数组

empty(shape, dtype=None, order='C')
    --根据给定的形状生成一个没有厨师化值得空数组
    
empty(prototype, dtype=None, order='K', subok=True)
    --根据所给定的数组生成一个一模一样的单数没有初始化的空数组

full(shape, fill_value, dtype=None, order='C')
    --根据给定的形状和数据类型生成指定数值的数组

full_like(a, fill_value, dtype=None, order='K', subok=True)
    --根据给定的数组生成一模一样单数指定数值的数组

eye(N, M=None, k=0, dtype=float, order='C')
identity(n, dtype=None)
    --生成一个特殊矩阵,对角线全是1,其他都是0

'''
#array()上面已经有了,

#asarray()
huang_asarray = numpy.asarray(['huang','chang','huai'])
# print(huang_asarray) #['huang' 'chang' 'huai']


#zeros()
huang_zeros = numpy.zeros((3,6))
# print(huang_zeros) #3行6列值为0的数组


#empty()
# huang_empty = numpy.empty((2,3,3))
# huang_empty = numpy.empty((2,3))
# print(huang_empty)


#arange()
huang_arange = numpy.arange(10)
# print(huang_arange) #[0 1 2 3 4 5 6 7 8 9]




#--------------------------------------------------------------------
'''数据类型:
数据类型，即dtype，是一个特殊的对象，它包含了ndarray需要为某一种数据所申明
 的内块信息。

    类型      	      代码              	描述
int8、uint8	        i1，u1	        有符号和无符号的8位整数
int16、uint16	    i2，u2	        有符号和无符号的16位整数
int32、uint32	    i4，u4	        有符号和无符号的32位整数
int64、uint64	    i8，u8	        有符号和无符号的64位整数
float16	            f2	            半精度浮点型
float32	            f4、f	        标准单精度浮点型
float64	            f8、d	        标准双精度浮点型
float128	        f16、g	        拓展精度浮点型
complex64	        c8	            基于32位浮点数的复数
complex128	        c16	            基于63位浮点数的复数
complex256	        c32	            基于128位浮点数的复数
bool	            ?	            布尔值
object	            o	            Python object类型
string_	            S	            ASCII 字符串类型
unicode_	        U	            Unicode类型

'''
#    Numpy包含的数据类型比较丰富，当需要转换数据格式时，可以使用astype()函数。
# 使用astype()总是生成一个新的数组，尽管传入的dtype与之前的一样

import numpy


data = numpy.array([1,2,3,4,5,6,7,8,9], dtype=numpy.int64)
# print('数据类型:',data.dtype) #int64


float_data = data.astype(numpy.float32)
# print('数据类型:',float_data.dtype) #float32


strdata = numpy.array(['11','12','12.3','15','18.9','19.88'])
# print('数据类型:',strdata.dtype) #<U5


num_data = strdata.astype(numpy.float32)
# print('数据类型:',num_data) #[11.   12.   12.3  15.   18.9  19.88]

#-------------------------------------------------------------------

'''数据组访问:

1、一维数组:
  （1）位置索引
  使用位置索引可以实现数组元素的获取，列表中讲解过如何通过正向索引、负向索引、
切片索引和无限索引获取元素。
  （2）神奇索引
  在一维数组中，列表的所有索引方法都可以用在数组上，而且还可以将任意位置的索引
组装为列表，用作对元素的获取，这个也称之为神奇索引。神奇索引与其它的切片不同，
它总是将数据复制到一个新的数组中。


2、二维数组:
  在二维数组中，位置索引必须写成
  [rows, cols]的形式，
  方括号前半部分用于控制行索引，后半部分用于控制列索引；
如果需要获取所有的行或者列的元素，那么，对应的行索引或者列索引用冒号表示；
'''
#(前面定义的例子)

#一维数组元素的获取:
# print(arr1[[1,2,5,8]]) #[2 3 6 9]
 #里面的数字就是index


#二维数组元素的获取
# print(arr3[1,2]) #3


# print(arr3[2,:]) #['a' 'b' 'c' 'd' 'e']


arr3 = numpy.array([[1,2,3,4,5],
                    [5,4,3,2,1],
                    ['a','b','c','d','e'],
                    ['e','d','c','b','a']])

# print(arr3[:,2]) #['3' '3' 'c' 'c']



# print(arr3[1:4,2:8])
'''通俗理解:
 , 左边是行;
 , 右边是列
'''




'''3,如果要取二维数组的某几行,某几列,应该使用 ix_() 函数
 #第一行,第三行,最后一行;第二列,第三列,最后一列
'''

# print(arr3[numpy.ix_([0,2,-1],[1,2,-1])])



'''4、对切片的赋值，整个切片都会被重新赋值。

  区别于python的内置列表，数组的切片是原数组的视图，这意味数据并不是被复制了，
任何对于视图的修改都会反应到原数组上，这样设计非常适合处理非常大的数组。
如果你还是想要一份数组切片的拷贝，而不是一份视图的话，你就必须显式地复制这个
数组。如：
Data[5:8].copy()
'''
import numpy

data = numpy.array([1,2,3,4,5,6,7,8,9])
# print('一维数组:',data)


dataslice = data[5:8]
# print('切片:',dataslice) #切片: [4 5 6 7 8]
dataslice[0:2] = 12
# print('切片赋值后:',data) #[ 1  2  3  4  5 12 12  8  9]


slicecopy = data[5:8].copy()
slicecopy = 13
# print('切片复制赋值后:',data) #[ 1  2  3  4  5 12 12  8  9]




'''数组属性
  每一数组都有一个shape属性,用来表征数组每一维度的数量;
  每个数组都有一个dtype属性,用来描述数组的数据类型;
'''
# print("二维数组的数据结构：",type(arr3)) #<class 'numpy.ndarray'>
# print("二维数组的维数：",arr3.ndim) #2
# print("二维数组的行列数：",arr3.shape) #(4,5)
# print("二维数组的数据类型：",arr3.dtype) #<U11
# print("二维数组的元素的个数：",arr3.size) #20




'''数组形状

   数组形状处理的手段主要有:
reshape()、   resize()、   ravel()、   flatten()、   vstack()、
hstack()、   row_stack()、   colum_stack()。

   reshap和resize都是用来改变数组形状的方法，但是reshape方法只是返回改变
形状后的预览，但是并未改变原来数组的形状，而resize方法会直接改变原数组的形状
'''

arr3 = numpy.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
# print('数组形状: ',arr3.shape)
# print(arr3.reshape(2,9))
# print('数组形状: ',arr3.shape)
# print(arr3.resize(2,9))
# print('数组形状: ',arr3.shape)




'''
   如果需要将二维数组降维为一维数组，利用ravel、flatten和reshape方法可以解决。
通过flatten方法实现的降维是复制，它的结果修改对原数据没有影响；
ravel与reshape返回的则是视图，通过对视图的修改会影响原数组。
'''
arr4 = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
# print('原数组: \n',arr4)
#
# print('数组降维: \n',arr4.ravel())
# print('数组降维: \n',arr4.flatten())
# print('数组降维: \n',arr4.reshape(-1))

print('===============分割线==============')

# print('数组降维: \n', arr4.ravel(order='F')) # [1 4 7 2 5 8 3 6 9]
# print('数组降维: \n',arr4.flatten(order='F')) #[1 4 7 2 5 8 3 6 9]
# print('数组降维: \n',arr4.reshape(-1, order='F')) #[1 4 7 2 5 8 3 6 9]

print('-------------再来一个分割线-------------')

arr4.flatten()[0] = 99
# print('flatten方法：\n',arr4)

arr4.ravel()[1] = 88
# print('ravel方法：\n',arr4)

arr4.reshape(-1)[2] = 77
# print('reshape方法：\n',arr4)





'''
   vstack()用于垂直方向的数组堆叠，其功能与row_stack()函数一致，
而hstack()用于水平方向的数组合并，其功能与column_stack()一致.
  如果是多个数组的垂直堆叠，必须保证每个数组的列数相同，
  如果将多个数水平堆叠，则必须保证所有数组的行数相同。
'''
arr5 = numpy.array([11,22,33])
print("垂直合并数组，vstack：\n",numpy.vstack([arr4,arr5]))
print("垂直合并数组，row_stack：\n",numpy.row_stack([arr4,arr5]))

arr6 = numpy.array([[44],[55],[66]])
print("水平合并数组，hstack：\n",numpy.hstack([arr4,arr6]))
print("水平合并数组，column_stack：\n",numpy.column_stack([arr4,arr6]))







'''排序

跟python列表类似，numpy数组可以用数组的sort方法按位置排序；
可以在多维数组中根据传递的axis值，沿着轴向对每个一维数据段进行排序；
顶层的np.sort()方法返回的是的是已经排序好的数组的拷贝，而不是对原来数组按
  0位置排序。
'''















































