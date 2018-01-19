'''
20180119	jlhung	v1.0
'''

n = int(input())
for i in range(n):
	a = input()
	m = list(map(int, input().split()))
	
	sum = 0
	m.sort(reverse=True)
	for j in range(2, len(m), 3):
		sum += m[j]
	print(sum)