class cls_parent:
	x = 10
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def demonstrate(self):
		return self.y

class cls_child(cls_parent):
	def __init__(self, x, y, z):
		super().__init__(x, y)
		self.z = z

	def __repr__(self):
		return f"x is {self.x}, y is {self.y}, z is {self.z}"






c_1 = cls_parent(1111, 2222)
print(c_1.demonstrate())

c_2 = cls_child(333,555,999)
print(c_2)