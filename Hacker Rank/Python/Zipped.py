if __name__=="__main__":
	student_number, subject_number = input().split()
	subject_number = int(subject_number)
	sb_num = subject_number
	marks = []
	for i in range(subject_number):
		x = [float(i) for i in input().split()]
		marks = marks + [x]
	subject_number -= 1
	avg_lst = []
	std_marks = list(zip(*marks))
	for i in std_marks:
		avg_lst.append(sum(i)/sb_num)
	for i in avg_lst:
		print(i)
		


