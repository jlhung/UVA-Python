'''
20180113	jlhung	v1.0
'''

a = {}

def cal(x):
	if x in a:
		return a[x]
	
	if x <= 1:
		return 1
	
	if x % 2 == 1:
		y = 3 * x + 1
	else:
		y = x // 2
	
	a[x] = cal(y) + 1
	return a[x]

while True:
	try:
		x, y = map(int, input().split())
	except EOFError:
		break

	max_cycle = 0
	for i in range(min(x, y), max(x, y) + 1):
		n = cal(i)
			
		if n > max_cycle:
			max_cycle = n
	
	print(x, y, max_cycle)
