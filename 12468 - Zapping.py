'''
20180113	jlhung	v1.0
'''

while True:
	m, n = map(int, input().split())
	if m == n and m == -1:
		break
	
	print("{}".format(min(max(m, n)-min(m, n), min(m, n)-max(m, n)+100)))