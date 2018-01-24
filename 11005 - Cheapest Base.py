'''
20180124	jlhung	v1.0
'''

n = int(input())
for i in range(n):
	a = []
	for j in range(4):
		a += map(int, input().split())
	
	m = int(input())
	
	if i > 0:
		print()
	print("Case {}:".format(i+1))
	
	for j in range(m):
		number = int(input())
		total = [0 for i in range(35)]
		
		for k in range(2, 37):
			t = number
			while t > 0:
				total[k-2] += a[t % k]
				t //= k
		
		min_money = min(total)
		print("Cheapest base(s) for number {}:".format(number), end="")
		for k in range(35):
			if total[k] == min_money:
				print(" {}".format(k+2), end="")
		print()
		
