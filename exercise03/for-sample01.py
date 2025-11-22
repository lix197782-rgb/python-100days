n=int(input("请输入一个正整数："))
count=0 # 记录运算次数
if n<=0:
    print("ERROR")
else:
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        count+=1
        print(f"第{count}次运算之后:{n}")
    print(f"总共运算了{count}次")