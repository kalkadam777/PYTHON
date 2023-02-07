n = int(input())
l = []
while n!=0:
    l.append(n)
    n = int(input())
s = sum(l)/len(l)
Sum = 0
for i in l:
    Sum+=(i-s)**2
print((Sum/(len(l)-1))**0.5)
