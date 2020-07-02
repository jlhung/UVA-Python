'''
20200702    v1.0    jlhung
'''

F = [ i for i in range(0, 5000)]
F[0] = F[1] = 1

for i in range(2, 5000):
    F[i] = F[i-1] + F[i-2]

while True:
    try:
        n = int(input())
        
        #注意
        if n == 0:
            print("The Fibonacci number for 0 is 0")
        else:
            print("The Fibonacci number for {} is {}".format(n, F[n-1]))
    except EOFError:
        break
