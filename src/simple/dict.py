#!/usr/bin/python3
#coding=utf-8    #必不可少的，不然容易报错
'''
Created on 2017年9月24日
用于演示python中字典的相关函数；
    字典是用大括号来包含数据的，大括号里面包含键和其对应的值，键和值之间用冒号隔开，一对键和值
成为一项；每一项之间用逗号隔开，
注意点：
    1:字典的键必须是不可变数据类型（int，string，tuple）；如果用元组做键，
必须保证元组中的对象也是不可变的对象；可变数据类型对象不能作为字典的键；不然报错TypeError: unhashable type: 'list'
    2:字典是无序的，不能用下标来取值；
@author: lengxiaoqi
'''
dangan={"xingming":"zhangsan",'age':11,'sex':'nan'};
print(dangan['xingming']);#使用字典中某个键来取得字典中的值；
dangan['address']='henan';#在字典后面追加一项；
print(dangan);
dangan['xingming']='lisi';#直接修改字典中某一项的值
print(dangan);
del dangan['age'];#删除字典中的某一项
print(dangan);
dangan.pop('sex');#使用字典自带的函数删除字典中的某一项
print(dangan.get('xingmin', '默认值'));#使用字典自带的函数获取字典中的某一项的值













