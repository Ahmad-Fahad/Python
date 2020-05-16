class Queue:
	def __init__(self, Max_size):
		self.lst       = []
		self.Q_size    = Max_size
		self.Present_Q = 0
		self.front	   = 0
		self.rear	   = 0
	def enqueue(self, data):
		if self.is_full():
			print("Queue is full")
			return
		print("Inserting", data)
		self.lst.insert(self.rear, data)
		self.rear       = (self.rear+1) % self.Q_size
		self.Present_Q += 1
	def dequeue(self):
		if self.is_empty():
			print("Queue is empty")
			return
		data            = self.lst[self.front]
		self.front      = (self.front+1) % self.Q_size
		self.Present_Q -= 1
		return data
	def is_empty(self):
		if self.Present_Q == 0:
			return True
		return False
	def is_full(self): 
		if self.Present_Q == self.Q_size:
			return True
		return False
		
q = Queue(5)
print(q.lst)
print(q.front)
print(q.rear)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q.lst)
print(q.front)
print(q.rear)

q.enqueue(6)
q.enqueue(7)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print(q.lst)
print(q.front)
print(q.rear)