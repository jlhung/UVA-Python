'''
20200708    v1.0    jlhung
'''
 
while True:
    n = input()

    if n == "END":
        break
    
    #注意1
    if n == "1":
        print(1)
        continue

    ans = 1
    p = len(n)
    tmp = 0
    while True:
        if tmp == p:
            break
        tmp = p
        p = len(str(p))
        ans += 1

    print(ans)