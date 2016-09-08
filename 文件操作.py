#!/usr/bin/python
# -*- coding:utf-8 -*-
#操作文件和目录
import os 

#输出操作系统名字
print os.name

#输出操作系统的详细信息
print os.uname()

#环境变量，输出系统中的所有环境变量和特定的环境变量
print os.environ

#输出特定环境变量的信息
print os.getenv('JAVA_HOME')

#操作文件或目录
#查看当前所在文件夹的绝对路徑
print os.path.abspath('.')
#在某个目录下创建一个新目录
#首先把新目录的完整路徑表示出来
a = os.path.join('.','demotest')
b = os.mkdir(a)
#删掉一个目录：
os.rmdir(a)

#之所以用os.path.join的方法来拼地址的原因是，采用拼字符的方式得到的路经不能使用不同的操作系统
#在linux下，part_1/part_2
#在windows下，part_1\part_2

#同样的道理，要拆分路进是，不要直接去拆字符，而是通过os.path.split()函数，这样可以把一个路经拆为两部分，后面的部分总是最后级别的目录或文件名。
print os.path.split('/home/tang/python/READ.md')

#splittext()函数可以直接得到文件扩展名
print os.path.splitext('/home/tang/python/READ.md')
os.remove('demo.md')
