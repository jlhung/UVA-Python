'''
20200709    v1.0    jlhung
'''

n = int(input())

for i in range(n):
    p = []
    max_ = 0
    
    for _ in range(10):
        x, y = input().split()
        
        p.append((x, int(y)))
        if int(y) > max_:
            max_ = int(y)
            
    print("Case #{}:".format(i + 1)) 
    for x, y in p:
        if y == max_:
            print(x)
        