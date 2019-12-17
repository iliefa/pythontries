d={'first':'string value','second':[1,2]}

print(d.keys())

print(d.values())

if 'first' in d : 
    print("true")

#return value of first key
print(d.get('first'))

d.pop('first')
print(d)


#popitem removes and returns a pair ; you do not choose because dictionary is not sorted

d1={'a':[1,2]}
d2=d1.copy()
print(d2)


#clear dictionary

d2.clear()

d={'a':1,'b':2,'c':3}
del d['a']
print(d)

#strings are immutable
