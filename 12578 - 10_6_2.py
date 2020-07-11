'''
20200708    v1.0    jlhung
'''

import math

n = int(input())

for _ in range(n):
    m = int(input())
    
    circle = 0.2*m * 0.2*m * math.pi
    rect = m * 0.6*m - circle
    
    print("{:.2f} {:.2f}".format(circle, rect))