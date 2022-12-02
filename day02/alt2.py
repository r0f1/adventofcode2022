with open("input.txt") as f:
    strat = [x.strip() for x in f]

l = ["","B X","C Y","A Z","A X","B Y","C Z","C X","A Y","B Z"]
print(sum([l.index(s) for s in strat]))

l = ["","B X","C X","A X","A Y","B Y","C Y","C Z","A Z","B Z"]
print(sum([l.index(s) for s in strat]))
