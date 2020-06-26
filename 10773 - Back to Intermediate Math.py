'''
20200610    jlhung    v1.0
'''
import math

n = int(input())
t = 1

while n > 0:
	d, v, u = list(map(float, input().split()))
	
	if v == 0 or u <= v or u == 0:
		print("Case {}: can't determine".format(t));
	else:
		shortestPathTime = d / math.sqrt(u*u - v*v);
		shortestTime = d / u;
		b = ('%.3f'%round(shortestPathTime - shortestTime, 3))
		print("Case {}: {}".format(t, b))
		
	n -= 1
	t += 1