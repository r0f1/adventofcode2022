with open("input.txt") as f:
    lines = f.readlines()
    
idx = 0
for i, l in enumerate(lines):
    if len(l) == 1:
        idx = i
        break

crates = list(zip(*[list(l[1::4]) for l in lines[i-2::-1]]))
crates = [[k for k in c if k != ' '] for c in crates]

moves = [l.split(" from ") for l in lines[idx+1:]]
for a, b in moves:
    idx_s, idx_t = [int(k)-1 for k in b.split(" to ")]
    s, t = crates[idx_s], crates[idx_t]
    r = [s.pop() for _ in range(int(a[5:]))]
    #t.extend(r)      # Part 1
    t.extend(r[::-1]) # Part 2

print("".join(c[-1] for c in crates))
