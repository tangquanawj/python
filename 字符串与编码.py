#! /usr/bin/python
# -*- coding:utf-8 -*-
print '%2d-%02d' % (3,1) #%2d的 意思就是后面的数字如果位数超过两位，则显示实际的位数;如果不足，则在前面空对应的位置与数字本身相加=2位
                       #%02d的意思就是后面的数字如果位数超过两位，则显示实际的位数;如果不足，则在前面加0对应的位置与数字本身相加=2位
print '%.2f' % 3.1 #%.2的意思就是决定后面小数点后的位数.如果后面小数的位数不足前面规定的位数，则用0补齐

print 'grown rate: %d %%' % 7 #当字符串中有%时，使用%转义，而不是/
