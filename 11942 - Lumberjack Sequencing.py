'''
20180114	jlhung	v1.0
'''

n = int(input())
print("Lumberjacks:")
for i in range(n):
	a = list(map(int, input().split()))
	a_sort1 = sorted(a)
	a_sort2 = sorted(a, reverse=True)
	
	if a == a_sort1 or a == a_sort2:
		print("Ordered")
	else:
		print("Unordered")
	
	