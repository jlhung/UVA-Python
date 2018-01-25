'''
20180125	jlhung	v1.0
'''

a = {'c':[2, 3, 4, 7, 8, 9, 10], 'd':[2, 3, 4, 7, 8, 9], 
	 'e':[2, 3, 4, 7, 8], 		 'f':[2, 3, 4, 7],
	 'g':[2, 3, 4], 			 'a':[2, 3], 
	 'b':[2], 					 'C':[3], 
	 'D':[1, 2, 3, 4, 7, 8, 9],  'E':[1, 2, 3, 4, 7, 8],
	 'F':[1, 2, 3, 4, 7], 		 'G':[1, 2, 3, 4],
	 'A':[1, 2, 3], 			 'B':[1, 2]}
	 
n = int(input())
for _ in range(n):
	m = input()
	
	sum = [0 for i in range(11)]
	now = [0 for i in range(11)]
	for i in m:
		for j in range(1, 11):
			if j in a[i]:
				if now[j] != 1:
					sum[j] += 1
					now[j] = 1
			else:
				now[j] = 0
			
	for i in range(1, len(sum)):
		if i > 1:
			print(" ", end="")
		print(sum[i], end="")
	print()