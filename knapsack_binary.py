def UnboundedKnapsack(Capacity, n, weight, val):
    dp = [float('inf')] * (Capacity + 1)
    selected_indices = [[] for _ in range(Capacity + 1)]

    weight = [-x for x in weight]

    for i in range(0, Capacity + 1):
        for j in range(0, n):
            if weight[j] <= i:
                if dp[i - weight[j]] != float('inf') and dp[i - weight[j]] + val[j] < dp[i]:
                    dp[i] = dp[i - weight[j]] + val[j]
                    selected_indices[i] = selected_indices[i - weight[j]] + [j]

    return dp[Capacity], selected_indices[Capacity]

# Example usage:
Capacity = 58
n = 3
weight = [7, 3, 20]
val = [12, 2, 41]

min_value, indices = UnboundedKnapsack(Capacity, n, weight, val)
print("Minimum value:", min_value)
print("Indices of costs for optimal filling:", indices)
