'''
Created on 2017年10月3日

@author: lengxiaoqi
'''
def add(x,y):
    return x+y;
try:
    print(add(1, 'ad'));
except TypeError as exc:
    print(exc);
finally:
    print("finally 模块");