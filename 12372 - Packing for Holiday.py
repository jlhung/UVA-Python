'''
20200709    v1.0    jlhung
'''

n = int(input())

for i in range(n):
    p = list(map(int, input().split()))
    
    print ("Case {}: {}".format(i+1, "good" if max(p) <= 20 else "bad"))