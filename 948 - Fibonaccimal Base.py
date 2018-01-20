'''
20180120	jlhung	v1.0
'''

a = [1, 2]
for i in range(2, 40):
	a.append(a[i-1] + a[i-2])
	
n = int(input())
for i in range(n):
	m = int(input())
	print("{} = ".format(m), end="")
	
	c = 0
	for j in range(39, -1, -1):
		if m // a[j] == 1:
			print("1", end="")
			m %= a[j]
			c += 1
		elif c > 0 and m // a[j] == 0:
			print("0", end="")
	
	print(" (fib)");
		