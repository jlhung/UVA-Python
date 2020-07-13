'''
20200709    v1.0    jlhung
'''

n = int(input())

for i in range(n):
    t = input()
    pp = list(map(int, input().split()))
    
    Mile = Juice = 0
    for p in pp:
        Mile += (p // 30 + 1) * 10
        Juice += (p // 60 + 1 ) * 15
    
    if Mile == Juice:
        print ("Case {}: Mile Juice {}".format(i+1, Mile))
    elif Mile < Juice:
        print ("Case {}: Mile {}".format(i+1, Mile))
    else:
        print ("Case {}: Juice {}".format(i+1, Juice))