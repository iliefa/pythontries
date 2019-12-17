from functools import reduce
items=[1,2,3,4,5]

squared=list(map(lambda x: x**2,items))
print(squared)

number_list=range(-10,5)

less_than_zero=list(filter(lambda x: x<0, number_list))
print(less_than_zero)


#reduce
#applies a rolling computation to sequential pairs of values in a list
product=reduce((lambda x,y:x*y),[1,2,3,4])
print(product)