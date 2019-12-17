import cProfile
import random


def f1(list):
    l1=sorted(list)
    l2=[i for i in l1 if i<0.5]
    return [i*i for i in l2]

def f2(list):
    l1=[i for i in list if i <0.5]
    l2=sorted(l1)
    return [i*i for i in l2]

def f3(list):
    l1=[i *i for i in list]
    l2=sorted(l1)
    return [i for i in l1 if i<(0.5*0.5)]

list=[random.random() for i in range(100000)]
cProfile.run('f1(list)')
cProfile.run('f2(list)')
cProfile.run('f3(list)')