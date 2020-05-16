def is_correct(s):
    lst_1 = list()
    lst_3 = list()
    for i in s:
        if i == '(':
            lst_1.append(i)
        elif i ==')':
            if not lst_1:
                return False
            lst_1.pop()
        elif i == '[':
            lst_3.append(i)
        elif i == ']':
            if not lst_3:
                return False
            lst_3.pop()
    if (not lst_1) and (not lst_3):
        return True
    else:
        return False

t = int(input())
while t>0:
    exp  = input()
    flag = is_correct(exp)
    if flag==True:
        print("Yes")
    else:
        print("No") 
    t -= 1