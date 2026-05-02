from functools import *

def prost(limit):
    a=[]
    for num in range(2,limit + 1):
        i = range(2,int(num**0.5)+1)
        p = list(filter(lambda p: num % p == 0,i))
        if len(p) == 0:
            a.append(num)        
    yield a

limit = int(input('Введите лимит: '))
for x in prost(limit):
    s = reduce(lambda x, y: x + y, x)
    print(x,s)
