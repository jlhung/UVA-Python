'''
20171217	jlhung	v1.0
'''

while True:
	try:
		x, y = map(int, input().split())
	except EOFError:
		break
		
	print(abs(x - y))