'''
20171216	jlhung	v1.0
'''

while True:
	n = int(input())
	
	if n == 0:
		break

	if n <= 100:
		print("f91({0}) = 91".format(n))
	else:
		print("f91({0}) = {1}".format(n, n-10))