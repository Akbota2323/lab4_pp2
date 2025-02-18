import math
degree = int(input())
radian = (degree * math.pi)/180
print(radian)

#2
import math
value1 = int(input())
value2 = int(input())
height = int(input())
area = ((value1 + value2)/2)*height
print(area)

#3
import math
num = int(input())
length = int(input())
area_polygon = (num * length * length)/(4*math.tan(math.pi/num))
print(int(area_polygon))

#4
import math
length = int(input())
height = int(input())
area = length * height
print(float(area))
