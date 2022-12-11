from functools import partial
from math import prod
from operator import add, mul

from more_itertools import chunked

stub = lambda a, b, op: {"+": add, "*": mul}[op](a, b)

with open("input.txt") as f:
    descs = list(chunked([x.strip() for x in f], 7))

monkeys = []
for desc in descs:
    m = {"items": [int(i) for i in desc[1].split(":")[1].split(",")],
         "test": int(desc[3].split()[-1]),
         True:   int(desc[4].split()[-1]),
         False:  int(desc[5].split()[-1]),
         "count": 0}
    chunks = desc[2].split("=")[1].strip()
    if chunks == "old * old":
        m["func"] = lambda x: x*x
    else:
        _, op, var2 = chunks.split()
        m["func"] = partial(stub, b=int(var2), op=op)
    monkeys.append(m)

z = prod(m["test"] for m in monkeys)

for k in range(10_000): # replace with 20 for Part 1
    for m in monkeys:
        while len(m["items"]) > 0:
            m["count"] += 1
            i = m["func"](m["items"].pop(0))
            # i //= 3 # Part 1
            i %= z    # Part 2
            monkeys[m[i % m["test"] == 0]]["items"].append(i)

print(prod(sorted([m["count"] for m in monkeys])[-2:]))
