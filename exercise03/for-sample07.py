n=int(input("请输入公里数："))
m=int(input("请输入分钟数："))
if n<=3:
    a=13
elif n<15:
    a=13+(n-3)*2.3
else:
    a=13+15*2.3+(n-18)*(0.5*2.3)
totaol=a+n*1
print(f"总费用为:{totaol:.2f}元")