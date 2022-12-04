with open("input.txt") as f:
    lines = [[[int(i) for i in k.split("-")] for k in x.split(",")] for x in f]

print(sum(a <= c <= d <= b or c <= a <= b <= d for (a,b), (c,d) in lines))
print(sum(any([a <= c <= b, a <= d <= b, c <= a <= d, c <= b <= d]) for (a,b), (c,d) in lines))

# Alternative for Part 2
print(sum([max(a,c) <= min(b,d) for (a,b), (c,d) in lines]))
