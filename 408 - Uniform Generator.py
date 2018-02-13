'''
20180212	jlhung	v1.0
'''

while True:
	try:
		m, n = map(int, input().split())
	except EOFError:
		break
	
	a, b = m, n
	while b % a > 0:
		a, b = b%a, a
	
	print("{:10}{:10}    ".format(m, n), end="")
	if a == 1:
		print("Good Choice")
	else:
		print("Bad Choice")
	print()