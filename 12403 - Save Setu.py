'''
20200709    v1.0    jlhung
'''

n = int(input())
d = 0

for _ in range(n):
    m = input()
    
    if m == "report":
        print(d)
    else:
        d += int(m.split()[1])