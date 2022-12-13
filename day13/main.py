from functools import cmp_to_key
from more_itertools import flatten

with open("input.txt") as f:
    pairs = [[eval(l) for l in x.split()] for x in f.read().split("\n\n")]

def is_correct_order(l, r):
    if type(l) == int and type(r) == int:
        return l - r
    if type(l) == list and type(r) == list:
        if len(l) == 0 and len(r) == 0: return 0
        if len(l) == 0:                 return -1
        if len(r) == 0:                 return 1
        r1 = is_correct_order(l[0], r[0])
        return r1 if r1 != 0 else is_correct_order(l[1:], r[1:])
    return is_correct_order([l], r) if type(l) == int else is_correct_order(l, [r])

print(sum(i for i, (l, r) in enumerate(pairs, start=1) if is_correct_order(l, r) < 0))

pairs = list(flatten(pairs))
pairs.extend([[[2]],[[6]]])

pairs_sorted = sorted(pairs, key=cmp_to_key(is_correct_order))
i1, i2 = pairs_sorted.index([[2]])+1, pairs_sorted.index([[6]])+1
print(i1*i2)
