'''
Created on 2017年10月3日

@author: lengxiaoqi
'''

x=0
if x>0:
    print("x is positive");
elif x<0:
    print("x is negative");
else:
    print("x is zero");
#在if判断中也可以使用各种表达式来作为判断条件；他们会被当做ture来处理
#None，0，空字符串，空列表，空集合会被当做false来处理；
#当然这种方式是不推荐的，推荐使用len(mylist)>0来判断一个列表是否为空
mylist=[1,2,3,4,5];
if mylist:
    print("The first element is ",mylist[0]);
else:
    print("there is no first element");