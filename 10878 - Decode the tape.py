'''
20200708    v1.0    jlhung 
'''

chk = -1
msg = []

while True:
    d = input()
    
    if d == "___________":
        if chk == -1:
            chk *= -1
            msg = []
            continue
        else:
            msg.pop()   #去除換行
            print("".join(msg))
            break
    
    m = 0
    for i in range(len(d)):
        if d[i] == "o":
            m = m*2 + 1
        elif d[i] == " ":
            m = m*2

    msg.append(chr(m))
