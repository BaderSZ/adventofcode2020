from typing import List
import numpy as np

inp = []
ls = []
delta = ((-1, -1), (-1, 0), (-1, 1),
         (0, -1), (0, 1),
         (1, -1), (1, 0), (1, 1))

with open("input", "r") as f:
    for l in f.readlines():
        inp.append(list(l.rsplit()[0]))

len_x = len(inp[0])
len_y = len(inp)


def first_run(matr: List[List[str]]) -> List[List[str]]:
    m = np.copy(matr)
    for i in range(0, len_y):
        for j in range(0, len_x):
            if matr[i][j] == "L":
                m[i][j] = "#"
    return m


def total_occupied(matr: List[List[str]]) -> int:
    total = 0
    for i in range(0, len_y):
        for j in range(0, len_x):
            if matr[i][j] == "#":
                total = total + 1
    return total


def neighbours(matr: List[List[str]], x: int, y: int) -> int:
    n = 0
    for dx, dy in delta:
        if 0 <= x + dx < len_x and 0 <= y + dy < len_y:
            if matr[y+dy][x+dx] == "#":
                n = n+1
    return n


def do_seats(matr: List[List[str]]) -> (List[List[str]], bool):
    m = np.copy(matr)
    changed = False
    for i in range(0, len_y):
        for j in range(0, len_x):
            n = neighbours(matr, j, i)
            if matr[i][j] == "#" and  n >= 4:
                m[i][j] = "L"
                changed = True
            elif matr[i][j] == "L" and n == 0:
                m[i][j] = "#"
                changed = True
    return m, changed


inp = first_run(inp)

d = True
while d:
    inp, d = do_seats(inp)

print("Result = ", total_occupied(inp))
