'''
20180127	jlhung	v1.0
'''

n = int(input())
for _ in range(n):
	input()
	a = list(map(int, input().split()))
	
	c = 0
	for i in range(len(a)-1):
		for j in range(len(a)-1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
				c += 1
	
	print("Optimal train swapping takes {} swaps.".format(c))