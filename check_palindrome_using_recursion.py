'''
Given string needs to be checked if its palindrome or not using recursive function
'''
def check_palindrome_recursive(mystring,start_index,end_index):
	if start_index < end_index:
		if mystring[start_index] == mystring[end_index]:
			start_index+=1
			end_index -= 1
			return True
		elif mystring[start_index] != mystring[end_index]:
			return False	
		else:
			return check_palindrome_recursive(mystring,start_index,end_index)

mystring = "saase"
start_index = 0
end_index = len(mystring) - 1

print(check_palindrome_recursive(mystring,start_index,end_index))

