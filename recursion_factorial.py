'''
Using recursion to find factorial of a number
factorial of 3 = 3 * 2 * 1 => 6
'''

def recursive_factorial(x):
	if x < 1:
		return 1
	else:
		return (x * recursive_factorial(x-1))

# x = 3
x = 7
# factotial of 7 => 7*6*5*4*3*2*1 = 5040
print(recursive_factorial(x))
