import operations

a = operations.add(11,22)

b = operations.sub(22,11)

c = operations.mul(11,2)

d = operations.div(22,2)

print a
print b
print c
print d

print operations.PI

from my_math.geo.circle import area

result = area(12)

print result

import my_math.geo.square as sq_area

result = sq_area.area(12)

print result