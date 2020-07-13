'''
20200707    v1.0    jlhung
'''

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    
    print((a//3) * (b//3))