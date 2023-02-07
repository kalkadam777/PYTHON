n = int(input())
l = []
while n!=0:
    l.append(n)
    n = int(input())
print(l.index(max(l)))