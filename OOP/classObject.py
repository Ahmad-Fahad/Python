class Square:
	s = 0
	def __init__(self, x):
		self.s = x
	def area(self):
		return self.s * self.s
class Cube:
	s = 0
	def __init__(self, z):
		self.s = z
	def cube(self):
		return self.s*self.s*self.s

sq = Square(4)
print(sq.area())

c = Cube(4)
print(c.cube())
