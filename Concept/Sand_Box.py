s = input()
t = ""
flag = 0
for i in s:
    if flag == 0:
        t += i.capitalise()
        flag = 1 
    elif i == ' ':
        flag = 1

