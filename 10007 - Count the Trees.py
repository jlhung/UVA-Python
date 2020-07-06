'''
20200706	jlhung	v1.0 卡特蘭樹
'''

while True:
    n = int(input())
    
    if n == 0:
        break
    
    total = 1
    for i in range(n+2, 2*n+1):
        total *= i
    
    print(total)