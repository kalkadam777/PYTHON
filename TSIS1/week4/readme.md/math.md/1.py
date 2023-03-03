import math
x = int(input())
def toRad(x):
    z = (x*math.pi)/180
    return z

print(round(toRad(x),6))