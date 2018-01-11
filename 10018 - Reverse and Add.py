'''
20180111	jlhung	v1.0
'''

n = int(input())

for i in range(n):
	m = int(input())
	count = 0
	
	while True:
		str_m = str(m)
		if str_m == str_m[::-1]:
			break
		m += int(str_m[::-1])
		count += 1
	
	print(count, m)