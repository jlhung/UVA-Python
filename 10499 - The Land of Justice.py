'''
20180125	jlhung	v1.0
'''

while True:
	n = int(input())
	if n < 0:
		break
	
	if n == 1:
		print("0%")
	else:
		print("{}%".format(n*25))