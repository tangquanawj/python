1.python程序由包(package),模块(module)和函数组成.
包是一系列模块组成的集合，模块以一系列函数和类的集合

2.包就是完成特定任务的工具箱。

3.包必须含有一个__init__.py文件，用于标识当前文件夹是一个包。

4.python的程序由一个个模块组成的，模块把一组相关的函数或代码组织到一个文件里，一个文件即是一个模块。
  模块由代码,函数和类组成。导入模块使用import语句。

5.包的作用：实现函数的复用。

6.函数是一段可以重复多次调用的代码，函数定义实例：
demo:

def arithmetic(x,y,operator):
    result={
        '+':x+y,
        '-':x-y,
        '/':x/y,
        '*':x*y
    }

函数的返回值用return来控制。
