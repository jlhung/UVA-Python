'''
20180114	jlhung	v1.0
'''

def cal(n):
	m = 0
	while n > 0:
		m += n % 10
		n //= 10
	return m

while True:
	n = int(input())
	if n == 0:
		break
	
	while n >= 10:
		n = cal(n)
		
	print(n)