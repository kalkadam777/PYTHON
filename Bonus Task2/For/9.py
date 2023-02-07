n = int(input())
l = n*[0]
for i in range(n):
    l[i] = int(input())
k = 0
for i in l:
    if i==0:
        k+=1
print(k)