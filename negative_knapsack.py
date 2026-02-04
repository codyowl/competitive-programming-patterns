def knapSack(W, wt, val, n):
	'''
	 :param W: capacity of knapsack 
	 :param wt: list containing weights
	 :param val: list containing corresponding values
	 :param n: size of lists
	 :return: Integer
	'''
	# code here
	dp_table = [[0 for j in range(W+1)]for i in range(len(wt)+1)]
	for i in range(1,len(dp_table)):
		for j in range(1, len(dp_table[0])):
			 if wt[i-1] <= j:
				 dp_table[i][j] = max(val[i-1]+dp_table[i-1][j-wt[i-1]],dp_table[i-1][j])
			 elif wt[i-1] > j:
				 dp_table[i][j] = dp_table[i-1][j]
	print(dp_table)
	return dp_table[-1][-1]
	# print(wt)

weight = [1, 3, 4, 5]
value = [10, 40, 50, 70]
W = 8
N = len(value)
print(knapSack(W, weight, value, N))