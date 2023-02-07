def fact(n):
    rez = 1
    for i in range(1,n+1):
        rez*=i
    return rez
Sum = 0
n = int(input())
for i in range(1,n+1):
    Sum+=fact(i)
print(Sum)

    