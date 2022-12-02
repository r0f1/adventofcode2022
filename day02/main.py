with open("input.txt") as f:
    strat = [(ord(x[0])-ord("A"), ord(x[2])-ord("X")) for x in f]

d1 = {0: [1,2,0], 1: [0,1,2], 2: [2,0,1]}
print(sum(1 + b + 3 * d1[a][b] for a, b in strat))

d2 = {0: [2,0,1], 1: [0,1,2], 2: [1,2,0]}
print(sum(3 * b + 1 + d2[a][b] for a, b in strat))
