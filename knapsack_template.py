import itertools

def knapsack(W,weight,value,N):
	table = 
	items = zip(weight, value)
	for itemIndex, (itemWeight, itemValue) in enumerate(items):
		for w in range(W,-1,-1):
			for n in range(N-1,-1,-1):
				if w + itemWeight > W:
					newWeight = W

weight = [1, 3, 4, 5]
value = [10, 40, 50, 70]
W = 8
N = len(value)
print(knapsack(W,weight,value,N))   