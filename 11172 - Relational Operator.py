'''
20180114	jlhung	v1.0
'''

n = int(input())
for i in range(n):
	x, y = map(int, input().split())
	
	if x > y:
		print(">")
	elif x < y:
		print("<")
	else:
		print("=")