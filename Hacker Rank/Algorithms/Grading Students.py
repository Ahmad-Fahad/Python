def gradingStudents(grades):
	result = list()
	for i in grades:
		if i >= 38 and i%5 != 0:
			q = i//5
			r = (q+1)*5
			if (r-i)<3:
				i = r
		result.append(i)	
	return result

if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
print(result)
