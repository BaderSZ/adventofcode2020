from enum import Enum

with open("input", "r") as f:
    inp = f.readlines()

instructions = []

for i in inp:
    instructions.append(i.rsplit() + [False])

end = len(instructions)

class Com(Enum):
    acc = "acc"
    jmp = "jmp"
    nop = "nop"

def run(p) -> (int, int):
    i = 0
    acc = 0

    while (not p[i][2]) and i < end:

        if p[i][0] == Com.nop.name:
            p[i][2] = True
            i = i + 1
        elif p[i][0] == Com.jmp.name:
            p[i][2] = True
            i = i + int(p[i][1])
        elif p[i][0] == Com.acc.name:
            p[i][2] = True
            acc = acc + int(p[i][1])
            i = i + 1

    return acc, i


print("Result: (acc, i) = ", run(instructions))
