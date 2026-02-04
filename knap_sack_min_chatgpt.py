def min_cost_knapsack(weights, costs, target_weight):
    n = len(weights)
    
    # Initialize a table to store the minimum cost for each subproblem
    dp = [[float('inf')] * (target_weight + 1) for _ in range(n + 1)]

    # Base case: Minimum cost to achieve a weight of 0 is 0 for any number of items
    for i in range(n + 1):
        dp[i][0] = 0

    # Fill the table using bottom-up dynamic programming
    for i in range(1, n + 1):
        for w in range(1, target_weight + 1):
            # If the current item can fit in the knapsack
            if weights[i - 1] <= w:
                # Choose whether to include the current item or not
                dp[i][w] = min(dp[i - 1][w], dp[i][w - weights[i - 1]] + costs[i - 1])
            else:
                # If the current item cannot fit, copy the result from the previous row
                dp[i][w] = dp[i - 1][w]

    # The final result is stored in the bottom-right cell of the table
    return dp[n][target_weight]

# Example usage:
# weights = [2, 3, 4, 5]
# costs = [3, 4, 5, 6]
# target_weight = 5
costs = [60, 100, 120, 50, 10, 10]  # Values
weights = [10, 20, 30, 20, 5, 5]  # Weights
target_weight = 50

result = min_cost_knapsack(weights, costs, target_weight)
print("Minimum cost for the given weight:", result)
