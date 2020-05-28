class Repr:
	def __init__(self, x,y):
		self.x = x
		self.y = y
	def __repr__(self):
		#return "x = {} \ny = {}".format(self.x, self.y)
		return repr(self.x)
r = Repr(3,5)
print(repr(r))


msg = "Hellow world"
print(repr(msg))