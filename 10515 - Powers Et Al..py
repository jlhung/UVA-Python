'''
20200706	jlhung	v1.0 直接計算會Timeout 次方會有規律性 取最後一位的規律查表即可
'''

#建表查詢
b = [[0, 0, 0, 0],
     [1, 1, 1, 1],
     [2, 4, 8, 6],
     [3, 9, 7, 1], 
     [4, 6, 4, 6],
     [5, 5, 5, 5],
     [6, 6, 6, 6],
     [7, 9, 3, 1],
     [8, 4, 2, 6],
     [9, 1, 9, 1]]

while True:
    m, n = map(int, input().split())
    
    if m + n == 0:
        break
    
    if n == 0:
        print(1)
    else:
        print(b[m % 10][(n-1) % 4])