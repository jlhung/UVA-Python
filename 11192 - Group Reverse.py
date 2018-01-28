'''
20180128	jlhung	v1.0
'''

while True:
	n = input()
	if n == "0":
		break
	
	m, a = n.split()
	x = len(a) // int(m)
	b = []
	for i in range(x-1, len(a), x):
		for j in range(x):
			b.append(a[i-j])
	
	print("".join(b))