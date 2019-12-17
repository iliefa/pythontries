from collections import namedtuple


#allows for more readable,self-documenting code

#can access fields by name instead of position index
#for assigning field names to result taples returned by the csv or sqlite3 modules

Point= namedtuple('Point',['x','y'])

p=Point(10,y=15)
print(p[0]+p[1])
print(p.x + p.y)

#methods:

# _make -makes a new instance from an existing instance

t=[20,20]
print(Point._make(t))

# _asdict() -> returns an ordereddict 
p = Point(x=11,y=15)
print(p._asdict())

# _replace(**kwargs)

s= Point(x=11,y=30)
print(s._replace(x=33))
