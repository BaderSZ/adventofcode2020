import re
from copy import deepcopy

inp = []

with open("input", "r") as f:
    for line in f.readlines():
        inp = inp + line.rsplit()[0].split(",")

# In form (BUS_ID, index)
busses = [(int(x), i) for i, x in enumerate(inp[1:]) if x != "x"]

# Chinese remainder theorem
time = 0
prod = 1

for id, i in busses:
    while (time + i)%id != 0:
        time = time + prod
    prod = prod * id

print("Result = ", time)