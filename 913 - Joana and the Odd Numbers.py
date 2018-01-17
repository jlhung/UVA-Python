'''
20180117	jlhung	v1.0
'''

while True:
	try:
		n = int(input())
	except EOFError:
		break
		
	m = (n+1) // 2
	m = m ** 2 * 2 - 1
	m = 3 * m - 6
	print(m)