t = int(input())
while t>0:
	a = int(input())
	sa = set(int(i) for i in input().split())
	b = int(input())
	sb = set(int(i) for i in input().split())
	flag = 0
	for i in sa:
		if i in sb:
			continue
		else:
			flag = 1
	if flag == 1:
		print("False")
	else:
		print("True")
	t -= 1