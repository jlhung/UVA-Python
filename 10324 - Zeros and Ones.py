'''
20200708    v1.0    jlhung 直接算會TIME LIMIT EXCEED
'''

case = 0

while True:
    try:
        s = input() 
        if len(s) == 0:
            break
            
        #作連續記號
        s_tra = [0] * len(s)  
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                s_tra[i] = s_tra[i-1]  
            else:
                s_tra[i] = s_tra[i-1] + 1
                 
        case += 1
        print("Case {}:".format(case))
        
        n = int(input())
        for _ in range(n):
            x, y = map(int, input().split())
            
            if s_tra[x] == s_tra[y]:
                print("Yes")
            else:
                print("No")
    
    except (EOFError):
        break