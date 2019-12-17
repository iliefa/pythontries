# supports thread safe ,memory efficient appends nad pops with o(1) performance in either direction

#functions:
# append, appendleft, clear,copy,count, extend,extendleft, index,insert,pop,popleft, remove,reverse,rotate,maxlen

from collections import deque

d= deque('this is life')
print(d.pop()) # return and remove the last element
for i in d:
    print(i.upper())
print('h' in d)
d.extend('jkl')
print(d)
d.extendleft('kool')
print(d)
print(list(d))

c= deque('experiment')
print(c)
c.rotate(1)
print(c)
e= deque('love')
#interesting - implement deletion using rotate
e.rotate(-1)
print(e)
e.popleft()
print(e)
e.rotate(1)
print(e)
def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)

f= deque('totally awesome')    
delete_nth(f, 2)   
print(list(f))