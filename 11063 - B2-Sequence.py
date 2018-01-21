'''
20180121	jlhung	v1.0
'''

case = 1
while True:
	try:
		if case > 1:
			input()
		input()
		a = list(map(int, input().split()))
	except EOFError:
		break
	
	c = 1
	b = []
	for i in range(len(a)):
		if i > 0 and a[i] <= a[i-1]:
			c = 0
			break
		elif a[i] < 1:
			c = 0
			break
			
		for j in range(i, len(a)):
			k = a[i] + a[j]
			if k not in b:
				b.append(k)
			else:
				c = 0
				break
		
	if c == 1:
		print("Case #{}: It is a B2-Sequence.".format(case))
	else:
		print("Case #{}: It is not a B2-Sequence.".format(case))
	print("")
	case += 1