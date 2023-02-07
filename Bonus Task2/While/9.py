n = int(input())
k = 0
l = []
while n!=0:
    l.append(n)
    n = int(input())
for i in range(1,len(l)):
    if l[i-1]<l[i]:
        k+=1
print(k)