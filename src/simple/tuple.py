#!/usr/bin/python3
#coding=utf-8    #必不可少的，不然容易报错
'''
Created on 2017年9月24日
演示元组的相关函数
元组的创建很简单，元组是用小括号括起来的，里面用逗号隔开的一串数组；
元组也是一种有序的集合，
注意点：
    1：元组中的值是不允许修改的，需要将整个元组或元组切片形成列表然后对列表进行操作，元组不能在原地进行修改替换等操作；
    2：判断元组是通过小括号和逗号一起的，只有小括号的时候，其会被作为运算符存在
@author: lengxiaoqi
'''
tup_int=(1,2,3,4,5,6);
tup_one=(1,);
tup_str=("a","b","c",1);
tuple([1,2,3]);#通过tuple函数来创建一个元组；
print(tuple("hello"));#通过tuple函数创建的字符元组
print(tup_int[0]);#通过下标的方式来取出元组中的值
print(tup_int[1:5]);#通过指定切片的起始下标和终止下标来获取元组中的值,左闭右开；
#以下演示元组的内置函数
print(len(tup_int));#输出元组中的元素个数
print(max(tup_int));#根据ASCII值返回最大值（元组中的所有值均为int类型,字符型也是不行的）












