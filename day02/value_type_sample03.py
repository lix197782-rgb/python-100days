"""
Version: 1.0.0
Author: Lixiaojie
Description: 复数类型示例  
Date: 2025-10-22
"""
complex_var1 = 2 + 3j      # 复数类型
complex_var2 = complex(4, -5)  # 使用complex()函数创建复数类型
print(f"复数变量 complex_var1 的值: {complex_var1}, 类型: {type(complex_var1)}")  # <class 'complex'>
print(f"复数变量 complex_var2 的值: {complex_var2}, 类型: {type(complex_var2)}")  # <class 'complex'>   
# 复数的实部和虚部
print(f"complex_var1 的实部: {complex_var1.real}, 虚部: {complex_var1.imag}")
print(f"complex_var2 的实部: {complex_var2.real}, 虚部: {complex_var2.imag}")
# 复数的共轭
print(f"complex_var1 的共轭: {complex_var1.conjugate()}")
print(f"complex_var2 的共轭: {complex_var2.conjugate()}")   
# 复数的加法和乘法
sum_complex = complex_var1 + complex_var2
product_complex = complex_var1 * complex_var2
print(f"complex_var1 + complex_var2 = {sum_complex}")
print(f"complex_var1 * complex_var2 = {product_complex}")   