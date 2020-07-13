'''
20200709    v1.0    jlhung 前後時間有交集就無法開會
'''

from datetime import datetime

n = int(input())

for i in range(n):
    time1 = input().split()
    time2 = input().split()
    
    wife = []
    meeting = []
    for t in time1:
        x, y = map(int, t.split(":"))
        wife.append(datetime(2000, 1, 1, x, y, 0))
    for t in time2:
        x, y = map(int, t.split(":"))
        meeting.append(datetime(2000, 1, 1, x, y, 0))
        
    if wife[1] < meeting[0] or meeting[1] < wife[0]:
        print("Case {}: Hits Meeting".format(i+1))
    else:
        print("Case {}: Mrs Meeting".format(i+1))