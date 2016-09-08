#!/usr/bin/python
# -*- coding:utf-8 -*-

#在python语言中，__str__一般格式是这样的是这样的。
#class A:
#    def __str__(self):
#        return 'this is in str'
#
#demo:

class strtest:
    def __init__(self):
        print "init：this is only test"
    def __str__(self):
        return "str: this is only test"

if __name__=="__main__":
    st = strtest()
    print st

#从上面的例子可以看出，当打印strtest的一个实例时，__str__函数被调用
