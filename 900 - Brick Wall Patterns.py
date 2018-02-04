'''
20180204	jlhung	v1.0
'''

a = [0 for i in range(55)]
a[1], a[2] = 1, 2
for i in range(3, 55):
	a[i] = a[i-1] + a[i-2]
	
while True:
	n = int(input())
	
	if n == 0:
		break
	else:
		print(a[n])