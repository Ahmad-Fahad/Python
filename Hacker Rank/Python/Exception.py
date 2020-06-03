t = int(input())
while t>0:
	t-=1
	dividend, divisor = input().split()
	try:
		q = int(dividend)//int(divisor)
		print(q)
	except ZeroDivisionError:
		print("Error Code: integer division or modulo by zero")
	except ValueError:
		print("Error Code: invalid literal for int() with base 10: {}".format(divisor))

