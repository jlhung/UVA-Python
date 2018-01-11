'''
20180111	jlhung	v1.0
'''

a = []

while True:
	try:
		a.append(int(input()))
	except EOFError:
		break
	
	a.sort()
	half = len(a) // 2
	print( int( (a[half] + a[~half]) / 2 ) )
	
	