import re
def text_match(text):
    pattern='ab{2,3}'
    if re.search(pattern,text):
        return 'Found'
    else:
        return 'Not found'
print(text_match('ab'))
print(text_match('aabbbbbc'))
print(text_match('abb'))
