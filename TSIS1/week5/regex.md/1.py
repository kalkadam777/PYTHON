import re
def text_match(text):
    pattern='^a(b*)$'
    if re.search(pattern,text):
        return 'Found a match'
    else:
        return 'Not match'
print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))
