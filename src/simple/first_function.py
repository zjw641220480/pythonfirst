'''
Created on 2017年10月3日

@author: lengxiaoqi
'''

from src.simple.simple_function import myFirstFunction, my_abs,\
    myFunctionParameter, power, calc, calc_pa, person, person_key

print(my_abs(-8));
print(myFirstFunction());
print(myFunctionParameter("key"));
print(power(2));
print(power(2,3));
print(calc([1,2,3]));#初始状态，将列表作为位置参数，
print(calc_pa(1,2,3));#参数为可变参数
print(calc_pa(*[1,2,3]));#另外一种传入可变参数的方式
person('zhangsan',11,city='beijing',job="Engineer");#关键字参数的传值方式，在调用这个方法的时候可以只传入必选参数
person('zhangsan',11,**{'city':'beijing','job':"Engineer"});#这也是一种传入关键字参数的方式
person_key('zhangsan',11,**{'city':'beijing','job':"Engineer"});#命名关键字参数的使用









