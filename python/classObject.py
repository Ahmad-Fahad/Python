class Square:

	def __init__(self, x):
		
		self.side = x

	def area(self):

		return self.side * self.side

sq = Square(4)

print sq.area()