def traverse_single_linked_list(list):
	current = head 
	while current:
		print(current.val)
		# traversing 
		current = current.next