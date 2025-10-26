"""
Version: 1.0
Author: lixiaojie
Description: 变量的类型转换操作
Date: 2025-10-22   
"""
# 字符串转整数
str_num = "456" # 定义一个字符串变量
int_num = int(str_num) # 将字符串转换为整数
print(f"字符串 '{str_num}' 转换为整数: {int_num}, 类型: {type(int_num)}")  # <class 'int'>
# 整数转浮点数
int_value = 789
float_value = float(int_value) # 将整数转换为浮点数
print(f"整数 {int_value} 转换为浮点数: {float_value}, 类型: {type(float_value)}")  # <class 'float'>
# 浮点数转字符串
float_num = 3.14159
str_float = str(float_num) # 将浮点数转换为字符串
print(f"浮点数 {float_num} 转换为字符串: '{str_float}', 类型: {type(str_float)}")  # <class 'str'>
# 布尔值转整数
bool_value = False