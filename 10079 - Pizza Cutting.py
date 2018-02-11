'''
20180211	jlhung	v1.0
'''

while True:
	n = int(input())
	if n < 0:
		break
	print("{}".format((n+1)*n//2+1))