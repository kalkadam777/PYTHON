str = input()
c = 0
for i in range(len(str)):
    if 'f'==str[i]:
        c+=1

if c>1:
    x = str[::-1].find('f')
    y = str.find('f')
    print(y,len(str)-1-x)
elif c==1:
    z = str.find('f')
    print(z)
      