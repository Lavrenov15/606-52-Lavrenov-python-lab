from functools import *

def prost(limit):
    a=[]
    for num in range(2,limit + 1):
        i = range(2,int(num**0.5)+1)
        p = list(filter(lambda p: num % p == 0,i))
        if len(p) == 0:
            a.append(num)
            s = reduce(lambda x, y: x + y, a)
    yield a,s

limit = 10
for x in prost(limit):
    print(x)