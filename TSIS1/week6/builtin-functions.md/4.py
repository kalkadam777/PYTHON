def istrue(_tuple):
    c=0
    for i in _tuple:
        if i==True:
            c+=1
    if c==len(_tuple):
        return True
    return False
    
print(istrue((True,True,True,True,True)))