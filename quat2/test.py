#!/usr/bin/env python3

def findv(x,d):
    key = None
    for v in d:
        if x in d[v]:
            key = v
    return key

d = {'1':['one','ett'], '2':['two','två']}

w = findv('two',d)
print(w)
