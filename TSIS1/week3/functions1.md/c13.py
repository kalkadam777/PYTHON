from random import randrange
st = input('Hello! What is your name?\n')
x = randrange(1,20+1)
k = 1

st1 = int(input('Well, KBTU, I am thinking of a number between 1 and 20.\nTake a guess.\n'))

while st1 != x:
    if st1<x:
        print('Your guess is too low.\nTake a guess.')
    else:
        print('Your guess is too high\nTake a guess.')
    st1 = int(input())
    k+=1
    
if st1==x:
    print('Good job, KBTU! You guessed my number in {} guesses!'.format(k))

    