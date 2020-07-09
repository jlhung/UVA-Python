'''
20200707    v1.0    jlhung
'''

while True:
    try:
        n = int(input())
        if n == 0:
            break
        if n <= 3:
            print(1)
        elif n == 4:
            print(2)
        else:
            print(n)
    
    except EOFError:
        break