from string import ascii_letters
from more_itertools import chunked

with open("input.txt") as f:
    lines = [x.strip() for x in f]

prios = {c: i+1 for i, c in enumerate(ascii_letters)}
print(sum(prios[(set(l[:len(l)//2]) & set(l[len(l)//2:])).pop()] for l in lines))
print(sum(prios[(set(l1) & set(l2) & set(l3)).pop()] for l1, l2, l3 in chunked(lines, 3)))
