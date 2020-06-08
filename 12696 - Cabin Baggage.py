'''
20200608    jlhung    v1.0
'''

n = int(input())
sum = 0

while n > 0:
    b = list(map(float, input().split()))
    
    if b[3] > 7:
        print(0)
    elif (b[0]+b[1]+b[2] > 125 and (b[0] > 56 or b[1] > 45 or b[2] > 25)):
        print(0)
    else:
        print(1)
        sum += 1
    n -= 1   

print(sum)