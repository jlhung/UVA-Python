'''
20180103	jlhung	v1.0
'''

a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

n = int(input())
for i in range(n):
	x, y = map(int, input().split())
	
	for j in range(x-1):
		y += a[j]
	
	y -= 1
	if y % 7 == 0:
		print("Saturday")
	elif y % 7 == 1:
		print("Sunday")
	elif y % 7 == 2:
		print("Monday")
	elif y % 7 == 3:
		print("Tuesday")
	elif y % 7 == 4:
		print("Wednesday")
	elif y % 7 == 5:
		print("Thursday")
	elif y % 7 == 6:
		print("Friday")