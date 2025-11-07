import math

M=int(input())
N=int(input())
gcd=math.gcd(M,N) # 最大公约数
lcm=(M*N)//gcd # 最小公倍数
print(gcd,lcm)