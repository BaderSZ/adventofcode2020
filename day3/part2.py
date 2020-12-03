import numpy

with open('input') as f:
    data = f.read()

inp = data.splitlines()


def variations(right, down):
    trees = 0
    i = 0
    for line in inp[::down]:
        if line[(i * right) % len(line)] == '#':
            trees = trees + 1
        i = i + 1
    return trees


arr = [variations(3,1),variations(1,1),variations(5,1),variations(7,1),variations(1,2)]
print("Result = ", numpy.product(arr))

