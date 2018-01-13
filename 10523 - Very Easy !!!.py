'''
20180113	jlhung	v1.0
'''


while True:
	try:
		m, n = map(int, input().split())
	except:
		break
	
	sum = 0
	for i in range(1, m+1):
		sum += i * (n ** i)
	
	print(sum)