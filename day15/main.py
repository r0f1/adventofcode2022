import re
from more_itertools import pairwise

cityblock = lambda x1, y1, x2, y2: abs(x1-x2) + abs(y1-y2)

# file_name = "test.txt"
# row_part1 = 10
# xy_bounds = (0, 20)

file_name = "input.txt"
row_part1 = 2_000_000
xy_bounds = (0, 4_000_000)

with open(file_name) as f:
    data = [[int(x) for x in re.findall("-?\d+", l)] for l in f]
    
sensors_beacons = set((sx, sy) for sx, sy, _, _ in data) | set((bx, by) for _, _, bx, by in data)

for row in range(*xy_bounds):
    intervals = []
    for sx, sy, bx, by in data:
        d = cityblock(sx, sy, bx, by) - cityblock(sx, sy, sx, row)
        if d >= 0:
            intervals.append((sx-d, sx+d))

    res = []
    s, e = 0, 0
    for i, ((lb1, ub1), (lb2, ub2)) in enumerate(pairwise(sorted(intervals))):
        if i == 0:
            s, e = lb1, ub1
        if lb2 <= (e+1):
            e = max(e, ub2)
        else:
            res.append((s, e))
            s, e = lb2, ub2
    res.append((s, e))

    if row == row_part1:
        n_beacons_in_row = len(set((bx, by) for _, _, bx, by in data if by == row))
        print(sum([ub-lb+1 for lb, ub in res]) - n_beacons_in_row)

    reduced = [(lb, ub) for lb, ub in res if ub >= xy_bounds[0] and lb <= xy_bounds[1]]
    if len(reduced) == 1:
        continue
    
    x, y = reduced[0][1]+1, row
    if (x, y) not in sensors_beacons:
        print(4_000_000*x+y)
