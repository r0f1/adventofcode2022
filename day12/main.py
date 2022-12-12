from networkx import grid_2d_graph
from networkx import shortest_path

with open("input.txt") as f:
    grid = [list(x.strip()) for x in f]

source = None
all_sources = []
target = None
for row_n, row in enumerate(grid):
    for col_n, c in enumerate(row):
        if c == "S":
            source = (row_n, col_n)
            grid[row_n][col_n] = "a"
        if c == "E":
            target = (row_n, col_n)
            grid[row_n][col_n] = "z"
        if grid[row_n][col_n] == "a":
            all_sources.append((row_n, col_n))

g = grid_2d_graph(len(grid), len(grid[0]))

grid = [[ord(c)-ord("a") for c in row] for row in grid]
def weight_func(a, b, edge_dict):
    if grid[a[0]][a[1]] < grid[b[0]][b[1]] - 1:
        return None
    return 1

print(len(shortest_path(g, source, target, weight_func))-1)

paths = []
for s in all_sources:
    try:
        paths.append(len(shortest_path(g, s, target, weight_func))-1)
    except:
        pass
print(min(paths))
