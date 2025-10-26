"""
version: 1.0
author: lixiaojie
Description: 使用type函数检查变量的类型
Date: 2025-10-22
"""
a = 100
b = 123.45
c = 'hello, world'
d = True

print(f"变量a的值: {a}, 类型: {type(a)}")  # <class 'int'>
print(f"变量b的值: {b}, 类型: {type(b)}")  # <class 'float'>
print(f"变量c的值: {c}, 类型: {type(c)}")  # <class 'str'>
print(f"变量d的值: {d}, 类型: {type(d)}")  # <class 'bool'>
# 通过type函数可以方便地检查变量的类型，有助于调试和理解代码行为。
# 运行结果:
# 变量a的值: 100, 类型: <class 'int'>
# 变量b的值: 123.45, 类型: <class 'float'>
# 变量c的值: hello, world, 类型: <class 'str'>
# 变量d的值: True, 类型: <class 'bool'>
