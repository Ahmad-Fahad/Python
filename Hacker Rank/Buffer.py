if __name__ == '__main__':
	n = int(input())
	nm = []
	gd = []
	while n>0:
		nm.append(input())
		gd.append(input())
		n -= 1
	max_1 = gd[0]
	max_2 = gd[0]
	for i in range(len(gd)):
		if max_1<gd[i]:
			max_2 = max_1
			max_1 = gd[i]
		elif min_2 == None or min_2 > lst[i]:
			min_2 = lst[i]
	tmp_lst = []
	for i in range(len(nm)):
		if max_2 == gd[i]:
			tmp_lst.append(nm[i])
	tmp_lst.sort()
	for i in tmp_lst:
		print(i)