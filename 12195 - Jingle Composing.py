'''
20180119	jlhung	v1.0
'''

a = {'W':1, 'H':0.5, 'Q':0.25, 'E':0.125, 
	 'S':0.0625, 'T':0.03125, 'X':0.015625}
	 
while True:
	n = input().split("/")
	if n[0] == "*":
		break
	
	correct = 0
	for i in n:
		t = 0
		for j in i:
			t += a[j]
		if t == 1:
			correct += 1
	
	print(correct)