import re
from copy import deepcopy

inp = []

with open("input", "r") as f:
    for line in f.readlines():
        inp = inp + line.rsplit()

timestamp = int(inp[0])
busses = [int(x) for x in re.split(",|x", inp[1]) if x != '']

nextbusses = deepcopy(busses)

for i, t in enumerate(busses):
    nextbusses[i] = timestamp+(t - timestamp%t)

nextbus = min(nextbusses)

print("Result = ", (nextbus - timestamp)*busses[nextbusses.index(nextbus)])
