#!/usr/bin/python
# -*- coding:utf-8 -*-
#使用try。。。finally来实现

try:
    f = open('/home/tang/demo.py','r')
    print f.read()
finally:
    if f:
        f.close()

#read()会一次性的读取文件的所有内容，如果文件有10G,内存就爆炸了，所以，为了保险器件，可以反复调用read(size)的方法，
#每次最多读size个字节的内容。
#另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
#如果是小文件，直接用read()
#如果不能确定文件大小，反复调用read(size)比较保险;如果是配置文件，调用readlines()最方便。

with open('/home/tang/demo.py','r') as f:
    print r.read()


