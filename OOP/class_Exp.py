class cls:
	x = 7
	def __init__(self_alter_obj, r):
		self_alter_obj.x = r


obj = cls(4)
print(obj.x)

