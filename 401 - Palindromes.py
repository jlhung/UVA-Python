'''
20180203	jlhung	v1.0
'''

a = "A000300HIL0JM0O0002TUVMXY51SE0Z0080"

def cal(z):
	if z >= 65:
		return z - 65
	else:
		return z - 49 + 26

while True:
	try:
		n = input()
	except EOFError:
		break
	
	if n == n[::-1]:
		p = 1
	else:
		p = 0
		
	m = 1
	for i in range(len(n)//2 + 1):
		x = cal(ord(n[i]))

		if a[x] != n[len(n)-1-i]:
			m = 0
			break
			
	if m == 1 and p == 1:
		print("{} -- is a mirrored palindrome.".format(n))
	elif m == 0 and p == 1:
		print("{} -- is a regular palindrome.".format(n))
	elif m == 1 and p == 0:
		print("{} -- is a mirrored string.".format(n))
	else:
		print("{} -- is not a palindrome.".format(n))
	print()
			
		