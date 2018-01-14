'''
20181014	jlhung	v1.0
'''

while True:
	n = int(input())
	if n < 0:
		break
	
	a = ""
	if n == 0:
		a = "0"
		
	while n > 0:
		a = str(n % 3) + a
		n //= 3
	
	print(a)