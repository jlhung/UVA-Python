'''
20180103	jlhung	v1.0
'''

while True:
	m, n = map(int, input().split())
	if m == 0 and n == 0:
		break
	
	sum = 0
	x = 0
	while m > 0 or n > 0:		
		if m % 10 + n % 10 + x >= 10:
			sum += 1
			x = 1
		else:
			x = 0
			
		m //= 10
		n //= 10
	
	if sum == 0:
		print("No carry operation.")
	elif sum == 1:
		print("1 carry operation.")
	else:
		print("{} carry operations.".format(sum))