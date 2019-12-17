import collections

cnt=collections.Counter('extremely')

print(cnt)
print(list(cnt.elements()))

c=collections.Counter('abracadrabrabardadra')
print(c.most_common(3))
print(list(c.elements()))