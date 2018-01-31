'''
20180131	jlhung	v1.0
'''

c = 1
n = int(input())
for _ in range(n):
	x = list(input())
	y = list(input())
	
	a, b = 0, 0
	
	t = 0
	for i in range(len(x)-1,-1,-1):
		if x[i] == "1":
			a += 2 ** t
		t += 1
	
	t = 0
	for i in range(len(y)-1,-1,-1):
		if y[i] == "1":
			b += 2 ** t
		t += 1
	
	while b > 0:
		a, b = b, a%b
	
	if a != 1:
		print("Pair #{}: All you need is love!".format(c))
	else:
		print("Pair #{}: Love is not all you need!".format(c))
	c += 1