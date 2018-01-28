'''
20180128	jlhung	v1.0
'''

n = int(input())
for _ in range(n):
	m = int(input())
	
	a = [0 for i in range(10)]
	for i in range(1, m+1):
		j = i
		while j > 0:
			a[j%10] += 1
			j //= 10
		
	for i in range(len(a)):
		if i > 0:
			print(" {}".format(a[i]), end="")
		else:
			print("{}".format(a[i]), end="")
	print()