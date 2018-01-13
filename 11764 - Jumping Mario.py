n = int(input())

for i in range(0, n):
	m = int(input())
	
	x = 0
	high = low = 0
	a = list(map(int, input().split()))
	
	for j in a:
		if x == 0:
			x = j
			continue
		
		if j > x:
			high += 1
		elif j < x:
			low += 1
		x = j
	
	print("Case {0}: {1} {2}".format(i+1, high, low))