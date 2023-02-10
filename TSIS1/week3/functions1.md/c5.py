from itertools import permutations
str = input()
def Permutations(str):
    lst = list(permutations(str))
    return lst

print(Permutations(str))