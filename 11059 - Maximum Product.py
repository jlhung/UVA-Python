'''
20180118	jlhung	v1.0
'''

case = 1
while True:
	try:
		if case != 1:
			m = input()
		n = int(input())
		a = list(map(int, input().split()))
	except EOFError:
		break

	max = 0
	for i in range(len(a)):
		t = 1
		for j in range(i,len(a)):
			t *= a[j]
			if t > max:
				max = t
				
	print("Case #{}: The maximum product is {}.".format(case, max))
	print("")
	case += 1
	