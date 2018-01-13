'''
20180112	jlhung	v1.0
'''

n = int(input())
for i in range(n):
	m = int(input())
	a = list(map(int, input().split()))
	a.sort()
	print("{}".format((a[-1]-a[0]) * 2))