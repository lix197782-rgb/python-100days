n = int(input("请输入n的值（n>0）："))
if n <= 0:
    print("n必须大于0！")
else:
    total = 0.0 # 和
    for i in range(1, n + 1):
        if i == 1:
            term = 1  # 第1项是1
        else:
            sign = (-1) ** (i + 1)  # 符号交替
            numerator = i - 1       # 分子
            denominator = i         # 分母
            term = sign * (numerator / denominator)
        total += term
    # 保留6位小数输出
    print("前{}项和为：{:.6f}".format(n, total))