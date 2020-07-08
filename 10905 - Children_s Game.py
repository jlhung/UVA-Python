'''
20200708    v1.0    jlhung 
'''
import functools

def cmp_f(x, y):
    a, b = "".join([x, y]), "".join([y, x])
    if a > b:
        return 1
    elif a <= b:
        return -1

while 1:
    n = int(input())
    if n == 0:
        break
        
    d = input().split()
    t = sorted(d, key=functools.cmp_to_key(cmp_f),
                  reverse=True)
    
    print ("".join(t))