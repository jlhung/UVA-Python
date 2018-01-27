'''
20180127	jlhung	v1.0
'''

a = {}

m, n = map(int, input().split())
for _ in range(m):
	x, y = input().split()
	a[x] = y

for _ in range(n):
	k = input()

	if k in a:
		print(a[k])
	elif k[-1] == "y" and k[-2] != "a" and k[-2] != "e" and k[-2] != "i" and k[-2] != "o" and k[-2] != "u":
		print(k[:-1], end="")
		print("ies")
	elif k[-1] == "o" or k[-1] == "s" or k[-1] == "x":
		print(k, end="")
		print("es")
	elif k[-2:] == "ch" or k[-2:] == "sh":
		print(k, end="")
		print("es")
	else:
		print(k, end="")
		print("s")
