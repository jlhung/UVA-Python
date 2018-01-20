'''
20180121	jlhung	v1.0
'''

a = {}

n = int(input())
for i in range(n):
	n = list(input().split())
	
	if n[0] not in a:
		a[n[0]] = 1
	else:
		a[n[0]] += 1
	
b = sorted(a)
for i in b:
	print("{} {}".format(i, a[i]))