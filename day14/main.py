import numpy as np
from more_itertools import flatten
from more_itertools import pairwise
from PIL import Image, ImageOps
from skimage.draw import line as draw_line

with open("input.txt") as f:
    lines = [[[int(c) for c in k.split(",")] for k in l.split(" -> ")] for l in f]

min_x, min_y = min([x for x, _ in flatten(lines)]+[500]), min([y for _, y in flatten(lines)]+[0])
max_x, max_y = max([x for x, _ in flatten(lines)]+[500]), max([y for _, y in flatten(lines)]+[0])

dim_x, dim_y = (max_x - min_x)+1, (max_y - min_y)+3

grid = np.zeros((dim_y, dim_x), dtype="uint8")
for line in lines:
    for a, b in pairwise(line):
        rr, cc = draw_line(a[1]-min_y, a[0]-min_x, b[1]-min_y, b[0]-min_x)
        grid[rr, cc] = 1

add_border = 300
grid = np.array(ImageOps.expand(Image.fromarray(grid), border=(add_border,0,add_border,0), fill=0))
rr, cc = draw_line(dim_y-1, 0, dim_y-1, dim_x-1+add_border*2)
grid[rr, cc] = 1

offset_x, offset_y = add_border, 0

generate_new_sand = True
init_pos_y, init_pos_x = 0-min_y+offset_y, 500-min_x+offset_x
try:
    while True:
        if generate_new_sand:
            if grid[init_pos_y, init_pos_x] == 3:
                break
            grid[init_pos_y, init_pos_x] = 2
            pos_y, pos_x = init_pos_y, init_pos_x
            generate_new_sand = False
        else:
            pos_y, pos_x = new_pos_y, new_pos_x

        for new_pos_y, new_pos_x in [(pos_y+1, pos_x), (pos_y+1, pos_x-1), (pos_y+1, pos_x+1)]:
            # if new_pos_x == -1:
            #     raise Exception()
            if grid[new_pos_y, new_pos_x] == 0:
                grid[pos_y, pos_x] = 0
                grid[new_pos_y, new_pos_x] = 2
                break
        else:
            grid[pos_y, pos_x] = 3
            generate_new_sand = True
except:
    pass

print(np.sum([grid == 3]))
