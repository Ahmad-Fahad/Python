def fnc(x, y, z = 0):
	
	x = x * 10
	y = y * 100
	z = z * 1000

	return x,y,z


a,b,c = fnc(11,22,33)

print a
print b
print c

v = fnc(12,13,14)

print v[0]
print v[1]
print v[2]