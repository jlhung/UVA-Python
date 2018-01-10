'''
20171216	jlhung	v1.0
'''

num = 1

while True:
	n = int(input())
	
	if n == 0:
		break
	
	a = list(map(int,input().split()))
	
	avg = sum(a) // n
	m = 0
	for i in range(0, n):
		if a[i] > avg:
			m += a[i] - avg
	
	print("Set #%d"%num)
	print("The minimum number of moves is %d.\n"%m)
	num += 1
	