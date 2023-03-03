from math import  *
x = int(input())
y = int(input())
def area_pol(n,a):
    s = ceil(((a**2)*n)/4*(tan(pi/n)))
    return s
print(area_pol(x,y))