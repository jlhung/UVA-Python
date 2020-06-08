'''
20200605    jlhung    v1.0
'''

x = 2147483647

while True:
	try:
		n = input()
	except EOFError:
		break

	print(n)
	b = list(n.split())
	if int(b[0]) > x:
		print("first number too big")
	if int(b[2]) > x:
		print("second number too big")
	if b[1] == "+" and int(b[0]) + int(b[2]) > x:
		print("result too big")
	elif b[1] == "*" and int(b[0]) * int(b[2]) > x:
		print("result too big")