'''
Given String needs to be check if its palindrome or not
'''

def check_palindrome(mystring):
	'''
	logic is to get both the first and final word of the string and compare it both
	then increment the start and decrement the final word
	'''
	start_index = 0
	end_index = len(mystring) - 1
	while start_index < end_index:
		if mystring[start_index] == mystring[end_index]:
			start_index += 1
			end_index -= 1
			return True
		else:
			return False

# mystring = "hah"
mystring = 'hai'
print(check_palindrome(mystring))	