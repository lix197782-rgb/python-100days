"""
Version: 1.0
Author: Lixiaojie
Description: A for loop that prints each character in a string, skipping spaces, replacing the previous version.
Date: 2025-11-01
"""
# str = "Hello World!"
for char in  "Hello World!":
    if char != ' ': # 跳过空格        
      print(char)   # 输出0到9的数字，不换行
      
str = "I am a student"
for char in str:
    if char == ' ': # 跳过空格        
      continue
    print(char)   # 输出0到9的数字，不换行