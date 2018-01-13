'''
20180113 jlhung	v1.0
'''

n = int(input())
for i in range(n):
	c, d = map(int, input().split())
	
	f = 9 * c / 5 + 32
	f += d
	print("Case {}: {:.2f}".format(i+1, (f-32) * 5 / 9))