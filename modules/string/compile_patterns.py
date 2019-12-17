import re

regexes=[
    re.compile(p)
    for p in ['this','that']
]

text=' does this text match your pattern'

print('text {!r}\n'.format(text))

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern),
        end=' ')
    if regex.search(text):
        print('match')
    else:
        print('no match')
