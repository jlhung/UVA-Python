'''
20180113	jlhung	v1.0
'''

while True:
	try:
		m, n = map(int, input().split())
		a = list(map(int, input().split()))
	except EOFError:
		break
	
	if m == n:
		print("*")
	else:
		for i in range(1, m+1):
			if i not in a:				
				print("{} ".format(i), end="")
		print("")