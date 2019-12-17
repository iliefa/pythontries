import collections

c= collections.ChainMap()
d= c.new_child()
e= c.new_child()

print(e.maps[0])
print(e.maps[-1])
print(e.parents)
d['x'] = 1
print(d['x'])
del d['x']
print(list(d))