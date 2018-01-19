'''
20180119	jlhung	v1.0
'''

case = 1
n = int(input())
for i in range(n):
	a = list(map(int, input().split()))
	
	print("Case {}: {}".format(case, a[a[0] // 2 + 1]))
	case += 1