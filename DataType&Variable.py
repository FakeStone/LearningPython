#-*- coding:utf-8 -*-
#基础部分 数据类型和变量


#整数{十进制 二进制 十六进制(0x)}

#浮点数 科学计数法

#字符串表示 {'' "" 转义字符 r''表示不转义 '''...'''表示多行内容}
#\n \t \\
print 'I\'m OK.'
print 'I\'m learning \n python.'

print r'\\\t\\\\'

print '''革命不是请客
吃饭

'''
print '----'

#boolean 布尔变量 {True False} 可以用 and or not 进行计算 布尔变量主要用在条件计算中
print True and False

#空值 None
if not None:
    print None


#动态语言的变量不用生命 类型不固定

#常量  Python无常量  用大写表示