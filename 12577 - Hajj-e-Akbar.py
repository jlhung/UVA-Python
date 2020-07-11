'''
20200708    v1.0    jlhung
'''

case = 0

while True:
    case += 1
    n = input()
    
    if n == "*":
        break
    elif n == "Hajj":
        print("Case {}: Hajj-e-Akbar".format(case))
    elif n == "Umrah":
        print("Case {}: Hajj-e-Asghar".format(case))
