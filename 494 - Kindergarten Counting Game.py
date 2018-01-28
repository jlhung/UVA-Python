'''
20180128	jlhung	v1.0
'''

while True:
	try:
		a = list(input().split())
	except EOFError:
		break
	
	total = 0
	for i in a:
		c = 0
		for j in i:
			if (65 <= ord(j) and ord(j) <= 90) or (97 <= ord(j) and ord(j) <= 122):
				if c == 0:
					total += 1
					c = 1
			else:
				if c == 1:
					c = 0
				
	print(total)