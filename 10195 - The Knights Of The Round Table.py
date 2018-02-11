'''
20180211	jlhung	v1.0
'''

while True:
	try:
		a, b, c = map(float, input().split())
	except EOFError:
		break
	
	if a + b + c == 0:
		print("The radius of the round table is: 0.000");
	else:
		n = (a+b+c) / 2
		m = (n*(n-a)*(n-b)*(n-c)) ** 0.5
		r = (2*m) / (a+b+c)
		print("The radius of the round table is: {:.3f}".format(r));