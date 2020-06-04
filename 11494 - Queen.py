'''
20200604    jlhung    v1.0
'''

while True:
    b = list(map(int, input().split()))
    
    if b[0] == 0 and b[1] == 0 and b[2] == 0 and b[3] == 0:
        break;
    if b[0] == b[2] and b[1] == b[3]:
        print(0)
    elif (b[0] - b[2])*(b[0] - b[2]) == (b[1] - b[3])*(b[1] - b[3]) or b[0] - b[2] == 0 or b[1] - b[3] == 0:
        print(1)
    else:
        print(2)


