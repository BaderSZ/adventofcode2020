from itertools import combinations

with open("input", "r") as f:
    inp = list((map(int, f.read().rsplit())))


def sum_array(inp, i):
    return [i+j for i, j in combinations(inp[i-25 : i], 2)]


def first_invalid(inp):
    for i in range(25, len(inp)):
        if inp[i] not in sum_array(inp, i):
            return inp[i]


# Result = 15353384
print("Result = ", first_invalid(inp))

