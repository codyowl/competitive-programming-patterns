import itertools

# def knapsack(weight,value):
#   combination_list = list(zip(weight,value))
#   for i in range(1, len(combination_list) + 1):
#       print(i)

from itertools import permutations

def find_closest_sum(numbers, target, n):
	permlist = list(permutations(numbers, n))
	sumlist = [sum(l) for l in permlist]
	maxpos = 0
	for i in range(1, len(sumlist)):
		if abs(sumlist[i] - target) < abs(sumlist[maxpos]-target):
			maxpos = i

	return permlist[maxpos]

value = [12,2,41]
result_shown = find_closest_sum(value, 58, 3)
print(result_shown)

# weight = [7,3,20]
# value = [12,2,41]
# capacity = 58

# knapsack(weight,value)

