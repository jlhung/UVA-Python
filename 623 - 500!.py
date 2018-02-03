'''
20180203	jlhung	v1.0
'''

while True:
	try:
		n = int(input())
	except EOFError:
		break
		
	a = 1
	for i in range(2, n+1):
		a *= i
		
	print("{}!".format(n))
	print(a)