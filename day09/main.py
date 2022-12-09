with open("input.txt") as f:
    instructions = [x.split() for x in f]

# n_knots = 2 # Part 1
n_knots = 10  # Part 2
pos_h = (0,0)
pos_ts     = [(0,0)   for _ in range(n_knots-1)]
history_ts = [{(0,0)} for _ in range(n_knots-1)]

sign = lambda x: (1, -1)[x < 0]

for k, t in instructions:
    d = {"R": (1,0), "L": (-1,0), "U": (0,1), "D": (0,-1)}[k]
    for _ in range(int(t)):
        pos_h = pos_h[0]+d[0], pos_h[1]+d[1]
        pos_pred = pos_h
        for i, history_t in enumerate(history_ts):
            x, y = pos_ts[i][0], pos_ts[i][1]
            dx, dy = x-pos_pred[0], y-pos_pred[1]
            
            if (abs(dx) > 0 and abs(dy) > 1) or (abs(dx) > 1 and abs(dy) > 0):
                pos_ts[i] = x-sign(dx), y-sign(dy)
            elif abs(dx) > 1:
                pos_ts[i] = x-sign(dx), y
            elif abs(dy) > 1:
                pos_ts[i] = x, y-sign(dy)
    
            pos_pred = pos_ts[i]
            history_t.add(pos_ts[i])

print(len(history_ts[-1]))
