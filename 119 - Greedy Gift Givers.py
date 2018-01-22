'''
20180122	jlhung	v1.0
'''

c = 0
while True:
	try:
		n = int(input())
	except EOFError:
		break
		
	a = {x : 0 for x in list(input().split())}
	for i in range(n):
		m = list(input().split())
		m[1], m[2] = int(m[1]), int(m[2])
		
		if m[2] != 0:
			add = m[1] // m[2]
			sub = m[1] - (m[1] % m[2])
			for j in range(m[2]):
				a[m[3+j]] += add
			a[m[0]] -= sub
	
	if c > 0:
		print()
	for key, value in a.items():
		print("{} {}".format(key, value))
	c += 1