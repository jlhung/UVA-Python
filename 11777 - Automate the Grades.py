'''
20200708    v1.0    jlhung 
'''

n = int(input())

for i in range(n):
    s = list(map(int, input().split()))
    s_t = s[4:]
    s_t.sort()
    total = sum(s[0:4]) + sum(s_t[1:]) / 2
    
    if total >= 90:
        grade ='A'
    elif 80 <= total < 90:
        grade = 'B'
    elif 70 <= total < 80:
        grade = 'C'
    elif 60 <= total < 70:
        grade = 'D'
    else:
        grade = 'F'
        
    print ("Case {}: {}".format(i+1, grade))