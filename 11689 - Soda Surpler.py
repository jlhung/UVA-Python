'''
20180119	jlhung	v1.0
'''

n = int(input())
for i in range(n):
	x, y, z = map(int, input().split())
	
	total = 0
	s = x + y
	while s // z > 0:
		total += s // z
		s = s // z + s % z
		
	print(total)