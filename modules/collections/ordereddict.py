#looks also for order when testing equality
from collections import OrderedDict
print('d1')
d1=OrderedDict()
d1['a']= 'A'
d1['b']= 'B'
d1['c'] = 'C'

for k,v in d1.items():
    print(k,v)

d2=OrderedDict()
d2['b']= 'B'
d2['a']= 'A'
d2['c'] = 'C'
print('d2')
for k,v in d2.items():
    print(k,v)
print('compare the 2 dicts',d1==d2)

d2.move_to_end('a',last=False)
print('d2 after reordering')
for k,v in d2.items():
    print(k,v)
print('compare the 2 dicts',d1==d2)
