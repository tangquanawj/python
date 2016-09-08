#!/usr/bin/python
# -*- coding:utf-8 -*-

#定义一个类
class people:
    name = ''
    age  = 0
    __weight = 0
    
    #构造函数
    def __init__(self,n,a,w):
        self.name = n
        self.age  = a
        self.__weight = w
    #方法
    def speak(self):
        print ("%s is speaking: I am %d years old"%(self.name,self.age))

#定义一个子类继承父类
class student(people):
    grade = 0
    
    #构造函数
    def __init__(self,n,a,w,g):
        #调用父类的构造函数
        people.__init__(self,n,a,w)
        self.grade = g
    
    def speak(self):
        print ("%s is speaking: I am %d years old,and I am grade in %d." %(self.name,self.age,self.grade))

p=student('Tom',10,10,3)
p.speak()
