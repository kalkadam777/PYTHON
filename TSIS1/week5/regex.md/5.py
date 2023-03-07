import re
def text_match(text):
    pattern='a.*b$'
    if re.search(pattern,text):
        return 'True'
    else:
        return 'False'
print(text_match("aabbbbd"))
print(text_match("aabAbbbc"))
print(text_match("accddbbjjjb"))
print(text_match('abbccvdbfb'))
