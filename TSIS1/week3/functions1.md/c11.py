st = input()

def is_palindrom(_s):
    if _s==_s[::-1]:
        return True
    return False

print(is_palindrom(st))