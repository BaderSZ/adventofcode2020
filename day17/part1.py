## hello O(n^5)
## 3D game of life

from collections import defaultdict


def first_run(inp):
    matr = []
    for i, line in enumerate(inp):
        for j, pos in enumerate(line):
            if pos == "#":
                 matr.append((i, j, 0))
    return matr


def next(matr):
    m = defaultdict(int)
    res = []

    for x, y, z in matr:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    if (dx, dy, dz) == (0, 0, 0):
                        continue
                    m[(x + dx, y + dy, z + dz)] += 1

    for pos, neighbours in m.items():
        if neighbours == 3 or (neighbours == 2 and pos in matr):
            res.append(pos)
    return res


inp = []

with open("input", "r") as f:
    for line in f.readlines():
        inp.append(line.rsplit()[0])

res = first_run(inp)
for _ in range(0, 6):
    res = next(res)

print("Result = ", len(res))
