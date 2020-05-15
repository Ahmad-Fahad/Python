class Queue:
	def __init__(self):
		self.lst   = []
		self.front = 0
		self.rear  = 0
	def enqueue(self, item):
		self.lst.insert(self.rear, item)
		self.rear += 1
	def dequeue(self):
		item = self.lst[self.front]
		self.front += 1
		return item
	def is_empty(self):
		if self.front == self.rear:
			return True
		return False
		
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

while not q.is_empty():
	print(q.is_empty())
	qq = q.dequeue()
	print(qq)