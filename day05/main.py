with open("input.txt") as f:
    lines_top, lines_bottom = [l.split("\n")[:-1] for l in f.read().split("\n\n")]

crates = zip(*[list(l[1::4]) for l in lines_top[::-1]])
crates = [[k for k in c if k != ' '] for c in crates]

for l in lines_bottom:
    a, b = l.split(" from ")
    s, t = [int(k)-1 for k in b.split(" to ")]
    r = [crates[s].pop() for _ in range(int(a[5:]))]
    #crates[t].extend(r)      # Part 1
    crates[t].extend(r[::-1]) # Part 2

print("".join(c[-1] for c in crates))
