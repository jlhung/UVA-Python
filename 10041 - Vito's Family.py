'''
20200605    jlhung    v1.0
'''


n = int(input())

while n > 0:
	b = list(map(int, input().split()))
	del b[0]
	b.sort()
	c = b[len(b) // 2]
	
	sum = 0
	for i in range(0, len(b)):
		sum += abs(c - b[i])
	print(sum)
	
	n -= 1