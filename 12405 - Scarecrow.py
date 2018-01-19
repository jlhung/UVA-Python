'''
20180119	jlhung	v1.0
'''

n = int(input())
case = 1
for i in range(n):
	m = int(input())
	a = list(input())
	
	total = 0
	for j in range(len(a)):
		if a[j] == ".":
			total += 1
			if j+1 < len(a):
				a[j+1] = "#"
			if j+2 < len(a):
				a[j+2] = "#"
			
	print("Case {}: {}".format(case, total))
	case += 1