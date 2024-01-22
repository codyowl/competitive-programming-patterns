from itertools import combinations
from itertools import product
import itertools

'''
Using Itertools to form combinations with a given array
from itertools import combinations
combinations will form combinations of taking sequential element with remaining elements
pattern = [a,b,c,d,e] => (a,b),(a,c),(a,d),(a,e),(b,c),(b,d),(b,e),(c,d),(c,e),(d,e)

from itertools import product
product will form combinations by taking one element with all the elements 
pattern = [a,b,c] => (a,a,),(a,b),(a,c),(b,a),(b,b),(b,c),(c,a),(c,b),(c,c)
'''

my_chars = ['a', 'b', 'c', 'd', 'e']

combinations = list(combinations(my_chars, 2))
combinations_single = list(product(my_chars,my_chars))


print(combinations)

#removing duplicates
for data in combinations_single:
	if data[0] == data[1]:
		combinations_single.remove(data)

# print(combinations_single)		

'''
Combination of uneven elemetns
'''

x = [1,2,3,4,5]
y = ['a','b','c']

uneven_combination = list(itertools.zip_longest(x,y))
print("un even combinations")
print(x)
print(y)
print(uneven_combination)