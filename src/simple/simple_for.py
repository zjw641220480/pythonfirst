'''
Created on 2017年10月3日

@author: lengxiaoqi
'''
from pip._vendor.requests.packages.urllib3.connectionpool import xrange
plays=set(['Hamlet','Macbeth','King Lear']);#将一个列表转变为集合
#各种方式取出集合中的元素
while plays:
    print(plays.pop());
    
for play in plays:
    print(play);

#使用for循环求和
total = 0;
for i in xrange(100):#i列表中每一项的值
    total = total+i;
print(total);    

values=[7,8,9,10,11,12,13];
for i in values:
    if i%2 == 0:
        continue;
    else:
        print(i);

for ch in 'names':
    print(ch);

#在for循环中使用enumerate函数来达到根据下标来循环的目的；
for i,value in enumerate(['a','b','c']):
    print(i,'\t',value);



