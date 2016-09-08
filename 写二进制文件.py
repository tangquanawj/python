#!/usr/bin/python
# -*- coding:utf-8 -*-
#f = open('text.txt','w')
#f.write('Hello World!')
#f.close()

#可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件，当我们写文件时，操作系统往往不会立刻把数据写入磁盘，
#而是放在内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
#忘记调用close()方法的结果就是一部分写入了磁盘，一部分丢失了，所有还是用with语句来的保险：

with open('demo.md','w') as f:
    f.write("Demo TEST")
