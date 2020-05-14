def swap_case(s):
	t = ''
	for i in s:
		if i.islower() == True:
			t += i.upper()
		elif i.isupper() == True:
			t += i.lower()
		else:
			t += i
	return t

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)