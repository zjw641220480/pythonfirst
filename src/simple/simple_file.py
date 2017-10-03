'''
Created on 2017年10月3日

@author: lengxiaoqi
'''

fi = open("test.txt");
#fi = file("test.txt");
text = fi.read();#读取文本中所有内容
print(text);
fi.close();
fi = open('test.txt');#需要重新打开文件，这里使用另一种方式
lines=fi.readlines();#结果以每一行作为一个列表的形式返回；
print(lines);
fi.close();
fi = open("test.txt");#循环读取出来每一行的内容
for line in fi:
    print(line.strip());#去除左右两边的空格后输出

#二进制文件的读写
import os
f = open('binary.bin', 'wb')
f.write(os.urandom(16));
f.close();

f = open('binary.bin', 'rb')
print(repr(f.read()));
f.close()
