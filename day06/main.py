from more_itertools import windowed

with open("input.txt") as f:
    line = f.read().strip()

for p in [4, 14]:
    for i, t in enumerate(windowed(line, p)):
        if p == len(set(t)):
            print(p+i)
            break
