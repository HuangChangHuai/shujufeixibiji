# -*- coding=utf-8 -*-
# Author  : 大白的浅
# Time    : 2019/1/14 15:06
# 描述    : 210773579@qq.com
print('start')
'''1,数值交换
    要求：（1）给两个变量分别赋不同的整数值，然后利用程序交换两个变量的值。
代码：
'''
# a = int(input('输入变量1的值:'))
# b = int(input('输入变量2的值:'))
# print(a,b)
# #交换两个变量的值
# c = a
# a = b
# b = c
# print('交换后变量1的值是：',a)
# print('交换后变量2的值是：',b)






'''2  三个数比较大小
    题目：输入三个整数x，y，z，请把这三个数由小到大输出。
'''
# a = int(input('给变量a赋值:'))
# b = int(input('给变量b赋值:'))
# c = int(input('给变量c赋值:'))
# print('你输入的三个数分别是:',a,b,c)
#
# if a > b:
#     d = a
#     a = b
#     b = d
# if a > c:
#     d = a
#     a = c
#     c = d
# if b > c:
#     d = b
#     b = c
#     c = d
# print('从小到大:',a,b,c)







'''3 计算人体健康BMI

    输入height(米)和weight,计算BMI,
指数小于18.5,偏瘦;指数在18.5与24.9之间,正常;42.9到299.9,偏重;29.9以上,肥胖
BMI = 体重/(身高*身高)
'''
# height = float(input('你的身高cm:'))
# weight = float(input('你的体重kg:'))
# height = height/100
# res_bmi = weight/(height*height)
# print('你的BMI指数是:',res_bmi)
# if res_bmi<18.5:
#     print('偏瘦')
# elif res_bmi < 24.5:
#     print('正常')
# elif res_bmi < 29.9:
#     print('偏重')
# else:
#     print('肥胖')









'''4 计算闰年

    闰年:
        普通闰年:能被4整除但不能被100整除的年份为普通闰年。
                 (如2004年就是闰年，1999年不是闰年);
        世纪闰年:能被400整除的为世纪闰年。(如2000年是闰年，1900年不是闰年);
    思路:如果年份是100的整数倍:能被400整除就是闰年;
            否则能被4整除的就是闰年
'''
# year = int(input('输入要判断的年份:'))
# if year%4 ==0:
#     if year%100 ==0:
#         if year%400 ==0:
#             print(year, "是闰年") # # 整百年能被400整除的是闰年
#         else:
#             print(year,"不是闰年")
#     else:
#         print(year,"是闰年")    # 非整百年能被4整除的为闰年
# else:
#     print(year, "不是闰年")








'''5 回文
    输入一个字符串，判断其是否为回文。
    回文字符串是指从左到右读和从右到左读完全相同的字符串。
     eg:abcdeedcba;abcdedcba;
'''
# mystr = input('英文字符串:')
# length = len(mystr)
# i = 0
# flag = True
# while i<= length/2:
#     if mystr[i] == mystr[(length-1)-i]:
#         i+=1
#     else:
#         flag = False
#         break
# if flag:
#     print('回文')
# else:
#     print('不是回文')







'''6 打印99乘法表
'''
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'*',i,'=',i*j, end='\t')
#     print() #让它换行成三角形






'''7 自然数求和
    求前N个自然数的和
'''
# num = int(input('你要计算前多少个自然数的和：'))
# i = 0
# sum = 0
# while i <= num:
#     sum+=i
#     i+=1
# print('前',num,'个自然数的和是',sum)









'''8 计算阶乘的和
    计算1! + 2! + 3! + …… + N!
'''
# #方法一:
# import math
# num = int(input('输入一个数字:'))
# i= 1
# sum = 0
# while i < num+1:
#     sum += math.factorial(i)
#     i += 1
# print('前',num,'个数的阶乘的和是',sum)
#


#方法二:
# myvalue = int(input("请输入你要计算前几个数的阶乘之和："))
# sum = 0
# fac = 1
# for i in range(1 , myvalue + 1):
#     fac = 1
#     for j in range(1 , i + 1):
#         fac = fac * j
#     sum += fac
# print("前",myvalue,"个自然数的阶乘之和是：",sum)






