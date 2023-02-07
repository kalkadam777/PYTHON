n = int(input())
l = []
l.append(0)
l.append(1)
for i in range(1,n):
    l.append(l[i-1]+l[i])
print(l[n])