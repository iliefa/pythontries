from itertools import *
"""
The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state to enable function 
to resume where it is left off. When resumed, the function continues execution immediately after the last yield run. 
This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.
used when we don’t want to store the entire sequence in memory.
"""
for i in chain([1,2,3],['a','b','c']):
    print(i,end=' ')
print()

# chain.from_interable() if the iterables to be combined are not known in advance

def make_iterables_to_chain():
    yield[1,2,3]
    yield['a','b','c']

for i in chain.from_iterable(make_iterables_to_chain()):
    print(i,end= ' ')
print()