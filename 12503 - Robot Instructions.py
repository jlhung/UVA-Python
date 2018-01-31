'''
20180131	jlhung	v1.0
'''

cmd = []

def cmdin(c):
	if c == "LEFT":
		cmd.append(-1)
		return -1
	elif c == "RIGHT":
		cmd.append(1)
		return 1
	else:
		cmd.append(cmd[int(c) - 1])
		return cmd[-1]

n = int(input())
for _ in range(n):
	m = int(input())
	
	cmd = []
	now = 0
	for i in range(m):
		k = list(input().split())
		if len(k) == 1:
			now += cmdin(k[0])
		else:
			now += cmdin(k[2])
	print(now)
			