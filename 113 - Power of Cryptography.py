'''
20180114	jlhung	v1.0
'''

while True:
	try:
		m = int(input())
		n = int(input())
	except EOFError:
		break
		
	print(round(n ** (1 / m)))