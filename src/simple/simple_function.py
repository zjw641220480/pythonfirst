#!/usr/bin/python3
#coding=utf-8    #必不可少的，不然容易报错
'''
Created on 2017年9月27日
用来演示python函数的相关操作
@author: lengxiaoqi
'''
#自己的第一个参数罢了
def myFirstFunction():
    print("这个是我的第一个参数");
    
#有参数的python方法
def myFunctionParameter(parameter):
    print("传递过来的参数为："+parameter);
    return parameter+"\tfanhuizhi"

print(myFirstFunction());#因为第一个函数无返回值，故第二行会打印None，
print(myFunctionParameter('parameter'));