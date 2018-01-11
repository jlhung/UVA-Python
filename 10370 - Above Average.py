'''
20171217	jlhung v1.0
'''

n = int(input())

for i in range(0, n):
	a = list(input().split())
	
	a.pop(0)
	a = list(map(int, a))
	avg = sum(a) / len(a)
	
	high = 0
	for j in a:
		if j > avg:
			high += 1
	
	print("{:.3%}".format(high / len(a)))