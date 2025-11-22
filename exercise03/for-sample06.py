month = int(input("请输入月份数: "))
if month <= 0:
    print("月份数必须大于0")
elif month == 1 or month == 2:
    print(f"第{month}个月的兔子对数为: 1")
else:
    f1, f2 = 1, 1  # 第1、2个月的对数
    for i in range(3, month + 1):
        f = f1 + f2
        f1, f2 = f2, f  # 更新前两个月的对数
    print(f"第{month}个月的兔子对数为: {f2}")