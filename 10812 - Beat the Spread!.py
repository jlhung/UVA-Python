n = int(input())

while n:
	x, y = map(int, input().split())
	
	if (x+y) % 2 or (x+y) < 0 or (x-y) < 0:
		print("impossible")
	else:
		print(int((x+y) / 2), int((x-y) / 2))
	
	n -= 1