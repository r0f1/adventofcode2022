from functools import cmp_to_key
from more_itertools import flatten

with open("input.txt") as f:
    pairs = [[eval(l) for l in x.split()] for x in f.read().split("\n\n")]

def is_correct_order(l, r):
    if type(l) == type(r):
        if type(l) == int and type(r) == int:
            return "Unsure" if l == r else str(l < r)
        else:
            if len(l) == 0 and len(r) == 0: return "Unsure"
            if len(l) == 0:                 return "True"
            if len(r) == 0:                 return "False"
            r1 = is_correct_order(l[0], r[0])
            return r1 if r1 != "Unsure" else is_correct_order(l[1:], r[1:])

    return is_correct_order([l], r) if type(l) == int else is_correct_order(l, [r])

print(sum(i for i, (l, r) in enumerate(pairs, start=1) if is_correct_order(l, r) == "True"))

pairs = list(flatten(pairs))
pairs.extend([[[2]],[[6]]])

def compare(a, b):
    return {"True": -1, "Unsure": 0, "False": 1}[is_correct_order(a, b)]

pairs_sorted = sorted(pairs, key=cmp_to_key(compare))
i1, i2 = pairs_sorted.index([[2]])+1, pairs_sorted.index([[6]])+1
print(i1*i2)
