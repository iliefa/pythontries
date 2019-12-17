So a decorator is just a function that returns a function


@my_decorator
def my_func(stuff):
    do_things


    equals to :

def my_func(stuff):
    do_things

my_func = my_decorator(my_func)