# From travisdoesmath on Reddit
with open("input.txt") as f:
    signal = f.read().strip()
print([[i for i in range(n, len(signal)) if len(set(signal[i-n:i])) == n][0] for n in [4, 14]])
