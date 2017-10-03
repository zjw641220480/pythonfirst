#!/usr/bin/python3
#coding=utf-8    #必不可少的，不然容易报错
"""
Created on 2017年9月21日
python有五种数据类型，int，boolean，字符串--用''或""表示，列表--list--用[]表示，元祖--tuple--用()表示，字典--dict--用{}表示
python的可变数据类型，列表[]，字典{}
python的不可变数据类型，整型int，字符串str，元组()
python还有一种数据类型，名称为集合(set)，专门用来对数学中的集合进行相关运算,集合的标志直接是一个大括号
注意：集合是无序的；每一次的输出都是不一致的，无序在代码上的更直观表现是：不能通过索引和切片来做一些操作
@author: lengxiaoqi
"""

print ("hello python")
a="hello";
d=9.8;
i=565;

print(abs(d));#获取绝对值
print(bin(i));#转换为二进制
print(oct(i));#转换为八进制
print(hex(i));#转换为十六进制
print(bytes(a,encoding="utf-8"));#转换为byte
print(dict(one=1,two=2));#创建数据字典
print(dir());#不带参数的时候，返回当前范围内的变量，方法，和定义的类型列表，
#带参数的时候返回参数的属性，方法列表；
print(eval("1+2+4"));#将字符串作为有效的表达式求值并返回计算结果
print("i am {0} i like {1}".format("zhangsan","tonm" ));#格式化输出，这里只是使用到类似占位符的功效
print(frozenset('myset'));#创建一个不可修改的集合
print(id(a));#返回对象a的内存地址
print(hash(a));#返回a的hash值
print(int("45"));#字符串转数字
class Foo(object):#这个类集成Object类
    pass;
class Bar(Foo):#这个类集成Foo类
    pass;
print(isinstance(Foo(), Foo));#检查对象是否是指定类的对象，返回True或False
print(issubclass(Bar,Foo));#检查一个类是另一个类的子类；
print(len(a));#返回对象的长度，对象需要时序列类型（字符串，元组，列表）和映射类型（字典）
print(list("name"));#创建一个列表
print(locals());#打印当前可用的局部变量的字典；

print(dir(a));#查看拥有的相关变量和函数
print(type(a));#查看变量的类型


