'''
20200707    v1.0    jlhung
'''

while True:
    try:
        n = int(input())
        s = list(map(int, input().split()))
        
        print(sum(i == n for i in s))
        
    except EOFError:
        break