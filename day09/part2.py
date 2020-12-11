from itertools import combinations

with open("input", "r") as f:
    inp = list((map(int, f.read().rsplit())))


def sum_array(inp, i, r):
    return [i+j for i, j in combinations(inp[i-25 : i], r)]


def first_invalid(inp):
    for i in range(25, len(inp)):
        if inp[i] not in sum_array(inp, i, 2):
            return inp[i]


def sum_min_max(arr, n):
    for j in range(2, len(inp)):
        for i in range(0, len(arr)-j+1):
            arr[i] += inp[i+j-1]
            if arr[i] == n:
                res = inp[i : i+j]
                return min(res) + max(res)


# Result = 2466556
print("Result = ", sum_min_max(inp[:], first_invalid(inp)))
