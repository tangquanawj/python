#!/usr/bin/python
# -*- coding:utf-8 -*-
class Book(object):
    def __setattr__(self,name,value):
        if name == "value":
            object.__setattr__(self,name,value-100)
        else:
            object.__setattr__(self,name,value)

    def __getattr__(self,name):
        try:
            return object.__getattribute__(self,name)
        except:
            return name + ' is not found!'

    def __str__(self):
        return self.name + ' cost: ' + str(self.value)
    
c = Book()
c.name = 'Tom'
c.value = 100

print c.name
print c.value
print c
print c.Type
 
