n=int(input())
factorial_sum=0 # 累加和
current_factorial=1 # 当前的阶乘值
for i in range(1, n+1): # 计算1到n的阶乘并累加
    current_factorial *= i # 计算i的阶乘
    factorial_sum += current_factorial # 累加阶乘值
print(factorial_sum)