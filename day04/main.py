with open("input.txt") as f:
    lines = [[[int(i) for i in k.split("-")] for k in x.split(",")] for x in f]

print(sum((a <= c <= b and a <= d <= b) or (c <= a <= d and c <= b <= d) for (a,b), (c,d) in lines))
print(sum(any([a <= c <= b, a <= d <= b, c <= a <= d, c <= b <= d])      for (a,b), (c,d) in lines))
