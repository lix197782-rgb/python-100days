"""
Version: 1.0
Author: Lixiaojie
Description:数值类型转换
Date: 2025-10-22
"""
# 整数转换为浮点数
int_var = 100
float_var = float(int_var)
print(f"整数 {int_var} 转换为浮点数: {float_var}, 类型: {type(float_var)}")  # <class 'float'>
# 浮点数转换为整数
float_value = 9.99
int_value = int(float_value)
print(f"浮点数 {float_value} 转换为整数: {int_value}, 类型: {type(int_value)}")  # <class 'int'>
# 整数转换为复数
int_number = 7
complex_number = complex(int_number)
print(f"整数 {int_number} 转换为复数: {complex_number}, 类型: {type(complex_number)}")  # <class 'complex'>
# 浮点数转换为复数
float_number = 5.67