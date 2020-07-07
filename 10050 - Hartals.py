'''
20200707    v1.0    jlhung
'''

n = int(input())

for _ in range(n):
    d = int(input())
    m = int(input())
    c = [0] * m
    
    for i in range(m):
        c[i] = int(input())
    
    #模擬罷會
    total = 0
    for i in range(1, d+1):
        #跳過星期五星期六
        if i % 7 == 6 or i % 7 == 0:
            continue
        
        #只要一個罷會就加一
        for j in range(m):
            if i % c[j] == 0:
                total += 1
                break
        
    print(total)