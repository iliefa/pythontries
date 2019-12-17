##lists


l=[1,2,3]
print(l[0])

stack = ['a','b']
stack.append('c')
print(stack)
stack.append(['d','e'])
print(stack)

#append -adds the list

stack= ['a','b']
stack.extend(['c','d','e','f'])

#extends- adds the elements of the list
print(stack)

#index --> searches for an element in a list
my_list=['a','b','c','b','a']
print(my_list.index('b'))
print(my_list.index('b',2)) #index of "second " b

#insert method inserts an object before the index provided
print(my_list)
print("insert element at second index")
my_list.insert(2,'f')
print(my_list)

#remove method - removes the first occurence of an element

my_list.remove('a')
print(my_list)

#pop- removes last element and prints the last element -list a stack 
print(my_list.pop())
print(my_list)

#list as queue
my_list.pop(0) 
print(my_list)
#count 
print(my_list.count('b'))

#sort
my_list.sort(reverse=True)
print(my_list)

#reverse
my_list.reverse()
print(my_list)


#shallow copy

a = [1, 2, [3, 4]]
b=a[:]
a[2][0]=10
print(a)
print(b)

#deep copy

import copy
a=[1,2,[3,4]]
b=copy.deepcopy(a)
a[2][0] = 10
print(a);print(b)



#Tuples -index and count
#faster, immutables
#used as keys in dictionaries

d=dict([('jan',1),('feb',2),('mar',3)])
print(d['feb'])

t=('a','b','c')*4
print(t)
print(t.count('a'))
print(t.index('a'))