''' 9 鸡兔同笼
    题目：今有鸡兔同笼，上有35头，下有94足，鸡兔分别有几只？
'''
# chicken = 0
# rabbit = 35 - chicken
# while chicken <= 35:
#     if 2*chicken +4*rabbit == 94:
#         print('鸡',chicken)
#         print('兔子',rabbit)
#     chicken += 1
#     rabbit = 35-chicken






''' 10 百人分百饼
    有一百个人，分一百个饼，其中，大人每人分3个，小孩子3个人分1个，
请问有多少个小孩，多少个大人。
'''
# child = 0
# adult = 100 -child
# while child <=100:
#     if 3*adult + child/3 == 100:
#         print('小孩:',child)
#         print('大人:',adult)
#     child += 1
#     adult = 100 -child








''' 11 最大值最小值
    利用循环比较的方法，打出一个列表中的最大值和最小值，不要用max函数和min函。
'''
# import random
# mylist = [random.randint(1,100) for i in range(10)]
# # print(mylist)
#
# maxnum = mylist[0]
# minnum = mylist[0]
#
# for i in mylist:
#     if i < minnum:
#         minnum = i
#     if i > maxnum:
#         maxnum = i
# print('最大值:',maxnum)
# print('最小值:',minnum)
# print('max()内置函数计算的结果:',max(mylist))
# print('min()内置函数计算的结果:',min(mylist))







'''换零钱
    把1元钱换成1分、2分和5分的硬币，请问有多少种换法？
'''
# coin1,coin2,coin5 = 0, 0, 0
# max1,max2,max5 = 100, int(100/2), int(100/5)
#
# count = 0  #总方案数
#
# while coin1 <= max1:
#     coin2 = 0
#     while coin2 <= max2:
#         coin5 = 0
#         while coin5 <= max5:
#             if coin1+2*coin2 + 5*coin5 == 100:
#                 count += 1
#                 print('第%s方案:\t一分%s个\t二分%s个\t五分%s个'%(count,coin1,coin2,coin5))
#             coin5 +=1
#         coin2+=1
#     coin1 += 1
# print('总方案数:',count)


#方式二:
# count = 0
# max1,max2,max5 = 100, int(100/2), int(100/5)
# for coin1 in range(max1+1):
#     for coin2 in range(max2+1):
#         for coin5 in range(max5+1):
#             if coin1 + 2 * coin2 + 5 * coin5 == 100:
#                 count += 1
#                 print('方案', count, ':\t 1分', coin1, '个\t2分', coin2, '个\t5分：', coin5, '个')
#







'''13 登录功能
    题目：模拟实现一个系统登录功能，最多允许输错4次；
'''
# username = "admin"
# password = "abc888"
# flag = False
# trytimes = 0
#
# while not flag:
#     myname = input("请输入你的用户名：")
#     mypassword = input("请输入你的密码：")
#     trytimes += 1
#     if myname == username and mypassword == password:
#         flag = True
#         print('您登录成功，欢迎你进入系统')
#     else:
#         print('用户名错误或者密码错误')
#         print('你还有{:d}次尝试机会'.format(4 - trytimes))
#         if trytimes >= 4:
#             print('你已经输错4次，为了账户安全，账号被锁定')
#             break




# 12.14.	修改密码功能
# 题目：模拟用户修改密码的功能。

# username = "admin"
# password = "abc888"
# flag = False
# trytimes = 0
#
# while not flag:
#     oldpassword  = input("请输入你的旧密码：")
#     trytimes += 1
#     if oldpassword == password:
#         while not flag:
#             newpassword1 = input("请输入你的新密码:")
#             newpassword2 = input("请再次输入你的新密码:")
#             if newpassword1 == newpassword2:
# 	       password = newpassword1
#                 print('你的密码修改成功')
#                 flag = True
#             else:
#                 print('你两次输入的密码不一致，请重新输入')
#     else:
#         print('你输入的旧密码错误，你还有{:d}次尝试机会'.format(4 - trytimes))
#         if trytimes >= 4:
#             print('你已经输错4次，为了账户安全，账号被锁定')
#             break





