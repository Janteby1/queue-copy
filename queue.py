import sys

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class Queue:
	def __init__(self, head):
		self.head = head

	def enqueque (self, data):
		new = Node(data)
		n = self.head
		while n.next != None:
			n = n.next
		n.next = new
		new.prev = n

	def denqueque (self):
		if self.head.prev == None and self.head.next == None:
			sys.exit()
		self.head = self.head.next		
		self.head.prev = None

	def is_empty (self):
		if self.head.data == None:
			return True
		else:
			return False

	def get_front (self):
		return self.head.data

	def print_queue(self):
		n = self.head
		while n != None:
			print(n.data)
			n = n.next

my_queue = Queue(Node("A"))
my_queue.enqueque("B")
my_queue.enqueque("C")
my_queue.enqueque("D")

my_queue.denqueque()
print (my_queue.is_empty())
print ("Front is: ", my_queue.get_front())

my_queue.print_queue ()


