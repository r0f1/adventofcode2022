with open("input.txt") as f:
    lines = [x.strip().split() for x in f]

root = {".type": "d"}
cwd = None
path = []
for t in lines:
    if t[0] == "$":
        if t[1] == "cd":
            if   t[2] == "/":  cwd = root
            elif t[2] == "..": cwd = path.pop() 
            else:              path.append(cwd); cwd = cwd[t[2]]
    elif t[0] == "dir": cwd[t[1]] = {".type": "d"}
    else:               cwd[t[1]] = {".type": "f", ".size": int(t[0])}

def get_size(n):
    if n[".type"] == "f": return n[".size"]
    return sum(get_size(v) for k, v in n.items() if not k.startswith("."))

def create_size_list(cwd, all_sizes):
    all_sizes.append(get_size(cwd))
    for k, v in cwd.items():
        if not k.startswith(".") and v[".type"] == "d":
            create_size_list(v, all_sizes)

all_sizes = []
create_size_list(root, all_sizes)
print(sum(s for s in all_sizes if s < 100_000))

size_free = 70_000_000 - all_sizes[0]
for d in sorted(all_sizes):
    if size_free + d >= 30_000_000:
        print(d)
        break
