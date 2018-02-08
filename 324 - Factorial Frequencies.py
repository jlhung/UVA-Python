'''
20180208	jlhung	v1.0
'''

a = [[0 for j in range(10)] for i in range(367)]
n = 1
for i in range(1, 367):
	n *= i
	m = n
	while m > 0:
		a[i][m%10] += 1
		m //= 10
	
while True:
	n = int(input())
	if n == 0:
		break
	
	print("{}! --".format(n))
	for i in range(10):
		print("({}) {} ".format(i, a[n][i]), end="")
		if i == 4:
			print()
	print()
