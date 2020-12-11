with open('input') as f:
    data = f.read()

inp = data.splitlines()


def variations(right, down):
    trees = 0
    i = 0
    for line in inp:
        if line[(i * right) % len(line)] == '#':
            trees = trees + 1
        i = i + 1
    return trees


print("Result = ", variations(3,1))

