#!/usr/bin/python
# -*- coding:utf-8 -*-
#类的多重继承
#class 类名(父类1,父类2,...,父类n)
# <语句>
# 需要注意括号内父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索
#即方法在子类中未找到时，从左到右查找父类中是否包含方法

#先定义三个类
class people:
    name = ''
    age  = 0
    __weight = 0

    def __init__(self,n,a,w):
        self.name = n
        self.age  = a
        self.__weight = w
    
    def speak(self):
        print ("%s is speaking: I am %d years old" %(self.name,self.age))

class student(people):
    grade = 0

    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade = g

    def speak(self):
        print ("%s is speaking: I am %d years old,and I am grade in %d" %(self.name,self,age,self.grade)) 

class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    
    def speak(self):
        print ("I am %s,I am a speaker!My topic is %s" %(self.name,self.topic))

#多重继承
class sample(speaker,student):
    a = ''
    def __init__(self,n,a,w,g,t):
        speaker.__init__(self,n,t)
        student.__init__(self,n,a,w,g)

test = sample('Tim',25,80,4,'Python')
#默认是排名靠前的父类
test.speak()
