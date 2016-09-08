#!/usr/bin/python
# -*- coding:utf -*-

class student(object):
    name = ''
    age  = 0

    def __init__(self,name,age):
        self.name = name
        self.age  = age
        
sinfo = student('xiaoming',4)
print sinfo.name

setattr(sinfo,'python','haha')##和:sinfo.python = 'haha'的效果一样
#__dict__变量
print sinfo.__dict__

delattr(sinfo,'python')##和del sinfo.python效果一样
print sinfo.__dict__
