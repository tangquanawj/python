#!/usr/bin/python
# -*- coding:utf-8 -*-

#python中没有直接定义常量的方法，通过定义一个常量类来实现常量的功能

class _const:
    class ConstError(TypeError): pass
        def __setattr__(self,name,value):
            if self.__dict__.has_key(name):
                raise self.ConstError, "Can't rebind const(%s)" % name
                self.__dict__[name] = value
import sys
sys.modules[__name__] = _const()
