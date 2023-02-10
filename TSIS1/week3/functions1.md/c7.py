l = [1,3,3]

def has_33(list):
    for i in range(1,len(list)):
        if list[i-1]==list[i]:
            return True
    return False

print(has_33(l))