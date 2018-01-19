'''
20180119	jlhung	v1.0
'''

n = int(input())
for i in range(n):
	a = list(input().split())
	
	odd = 0
	even = 0
	for j in a:
		for k in range(4):
			if k % 2 > 0:
				odd += int(j[k])
			else:
				t = int(j[k]) * 2
				while t > 0:
					even += t % 10
					t //= 10
	
	if (odd+even) % 10 > 0:
		print("Invalid")
	else:
		print("Valid")