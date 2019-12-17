import collections

#for quickly linking a number of mappings so they can be treated as a single unit.

baseline= {'music':'bach','art':'rembrandt'}
adjustments={'art':'van gogh','opera':'carmen'}
chain = collections.ChainMap(adjustments,baseline)
print(list(chain))
print(list(chain.keys()))
print(list(chain.values()))