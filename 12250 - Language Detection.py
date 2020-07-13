'''
20200709    v1.0    jlhung
'''

p = {
    'HELLO': 'ENGLISH',
    'HOLA': 'SPANISH',
    'HALLO': 'GERMAN',
    'BONJOUR': 'FRENCH',
    'CIAO': 'ITALIAN',
    'ZDRAVSTVUJTE': 'RUSSIAN'
}

case = 0

while True:
    n = input()
    
    if n == "#":
        break
    
    case += 1
    try:
        print('Case {}: {}'.format(case, p[n]))
    except (KeyError):
        print('Case {}: UNKNOWN'.format(case))

    