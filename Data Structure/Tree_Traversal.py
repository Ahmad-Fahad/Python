class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data  = data
		self.left  = left
		self.right = right

		def __repr__(self):
			return repr(self.data)
			
	def add_left(self, node):
		self.left = node
	def add_right(self, node):
		self.right = node
	def create_Tree(self):
		n_2 = Node(2)
		n_7 = Node(7)
		n_9 = Node(9)
		n_2.add_left(n_7)
		n_2.add_right(n_9)
		n_1 = Node(1)
		n_6 = Node(6)
		n_7.add_left(n_1)
		n_7.add_right(n_6)
		n_5  = Node(5)
		n_10 = Node(10)
		n_6.add_left(n_5)
		n_6.add_right(n_10)
		n_8 = Node(8)
		n_9.add_right(n_8)
		n_3 = Node(3)
		n_4 = Node(4)
		n_8.add_left(n_3)
		n_8.add_right(n_4)
		return n_2

if __name__ == "__main__":
	root = create_Tree()
	print(root)

