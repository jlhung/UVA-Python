'''
20200709    v1.0    jlhung
'''

case = 0

while True:
    n = input()
    
    if n == "0":
        break
        
    p = list(map(int, input().split()))
    t = sum(1 for i in p if i == 0)
    
    case += 1
    print("Case {}: {}".format(case, len(p) - 2*t))