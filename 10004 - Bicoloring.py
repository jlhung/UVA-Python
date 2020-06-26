'''
20200610    jlhung    v1.0
'''
point = [0 for i in range(205)]

def dfs(edge, p, m, color):
    answer = 1

    #如已有顏色，則回傳是否相同
    if point[p] != 0:
        if point[p] == color*-1:
            return -1
        else:
            return 1
    
    point[p] = color
    
    for i in range(0, m):
        if str(p)+" "+str(i) in edge:
            answer *= dfs(edge, i, m, color*-1)
        if answer == -1:
            return answer
    
    return answer
    

while True:
    n = int(input())
    
    if n == 0:
        break
        
    m = int(input())
    
    #初始化點
    for i in range(0, n):
        point[i] = 0
    
    #初始化邊
    edge = [0 for i in range(m)]
    
    for i in range(0, m):
        edge[i] = input()
    
    if dfs(edge, 0, m, 1) == 1:
        print("BICOLORABLE.")
    else:
        print("NOT BICOLORABLE.")
        
