'''
20180108	jlhung	v1.0
'''

def mod(b, p, m):
    if p == 0:
        return 1
    elif p == 1:
        return b % m
    else:
        result = mod(b, p//2, m)
        if p % 2:
            return result * result * b % m
        else:
            return result * result % m
			
while True:
    try:
        b = input()
        if b == "":
            b = int(input())
        else:
            b = int(b)

        p = int(input())
        m = int(input())
    except EOFError:
        break

    print(mod(b, p, m))