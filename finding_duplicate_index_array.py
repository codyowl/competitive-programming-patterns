def find_duplicate_index(myarray):
	for x in myarray:
		duplicate_index_list = [index for index, element in enumerate(myarray) if element == x]
	return duplicate_index_list
	


myarray = [0,1,2,2,3,0,4,2]

print(find_duplicate_index(myarray))		 