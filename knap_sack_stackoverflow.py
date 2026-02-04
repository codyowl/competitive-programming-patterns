from itertools import combinations
import numpy as np



rlen = [2, maxn]
a = []
for r in rlen:
    best_value = sum(vm)
    for i in combinations(np.arange(0, len(vm)), r):
        if sum(np.array(wt)[list(i)]) >= W:
            if sum(np.array(vm)[list(i)]) < best_value:
                best_value = sum(np.array(vm)[list(i)])
                best_indices = list(i)
    a.append([r, best_value, best_indices])

split_inv = min(a, key=lambda t: t[1])[2]
print(split_inv)