l = [1,1,1,1,2,2,2,3,3,4,5,4]
def Set(list):
    l1 = []
    for i in list:
        if i not in l1:
            l1.append(i)
    return l1

print(Set(l))