'''
20180120	jlhung	v1.0
'''

a = [56, 96, 36, 76, 16]
n = int(input())

for i in range(n):
	m = int(input())
	
	if m == 0:
		print("1")
	elif m == 1:
		print("66")
	else:
		print(a[(m-2) % 5])