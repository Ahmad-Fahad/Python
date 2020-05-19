if __name__ == '__main__':
	s = input()
	alnum = 0
	alpha = 0
	digit = 0
	lower = 0
	upper = 0
	for i in s:
		if i.isalnum() and alnum == 0:
			print("True")
			alnum = 1
			break
	if alnum == 0:
		print("False")
	for i in s:
		if i.isalpha() and alpha == 0:
			print("True")
			alpha = 1
			break
	if alpha == 0:
		print("False")
	for i in s:
		if i.isdigit() and digit == 0:
			print("True")
			digit = 1
			break
	if digit == 0:
		print("False")
	for i in s:
		if i.islower() and lower == 0:
			print("True")
			lower = 1
			break
	if lower == 0:
		print("False")
	for i in s:
		if i.isupper() and upper == 0:
			print("True")
			upper = 1
			break
	if upper == 0:
		print("False")
