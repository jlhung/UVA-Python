'''
20180111	jlhung	v1.0
'''

n = int(input())

for i in range(n):
	m = input()

	if len(m) == 5:
		print("3")
		continue
	
	x = 0
	if m[0] == 'o':
		x += 1
	if m[1] == 'n':
		x += 1
	if m[2] == 'e':
		x += 1
		
	if x > 1:
		print("1")
	else:
		print("2")
