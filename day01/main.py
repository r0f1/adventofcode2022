with open("input.txt") as f:
    cals = f.read().strip()
elves = sorted([sum(int(c) for c in e.split("\n")) for e in cals.split("\n\n")])
print(elves[-1])
print(sum(elves[-3:]))
