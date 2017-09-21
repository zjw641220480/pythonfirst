#coding=utf-8    #必不可少的，不然容易报错
"""
Created on 2017年9月21日
用来演示python中的字符串相关函数
@author: lengxiaoqi
"""

#去空格及特殊符号
str='python String function';
print len(str);#获取字符串的长度
print str.upper();#字符串转大写
print str.lower();#字符串转小写
print str.swapcase();#字符串大小写互换
print str.capitalize();#首字母大写，其余均小写
print '%s lower=%s' % (str,str.lower())
print str.find("t");#搜索第一次出现的下标
print str.find("t",3);#从指定下标开始搜索，并且报错此下标
print str.find("t",3,10);#从指定下标开始，截止到指定下标