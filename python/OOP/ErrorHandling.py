def divide(x, y):
	try:
		result = x / y
	except ZeroDivisionError:
		print "You can't divide something by zero"
	except TypeError:
		print "you should use only Integers here"
	else:
		return result
	finally:
		print "Inside finally "
	

a = 12

b = 0

print divide(a, b)