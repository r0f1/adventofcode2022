with open("input.txt") as f:
    strat = [(ord(x[0])-ord("A"), ord(x[2])-ord("X")) for x in f]
print(sum(1 + b + (b-a+1)%3 * 3 for a, b in strat))
print(sum(1 + 3 * b + (b+a-1)%3 for a, b in strat))
