'''
20180113	jlhung	v1.0
'''

a = [1 for i in range(81)]
for i in range(2, 81):
	a[i] = a[i-1] + a[i-2]
	
while True:
	n = int(input())
	if n == 0:
		break
	
	print(a[n])