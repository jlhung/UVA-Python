'''
20180214	jlhung	v1.0
'''

n = int(input())
x = 0
for _ in range(n):
	input()
	b = list(map(int, input().split()))
	c = list(map(str, input().split()))
	
	a = {}
	for i in range(len(b)):
		a[b[i]] = c[i]
	
	if x > 0:
		print()
	x += 1
	
	for key in sorted(a):
		print(a[key])