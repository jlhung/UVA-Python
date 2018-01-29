'''
20180129	jlhung	v1.0
'''

c = 1
while True:
	n = int(input())
	if n == 0:
		break
	
	a = []
	for _ in range(n):
		a.append(input())
	
	print("Case {}:".format(c))	
	print("#include<string.h>")
	print("#include<stdio.h>")
	print("int main()")
	print("{")
	
	for i in a:
		print("printf(\"", end="")
		for j in i:
			if j == "\"" or j == "\\":
				print("\\", end="")
			print(j, end="")
		print("\\n\");")
		
	print("printf(\"\\n\");")
	print("return 0;")
	print("}")
	c += 1