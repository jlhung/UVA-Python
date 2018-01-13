while True:
    n = int(input())
    if n == 0:
        break
   
    while n > 100:
        n = n // 10 - 5 * (n % 10)

    if not n % 17:
        print("1")
    else:
        print("0")