# hugues_hoppe on Reddit
from itertools import accumulate

with open("input.txt") as f:
    lines = [x.strip() for x in f]

stack = []
sizes = []
for line in lines:
    t = line.split()
    if line == "$ cd ..":
        s = stack.pop()
        sizes.append(s)
        stack[-1] += s
    elif line.startswith("$ cd "):
        stack.append(0)
    elif t[0].isdigit():
        stack[-1] += int(t[0])
sizes.extend(accumulate(stack[::-1]))

print(sum(s for s in sizes if s <= 100_000))
print(min(s for s in sizes if s >= sizes[-1] - 40_000_000))