'''15.	质因数分解
    题目：输出一个大的整数，然后对这个数进行因数分解
'''
# number = int(input('请输入一个要进行质因数分析的数字：'))
# mylist = []
# test = 2
# while test <= number:
#     if number % test ==0:
#         mylist.append(test)
#         number /=test
#         continue
#     if number ==1:
#         break
#     test += 1
# print(mylist)







''' 16 冒泡排序

    冒泡排序的思想,每次比较两个相邻的元素,如果他们的顺序错误就把他们交换位置.
    冒泡排序的原理:
        每一趟只能将一个数归位,如果有n个数进行排序,需将n-1个数归位, 也就是说
        要进行n-1趟操作(已经归位的数不用再比较)
    缺点: 冒泡排序解决了桶排序浪费空间的问题, 但是冒泡排序的效率特别低
            比如有五个数: 12, 35, 99, 18, 76, 从大到小排序, 对相邻的两位进行比较。
                第一趟:
                第一次比较: 35, 12, 99, 18, 76
                第二次比较: 35, 99, 12, 18, 76
                第三次比较: 35, 99, 18, 12, 76
                第四次比较: 35, 99, 18, 76, 12
                经过第一趟比较后, 五个数中最小的数已经在最后面了, 
                接下来只比较前四个数, 依次类推
                第二趟
                99, 35, 76, 18, 12
                第三趟
                99, 76, 35, 18, 12
                第四趟
                99, 76, 35, 18, 12
                比较完成
'''
# import random
# mylist = [random.randint(1,100) for i in range(10)]
# print(mylist)
#
# #冒泡排序
# for i in range(len(mylist)-1):  #这个循环负责设置冒泡排序进行的次数
#     for j in range(len(mylist) - i - 1): #j为列表下标
#         if mylist[j] > mylist[j+1]:
#             mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
#     print('第',i+1,"趟排序后的数值列表：", mylist) ##输出每一趟排序的结果
# print("冒泡排序后的数值列表：", mylist)








'''17 约瑟夫问题
    约瑟夫问题是一个有趣的数学游戏,游戏规则是:
    N个人围成一个圈，编号从1开始，依次到N。编号为M的游戏参与者开始报数，报数从1
开始，后面的人报数接龙，直到K为止，报数为K的人将出局。出局者的下一个玩家接着从1
开始报数，如此循环，直到剩下一个玩家时游戏结束，这个玩家就是游戏获胜者。哪个编
号是游戏获胜者呢？
'''
# def josephusl(n, k):
#     link = list(range(1,n+1))
#     print(link)
#     killnum = 0
#     while len(link) > 1:
#         killnum += k-1
#         if killnum >= len(link):
#             killnum %= len(link)
#
#         print('本轮kill:',link[killnum])
#         del link[killnum]
#     print('最终幸存者是',link[0])
# josephusl(200,6)






'''18 递归求自然数和
'''
# def mysum(n):
#     if n == 1:
#         return 1
#     else:
#         return n+mysum(n-1)
# print(mysum(100))
#






'''斐波那契数列
    除了前两个数外,每个数的值和等于前两个数的总和;
    0,0,sn = sn-1 + sn-2
'''

# def fei(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fei(n-1)+fei(n-2)
# print(fei(8))







'''猜幸运数字
    系统随机生成一个1-1000之间的数字，然后用户开始猜，程序提示大了或者是小了，
给10次猜数字的机会。
'''
# import random
# result_num = random.randint(1,999)
# times = 10
# success = False
#
# print('你有诗词机会猜幸运数字')
# while times:
#     guess = int(input('你猜:'))
#     if guess == result_num:
#         print('中了!',result_num)
#         success = True
#         break
#     else:
#         times -= 1
# if success:
#     pass
# else:
#     print('很遗憾你没有猜中!')







