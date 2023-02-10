def solve(h,l):
    y = (4*h-l)/2
    x = h - y
    return 'Rabbits: {} \nChickens: {}'.format(int(x),int(y))

print(solve(35,94))
    