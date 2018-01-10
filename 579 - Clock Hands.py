'''
20180103	jlhung	v1.0
'''

while True:
	h, m = map(int, input().split(":"))
	if h == 0 and m == 0:
		break
	
	m_angle = 6 * m
	h_angle = h * 30 + m * 0.5 if h < 12 else m * 0.5
	m_n = abs(m_angle - h_angle)
	m_n = m_n if m_n < 180 else 360 - m_n
	print("{:.3f}".format(m_n))