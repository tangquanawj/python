python的三种文件类型：
1.源代码:
	这些代码不需要编译，直接由python解释器解释运行，扩展名为.py
2.字节编码:
	源文件经过编译后生成的文件.pyc，为编译过的字节文件。这种文件不能使用文本编辑器修改，但可以在大多数操作系统上运行。
	import py_compile
	py_compile.compile('hello.py')
3.优化代码:经过优化的源文件以.pyo为后缀，也不能用文本编辑起修改。如下命令为：
	python -O -m py_compile hello.py
