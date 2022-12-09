from functools import reduce
import numpy as np

with open("input.txt") as f:
    orig_grid = np.array([[int(c) for c in x.strip()] for x in f])
orig_mask = np.zeros_like(orig_grid)
dists = [np.zeros_like(orig_grid) for _ in range(4)]

for k, dist in enumerate(dists):
    grid, mask = np.rot90(orig_grid, k=k), np.rot90(orig_mask, k=k)
    for row, (g, m, d) in enumerate(zip(grid, mask, dist)):
        curr = 0
        for col, h in enumerate(g):
            if col == 0 or h > curr:
                m[col] = 1
                curr = h
            curr_height = h
            counter = 0
            for i in g[col+1:]:
                counter += 1
                if i >= curr_height:
                    break
            d[col] = counter

print(np.sum(mask))

dists = [np.rot90(d, k=-k) for k, d in enumerate(dists)]
print(np.max(reduce(np.multiply, dists)))
