import math
n=int(input("请输入一个数："))
a=float(input("请输入左端带=点a的值："))
b=float(input("请输入右端带=点b的值："))
dx= (b - a) / n
area=0.0
for i in range(n):
    x1=a+i*dx # 计算左端点x1
    x2=a+(i+1)*dx  # 计算右端点x2
    fx1=math.sin(x1)  # 计算左端点函数值
    fx2=math.sin(x2)  # 计算右端点函数值
    area+= (fx1+fx2)*dx/2  # 梯形面积累加
print("sin(x)在[{:.2f},{:.2f}]区间的近似积分值为：{:.6f}".format(a,b,area)) 
    