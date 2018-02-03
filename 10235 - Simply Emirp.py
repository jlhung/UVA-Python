'''
20180203	jlhung	v1.0
'''

a = [0 for i in range(1000001)]
a[0], a[1] = 1, 1
for i in range(2, 1000001):
	if a[i] == 0:
		for j in range(i+i, 1000001, i):
			a[j] = 1
			
while True:
	try:
		n = int(input())
	except EOFError:
		break
	
	n_s = str(n)
	n_s= n_s[::-1]
	n_s = int(n_s)
	
	if a[n] == 1:
		print("{} is not prime.".format(n))
	elif a[n] == 0 and a[n_s] == 0 and n != n_s:
		print("{} is emirp.".format(n))
	else:
		print("{} is prime.".format(n))