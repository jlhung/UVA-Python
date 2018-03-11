#20180309	jlhung	v1.0

while(1):
	try:
		a = input()
		b = input()
	except EOFError:
		break

	c = [0 for i in range(26)]
	d = [0 for i in range(26)]
	
	for i in a:
		c[ord(i)-97] += 1
	for i in b:
		if(c[ord(i)-97]) > 0:
			c[ord(i)-97] -= 1
			d[ord(i)-97] += 1
	
	for i in range(26):
		for j in range(d[i]):
			print(chr(i+97), end="")
	print()
		