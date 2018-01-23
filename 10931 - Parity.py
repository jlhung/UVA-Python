'''
20180123	jlhung	v1.0
'''

while True:
	n = int(input())
	if n == 0:
		break
	
	a = []
	while n > 0:
		a.append(str(n % 2))
		n //= 2

	a.reverse()
	print("The parity of {} is {} (mod 2).".format("".join(a), a.count("1")))