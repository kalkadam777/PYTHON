n = int(input())
l = []
k =0
while n!=0:
    l.append(n)
    n = int(input())
for i in l:
    if max(l)==i:
        k+=1
print(k)
