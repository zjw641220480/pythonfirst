#!/usr/bin/python3
#coding=utf-8    #必不可少的，不然容易报错
'''
Created on 2017年9月27日
用来掩饰集合的相关操作
set集合是无序的，不能通过索引和切片的方式来进行操作
@author: lengxiaoqi
'''

simple_set = set('name');
print(simple_set);
simple_set.add('age');#集合将age整体作为一个元素放入到集合内部；
print(simple_set);
simple_set.remove('n');#指定删除集合中的某个值；
print(simple_set);

#以下演示集合的运算
setA=set('myfirst');
setB=set('name');

print(setA-setB);#两个集合的差集
print(setA|setB);#两个集合的并集
print(setA&setB);#两个集合的交集
print(setA in setB);#判断集合a是否在集合b中






