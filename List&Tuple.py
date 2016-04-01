#-*- coding:utf-8 -*-
#内部数据类型学习


#List 是一种有序[集合] 增加和删除元素
classmates = ['Lee1', 'Wang2', 'Zhang3']
print classmates
#len()
print len(classmates)
#索引访问元素 超出范围IndexError
print classmates[-1]
#list是一个可变的有序列表可以往list中追加元素，添加到末尾
classmates.append('Sun4')
print classmates
#在指定位置插入
classmates.insert(0,'Qian5')
print classmates
#删除使用pop方法
print classmates.pop()

#list 内部的元素类型可以不同 list内部元素还可以是list 即多维数组

#初始化就不能修改的有序列表 tuple tuple 不可变所以安全
#定义为空的tuple
t = ()
#定义只含有一个元素的tuple 结尾用逗号避免与(1) 运算符优先级混淆
t = (1,)
#tuple 内有一个[]list 元素即可实现可变
t = (1, 2, 3, [4, 5])
t[3][0] = 6
print t
#tuple 用于存储常量