'''
20180117	jlhung	v1.0
'''

n = int(input())
for i in range(n):
	m = int(input())
	
	sum = 0
	for j in  range(m):
		a = list(map(int, input().split()))
		sum += a[0] * a[2]
		
	print(sum)