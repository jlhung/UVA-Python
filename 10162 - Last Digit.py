'''
20180129	jlhung	v1.0
'''

a = [[0, 1, 4, 7, 6, 5, 6, 3, 6, 9],
     [0, 1, 6, 3, 6, 5, 6, 7, 4, 9]]

	 
while True:
	n = int(input())
	if n == 0:
		break
	
	ans = (n // 10) * 47
	for i in range(1, (n%10)+1):
		ans += a[(n//10)%2][i]

	print(ans % 10)
	