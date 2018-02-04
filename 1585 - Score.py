'''
20180204	jlhung	v1.0
'''

n = int(input())
for _ in range(n):
	m = input()
	
	c = 1
	sum = 0
	for i in m:
		if i == "O":
			sum += c
			c += 1
		else:
			c = 1
		
	print(sum)