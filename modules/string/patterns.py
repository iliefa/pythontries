import re

pattern= 'this'
text = 'does this text match your pattern'

match=re.search(pattern,text)
s=match.start()
e=match.end()
print('Found "{}"\nin "{}"\nfrom {} to {}'.format(
    match.re.pattern, match.string, s, e, text[s:e]))