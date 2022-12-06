with open("input.txt") as f:
    lines = [[*map(int, x.replace("-", ",").split(","))] for x in f]

print(sum(a <= c <= d <= b or c <= a <= b <= d for a, b, c, d in lines))
print(sum(a <= d and b >= c for a, b, c, d in lines))
