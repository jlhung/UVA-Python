'''
20180113	jlhung	v1.0
'''

n = int(input())
for i in range(n):
	m = input()
	
	x = (ord(m[0])-65) * 26**2 + (ord(m[1])-65) * 26 + (ord(m[2])-65)
	y = int(m[4:])
	
	if abs(x - y) <= 100:
		print("nice")
	else:
		print("not nice")