#!/usr/bin/python
#-*- coding:utf-8  -*-
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

p = people('Tom',10,30)
p.speak()
