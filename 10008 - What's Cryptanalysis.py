'''
20180121	jlhung	v1.0
'''
a = {chr(65+i) : 0 for i in range(26)}
n = int(input())

for i in range(n):
	m = list(input().split())
	
	for j in m:
		for k in range(0, len(j)):
			x = ord(j[k])
			if x >= 65 and x <= 90:
				a[chr(x)] += 1
			elif x >= 97 and x <= 122:
				a[chr(x - 97 + 65)] += 1

b = sorted(a.items(), key = lambda d:d[1], reverse = True)  
for key, value in b:
	if value > 0:
		print("{} {}".format(key, value))
