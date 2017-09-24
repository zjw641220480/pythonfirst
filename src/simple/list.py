#!/usr/bin/python3
#coding=utf-8    #必不可少的，不然容易报错
'''
Created on 2017年9月24日
演示列表相关
列表有种stringBuffer的意味
@author: lengxiaoqi
'''

li=["a","b","c",1,2,3,1];
li[0]=0;#根据下标索引，修改列表中的值
print(li);
#列表中删除元素的三种最常用的方法；del，remove，pop
del li[1];#根据下标来删除列表中的某个位置的元素
print(li);
li.remove(1);#根据给定的值，删除列表中的某个值,只删除第一个出现的,这个函数只有这一个参数
print(li)
li.pop(1);#弹出某个下标的值，当超出下标索引的时候，报错IndexError: pop index out of range
print(li)
#以下演示列表的分片赋值
names=list('Perl');
names[1:]=list('python');#将下标1之后的（包含下标1）替换为右边的新的列表
print(names); 
names[1:1]=list('python');#在下标1后面添加上右边新的列表从而形成新的列表
print(names)
#上面的其实就是将列表中指定范围的元素替换为指定列表；
names.append('a');#在列表后面追加上新的元素，（可以使一个列表，可以是一个元素）,追加后列表新增一个元素
print(names)
print(names.count('p'));#计算列表中元素出现的次数
names.extend(list("TOM"));#在列表的后面追加新的列表（只能是列表），两个列表相加
print(names)
print(names.index('w'));#当元素不存在的时候报错，ValueError: 'w' is not in list





