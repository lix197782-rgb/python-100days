import math
a=float(input())
b=float(input())
radians=math.radians(60) # 60度转换为弧度
sin60=math.sin(radians)
cos60=math.cos(radians)
c=-b+((2*a*sin60*cos60)**0.5)
x=c/(2*a)
print(x)