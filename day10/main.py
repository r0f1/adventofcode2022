instructions = open("input.txt").readlines()

x = 1
c = 0
hist = [x]
output = ""

pix = lambda c, x: "#" if abs(c - x) <= 1 else "."

for instr in instructions:
    output += pix(c, x)
    c = (c + 1) % 40
    if instr.startswith("addx"):
        output += pix(c, x)
        c = (c + 1) % 40
        hist.append(x)
        x += int(instr.split()[1])
    hist.append(x)

print(sum(i*hist[i-1] for i in range(20, 221, 40)))
for row in range(0, 6):
    print(output[row*40:(row+1)*40])
