if __name__ == '__main__':
	n = int(input())
	nm = []
	gd = []
	while n>0:
		nm.append(input())
		gd.append(float(input()))
		n -= 1
	min_1 = gd[0]
	min_2 = None
	for i in range(len(gd)):
		if min_1>gd[i]:
			min_2 = min_1
			min_1 = gd[i]
		elif min_2 == None or min_2 > gd[i]:
			if min_1 != gd[i]:
				min_2 = gd[i]
	tmp_lst = []
	for i in range(len(nm)):
		if min_2 == gd[i]:
			tmp_lst.append(nm[i])
	tmp_lst.sort()
	for i in tmp_lst:
		print(i)