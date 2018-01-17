'''
20180118	jlhung	v1.0
'''

while True:
	try:
		n = int(input())
	except EOFError:
		break
	
	print(n + n // 2)