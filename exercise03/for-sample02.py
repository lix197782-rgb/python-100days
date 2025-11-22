num=int(input("请输入一个3位数:"))
a=num//100
b=(num//10)%10
c=num%10
d=a**3+b**3+c**3**3
if d==num:
    print(f"{num}是水仙花数")
else:
    print(f"{num}不是水仙花数")