#-*- coding:utf-8 -*-
#基础部分  ASCII码  其他语言自己编码 统一标准 Unicode一般两个字节 节约空间可变长编码utf-8 1-6个字节

#ASCII 字符和数字的转换 ord() chr()

print ord('A')
print chr(69)

#Unicode u'...'
print u'中'
#encode 表示Unicode转化为其他编码
u'中'.encode('utf-8')
#decode 表示其他编码转换为Unicode编码

#格式化  输出内容根据变量进行变化输出 用%表示 字符串内部用%号表示被替换部分
#%d %s %f %x
x = '0x%x' % 23
print x
print '0x%x' % 13