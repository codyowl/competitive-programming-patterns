def optimal_indices_for_given_weight(weights, costs, target_weight):
    n = len(weights)

    # Initialize a table to store the minimum cost and corresponding indices
    dp = [(float('inf'), []) for _ in range(target_weight + 1)]

    # Base case: Minimum cost to achieve a weight of 0 is 0
    dp[0] = (0, [])

    # Fill the table using bottom-up dynamic programming
    for i in range(1, n + 1):
        for w in range(weights[i - 1], target_weight + 1):
            new_cost = dp[w - weights[i - 1]][0] + costs[i - 1]
            if new_cost < dp[w][0]:
                dp[w] = (new_cost, dp[w - weights[i - 1]][1] + [i - 1])
    # The final result is the list of indices for the optimal filling
    return dp[target_weight][1]

# Example usage:
weights = [7, 3, 20, 25]
costs = [12, 2, 41, 10]
target_weight = 32

result_indices = optimal_indices_for_given_weight(weights, costs, target_weight)
print("Indices for the optimal filling:", result_indices)

count = 0
for x in result_indices:
    count += costs[x]
    print(costs[x])

print(count)    