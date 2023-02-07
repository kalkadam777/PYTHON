n = int(input())
i = 0
while n>=pow(2,i):
    x = pow(2,i)
    i+=1
print(i-1,x)