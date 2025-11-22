epsilon = float(input("请输入小于1的临界值: "))
e = 1.0  # 初始项为1
factorial = 1  # 阶乘初始值（1!）
n = 1
while True:
    term = 1 / factorial  # 当前项1/n!
    if term < epsilon:
        break
    e += term
    n += 1
    factorial *= n  # 计算(n+1)! = n! * (n+1)

print(f"自然常数e的近似值为: {e:.6f}")