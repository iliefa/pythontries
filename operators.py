# + operator can be used to extend a list

my_list=[1]
my_list+=[2]
print(my_list)
(my_list)*=2
print(my_list)


#slicing In Python 3.x range is a iterator. So, you need to convert it to a list:
#from 1 to 5
a=list(range(0,6)) 
print(a)
print(a[2:])

print(a[:2])
print(a[2:-1])
print(a[-1])

#list comprehension

a=[i for i in range(10) if i%2==0]
print(a)

li=list(range(0,20))
print([i*2 for i in li if i>9])