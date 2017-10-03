#!/usr/bin/python3
#coding=utf-8    #必不可少的，不然容易报错
'''
Created on 2017年9月27日
用来演示python函数的相关操作
@author: lengxiaoqi
'''
#自己的第一个参数罢了
from keyword import kwlist
def myFirstFunction():
    print("这个是我的第一个参数");
    
#有参数的python方法
def myFunctionParameter(parameter):
    print("传递过来的参数为："+parameter);
    return parameter+"\tfanhuizhi"

#计算绝对值的方法，一个实例方法
def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError("bad operand type");
    if x>=0:
        return x;
    else:
        return -x;
'''    
在Python中定义函数，可以用必选参数，默认参数，可变参数，关键字参数和命名关键字参数这5种
参数都可以组合使用，但是，参数定义的顺序必须是：必选参数，默认参数，可变参数，命名关键字参数和关键字参数
第一个参数为位置参数，第二个参数为默认参数，两个参数都没有进行类型校验；
*args是可变参数，args接受的是一个tuple；
**kw是关键字参数，kw接受的是一个dict；
定义命名关键字参数的时候，在没有可变参数的情况下，分隔符（*）不能省略，不然定义的就是位置变量了；
'''
def power(x,n=2):
    s=1;
    while n>0:
        n=n-1;
        s=s*x;
    return s;
'''
初始的将参数处理成列表或者集合
'''
def calc(numbers):
    sum=0;
    for n in numbers:
        sum= sum+n*n;
    return sum;
'''
将参数处理成可变参数（实质上就是一个列表）
'''
def calc_pa(*numbers):
    sum=0;
    for n in numbers:
        sum = sum + n*n;
    return sum;
'''
关键字参数演示
'''
def person(name,age,**kw):
    if 'city' in kw:
        #有city参数
        pass;
    if 'job' in kw:
        #有job参数
        pass;
    print('name:',name,'age:',age,'other:',kw);
'''
命名关键字参数的演示
'''
def person_key(name,age,*,city,job):
    print('name:',name,'age:',age,'city:',city,'job:',job);
    

#print(myFirstFunction());#因为第一个函数无返回值，故第二行会打印None，
#print(myFunctionParameter('parameter'));