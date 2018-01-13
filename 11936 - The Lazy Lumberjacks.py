'''
20180113	jlhung	v1.0
'''

n = int(input())
for i in range(n):
	a = list(map(int, input().split()))
	
	a.sort()
	if a[0] + a[1] > a[2]:
		print("OK")
	else:
		print("Wrong!!")