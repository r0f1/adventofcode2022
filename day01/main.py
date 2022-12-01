with open("input.txt") as f:
    cals = f.read().rstrip()
elves = [sum(int(c) for c in e.split("\n")) for e in cals.split("\n\n")]
print(max(elves))
print(sum(sorted(elves)[-3:]))
