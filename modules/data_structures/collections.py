#generators : don't return a value, they yield it

def generator_function():
    for i in range(10):
        yield i 

for item in generator_function():
    print(item)

def fib(n):
    a=b=1
    for i in range(n):
        yield a 
        a,b= b,a+b

for x in fib(1000):
    print(x)