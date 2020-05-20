s = input()
t = ""
flag = 0
for i in s:
	if flag == 0:
		if i != ' ':
			if(ord(i)>=97 and ord(i)<=122):
				i = chr(ord(i)-32)
			flag=1
		else:
			flag = 0
	t+=i


print(t)
