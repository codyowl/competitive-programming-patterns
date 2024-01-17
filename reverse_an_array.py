'''
Given an array needs to be reversed
'''
def reverse_an_array(myarray):
	'''
	The logic is to replace first element with last element and ascend from there 
	replace second element with the element before last
	need to save the value in a temp variable and do the swapping
	'''
	start_index = 0
	end_index = len(myarray) - 1
	while start_index <= end_index:
		temp = myarray[start_index]
		myarray[start_index] = myarray[end_index]
		myarray[end_index] = temp
		start_index += 1
		end_index -= 1
	return myarray
	
myarray = [45,55,20,78]	
print(reverse_an_array(myarray))		