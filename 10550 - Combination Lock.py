'''
20180120	jlhung	v1.0
'''

while True:
	a = list(map(int, input().split()))
	if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0:
		break
	
	angle = 1080
	angle += (a[0] - a[1] + 40) % 40 * 9
	angle += (a[2] - a[1] + 40) % 40 * 9
	angle += (a[2] - a[3] + 40) % 40 * 9
	print(angle)