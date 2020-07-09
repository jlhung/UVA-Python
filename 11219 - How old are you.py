'''
20200708    v1.0    jlhung
'''

n = int(input())

for i in range(n):
    _ = input()
    
    b1 = list(map(int, input().split("/")))
    b2 = list(map(int, input().split("/")))
    
    if b1[2]*365+b1[1]*30+b1[0] < b2[2]*365+b2[1]*30+b2[0]:
        print("Case #{}: Invalid birth date".format(i+1))
        continue
    
    age = b1[2] - b2[2]
    if b1[1] < b2[1]:
        age -= 1
    elif b1[1] == b2[1] and b1[0] < b2[0]:
        age -= 1
    
    if age > 130:
        print("Case #{}: Check birth date".format(i+1))
    else:
        print("Case #{}: {}".format(i+1, age))