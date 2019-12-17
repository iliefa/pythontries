from itertools import *

#combines the elements of several iterators into tuples

for i in zip([1,2,3],['a','b','c']):
    print(i)

#stops when first input iterator is exhausted

r1=range(5)
r2=range(10)
print(list(zip(r1,r2)))
print(list(zip_longest(r1,r2,fillvalue=0)))