'''赌大小游戏
'''
# import random
# name = input('your name:')
# money = int(input('your money:'))
# print('player info: %s $%d'%(name, money))
#
# while money:
#     stake = int(input('请输入下注金额:'))
#     if stake > money:
#         print('你钱不够了')
#         continue
#     print('1为大,0为小:')
#     num = int(input('大还是小:'))
#     if num == 0:
#         print('买定离手,你押小')
#     elif num == 1:
#         print('买定离手,你押大')
#     else:
#         print('你还是买一坨屎当零食吃吧!')
#
#     randomNum = random.randint(0,1)
#     print('****************')
#     if randomNum == 0:
#         print('*** 此局开小 ***')
#     else:
#         print('*** 此局开大 ***')
#     print('****************')
#     print()
#     if num == randomNum:
#         money += stake
#         print(name, '你赢了，你现在的余额为:', money)
#     else:
#         money -= stake
#         print(name, '你输了，你现在的余额为:', money)
#     print('*************************************')
#     print()
#     if money > 0:
#         print(name, '，赌局继续')
#     elif money > 10000:
#         print(name, '，你今天运气真好，不跟你玩了')
#         break
#
# print(name, ',运气真背，你输光了，明天再来吧')








'''22,五猴分桃
    5只猴子一起摘了1堆桃子，因为太累了，它们商量决定，先睡一觉再分。过了不知多久，
来了1只猴子，它见别的猴子没来，便将这1堆桃子平均分成5份，结果多了1个，
就将多的这个吃了，拿走其中的1堆。
又过了不知多久，第2只猴子来了，他不知道有1个同伴已经来过，还以为自己是第1个到的呢，
于是将地上的桃子堆起来，平均分成5份，发现也多了1个，同样吃了这1个，拿走其中的1堆。
第3只、第4只、第5只猴子都是这样。问这5只猴子至少摘了多少个桃子?
'''
# def taozi(n):
#     """
#     判断桃子数是不是符合题义
#     :param n:
#     :return:
#     """
#     for i in range(1,6):
#         n = n-1   #猴子吃掉了一个
#         if n%5 ==0:
#             n = n-n/5
#             continue
#         else:
#             return False    # 如果不能分成五份，则返回False
#     return True
#
# isright = False
# trynum = 1
# while not isright:
#     if taozi(trynum):
#         isright = True
#         break
#     trynum += 1
# print('最小的taozi数为:',trynum)
# for i in range(1, 6):
#     trynum = trynum - 1
#     trynum = trynum - trynum / 5
#     print("第{:d}猴子吃1个，拿走：{:.0f}个，还剩{:.0f}".format(i,int(trynum/4), trynum))
#
#







'''五人分鱼
问题描述:
    A、B、C、D、E这5个人合伙夜间捕鱼,凌晨时都已经疲惫不堪,于是各自在河边的树从
中找地方睡着了。
第二天日上三竿时,
    A第一个醒来,他将鱼平分为5份,把多余的条扔回河中,然后拿着自己的一份回家去了;
    B第二个醒来,但不知道A已经拿走了份鱼,于是他将剩下的鱼平分为5份,扔掉多余的一条,
然后只拿走了自己的一份;
    接着C、D、E依次醒来,也都按同样的办法分鱼。问这5人至少合伙捕到多少条鱼?
每个人醒来后所看到的鱼是多少条


问题分析:
    假设5个人合伙捕了x条鱼,则A第一个醒来,他将鱼平分为5份,把多余的一条扔回河中,
然后拿着自己的一份回家去了”之后,还剩下4(×-1)/5条鱼。
这里实际包含了一个隐含条件:
    假设Xn为第n(n=1、2、3、4、5)个人分鱼前鱼的总数,则(Xn-1)/5必须为正整数,
否则不合题意。
(Xn-1)/5为正整数即(X~)mod5=0必须成立.
又根据题意,有下面等式:
    X4 = 4(X5-1)/5
    X3 = 4(X4-1)/5
    X2 = 4(X3-1)/5
    X1 = 4(X2-1)/5

    则一旦给定X5,就可以依次推算出X4,X3,X2和x1的值。要保证X5、X4、X3、X2X1
都满足条件(Xn-1)mod5=0,
    此时的X5则为5个人合伙捕到的鱼的总条数。显然,5个人合伙可能捕到的鱼的条数并不唯,
但题目中强调了“至少”合伙捕到的鱼,此时题目的答案唯一。该问题可使用递归的方法求解。
'''
































































