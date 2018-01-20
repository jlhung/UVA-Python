'''
20180120	jlhung	v1.0
'''

c = 0
while True:
	n = list(map(int, input().split()))
	if n[0] == 0:
		break
	
	win = [0 for i in range(n[0]+1)]
	lost = [0 for i in range(n[0]+1)]
	
	total = n[0] * n[1] * (n[0]-1) // 2
	for j in range(total):
		a = list(input().split())
		if a[1] != a[3]:
			if a[1] == "rock" and a[3] == "scissors" or a[1] == "scissors" and a[3] == "paper" or a[1] == "paper" and a[3] == "rock":
				win[int(a[0])] += 1
				lost[int(a[2])] += 1
			else:
				win[int(a[2])] += 1
				lost[int(a[0])] += 1
	
	if c > 0:
		print("")
	c += 1
	
	for i in range(1, len(win)):
		if win[i] == 0 and lost[i] == 0:
			print("-")
		else:
			print("{:.3f}".format(win[i]/(win[i]+lost[i])))
	