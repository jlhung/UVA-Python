'''
20180112	jlhung	v1.0
'''

while True:
	try:
		m, n = map(str, input().split())
	except EOFError:
		break
		
	if len(m) > len(n):
		print("No")
	else:
		k = 0
		for i in range(len(n)):
			if m[k] == n[i]:
				k += 1
			if k == len(m):
				break
		
		if k == len(m):
			print("Yes")
		else:
			print("No")
		