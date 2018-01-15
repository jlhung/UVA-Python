'''
20180115	jlhung	v1.0
'''

c = 0
n = int(input())
for i in range(n):
	a = input().split()
	b = input().split()
	
	start = int(a[2])
	if a[0] == 'January' or a[0] == 'February':
		start -= 1
	
	end = int(b[2])
	d = int(b[1][:len(b[1])-1])
	if b[0] == 'January' or b[0] == 'February':
		end -= 1
	if b[0] == 'February' and d == 29:
		end += 1
		
	start = start//4 - start//100 + start//400;
	end = end//4 - end//100 + end//400;
	c += 1
	print("Case {}: {}".format(c, end-start))