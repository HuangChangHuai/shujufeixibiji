 # -*- coding=utf-8 -*-
# Author  : 大白的浅
# Time    : 2019/1/8 12:20
# 描述    : 210773579@qq.com

''' 数学函数

numpy.pi	                常数π
numpy.e	                    常数e
numpy.fabs(arr)	            计算各元素的浮点型绝对值
numpy.ceil(arr)	            各元素向上取整
numpy.floor(arr)	        各元素向下取整
numpy.round(arr)	        各元素四舍五入
numpy.fmod(arr1,arr2)	    计算arr1/arr2的余数
numpy.modf(arr)	            返回数组元素的整数部分和小数部分
numpy.sqrt(arr)	            计算种元素的算术平方根
numpy.square(arr)	        计算各元素的平方值
numpy.exp(arr)	            计算以e为底的指数
numpy.power(arr)	        计算各元素的指数
numpy.log2(arr)	            计算以2为底的各元素的对数
numpy.log10(arr)	        计算以10为底的各元素的对数

'''


'''统计函数

numpy.min(arr,axis)	        按着轴的方向计算最小值
numpy.max(arr,axis)	        按着轴的方向计算最大值
numpy.mean(arr,axis)	    按着轴的方向计算均值
numpy.median(arr,axis)	    按着轴的方向计算中位数
numpy.sum(arr,axis)	        按着轴的方向计算和
numpy.std(arr,axis)	        按着轴的方向计算标准差
numpy.var(arr,axis)	        按着轴的方向计算方差
numpy.cumsum(arr,axis)	    按着轴的方向计算累计和
numpy.cumprod(arr,axis)	    按着轴的方向计算累计乘积
numpy.argmin(arr,axis)	    按着轴的方向返回最小值所在的位置
numpy.argmax(arr,axis)	    按着轴的方向返回最大值所在的位置
numpy.cov(arr)	            计算协方差矩阵
'''


'''
   这些统计函数中的axis参数，表示在统计数组元素时需要按照不同的轴方向计算，
如果axis=1，则表示按水平方向计算统计值，即计算每一行的统计值；
如果axis=0，则表示按垂直方向计算统计值，即计算每一列的统计值。
'''
import numpy

data = numpy.array([[1,2,3], [4,5,6], [7,8,9]])
# print(data)

# print('垂直计算: \n', numpy.sum(data, axis=1))
# print('水平计算: \n', numpy.sum(data, axis=0))





'''线性代数

'''





'''随机模块

   Numpy.random模块填补了Python内建的random模块的不足，
可以高效地生成多种概率分布下的完整样本值数组。
   产生的随机数都是伪随机数，因为它们是由具有确定的算法根据随机数生成器中
的随机数种子生成的。
Numpy.random中的数据生成函数公用了一个全局的随机数种子，为了避免全局状态，你可以使用numpy.random.RandomState()生成一个随机数生成器，使数据独立于其它的随机数。


#其他的方法:

seed	        向随机数生成器传递随机状态种子
permutation	    返回一个序列的随机排列
shuffle	        随机排列一个序列
rand	        从均匀分布中抽取样本
randint	        根据给定的由低到高的范围生成抽取随机整数
randn	        从均值0方差1的正态分布中抽取样本
binomal	        从二项分布中抽取样本
beta	        从beta分布中抽取样本
normal	        从正态分布中抽取样本
uniform	        从均匀(0,1)分布中抽取样样本
'''











'''数据处理:

Pandas

'''








































































