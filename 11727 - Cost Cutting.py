'''
20180112	jlhung	v1.0
'''

n = int(input())
for i in range(n):
	a = list(map(int, input().split()))
	a.sort()
	print("Case {}: {}".format(i+1, a[1]))