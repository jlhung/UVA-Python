'''
20180112	jlhung	v1.0
'''

while True:
	try:
		m, n = map(int, input().split())
	except EOFError:
		break
		
	print(m ^ n)