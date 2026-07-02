class Linkedlist:
	def __init__(self, value, next):
		self.value = value
		self.next = next 

node1 = Linkedlist(1)
node2 = Linkedlist(2)
node3 = Linkedlist(4)

node1.next = node2
node2.next = node3 

head_node = node1
current_node = head_node		