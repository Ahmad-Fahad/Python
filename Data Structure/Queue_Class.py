class Queue:
	def __init__(self):
		self.lst = list()
	def enqueue(self, item):
		self.lst.append(item)
	def dequeue(self):
		return self.lst.pop(0)
	def is_empty(self):
		if self.lst == []:
			return True
		return False
		
st = Queue()
st.enqueue(1)
st.enqueue(2)
st.enqueue(3)
st.enqueue(4)
st.enqueue(5)

while not st.is_empty():
	print(st.is_empty())
	pp = st.dequeue()
	print(pp)