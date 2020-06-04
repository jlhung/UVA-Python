'''
20180115	jlhung	v1.0
'''

def deg(n):
	m = 0
	while n > 0:
		m += n % 10
		n //= 10
		
	return m

while True:
	a = int(input())
	if a == 0:
		break
	
	degree = 1
	t = deg(a)
	while t >= 10:
		t = deg(t)
		degree += 1
	
	if t % 9 == 0:
		print("{} is a multiple of 9 and has 9-degree {}.".format(a , degree))
	else:
		print("{} is not a multiple of 9.".format(a))
