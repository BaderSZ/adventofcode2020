from enum import Enum

class Com(Enum):
    acc = "acc"
    jmp = "jmp"
    nop = "nop"

def run(p):
    i = 0
    acc = 0

    while not p[i][2] and i < len(p):

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


with open("input", "r") as f:
    inp = f.readlines()

instructions = []

for i in inp:
    instructions.append(i.rsplit() + [False])

end = len(instructions)

def check_mod(p):
    for i, inst in enumerate(p):
        inst[0] = inst[0].replace("jmp", "nop")
        acc, v = run(p[:i]+ [inst] + p[i+1:])
        if v >= end:
            return acc,v        

# acc = 703
print("Result: acc,v = ", check_mod(instructions))