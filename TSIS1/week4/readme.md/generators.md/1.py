def square_gen(N):
    i = 0
    while i <= N:
        yield i ** 2
        i += 1

m = square_gen(10)

for i in m:
    print(i)