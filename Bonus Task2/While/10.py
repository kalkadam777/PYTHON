n = int(input())
l = []
while n!=0:
    l.append(n)
    n = int(input())
l.remove(max(l))

print(max(l))