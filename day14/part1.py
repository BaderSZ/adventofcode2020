from typing import List
import re

regex = r"[^[]*\[([^]]*)\]"

def convert_to_binary(n: int) -> List[int]:
    """Converts a base 10 int to list of binary digits"""
    res = [0]*36 # len mask = 37
    b = [int(x) for x in bin(n)[2:]]
    for j, _ in enumerate(b):
        res[-1-j] = b[-1-j]
    return res


def convert_to_base(n: List[int]) -> int:
    """Converts list of binary digits to base 10 int"""
    return int(''.join(str(x) for x in n), 2)


def apply_mask(b: List[int], mask: List[str]) -> List[int]:
    """Loops through and applies mask, returning new binary list"""
    res = b
    for j, m in enumerate(mask):
        if m == "X":
            continue
        elif m == "0":
            res[j] = 0
        elif m == "1":
            res[j] = 1
    return res


with open("test", "r") as f:
    """Create a tuple (mask: str, [vals]: List[int]) for each group. Append to main array inp"""
    cmask = ""
    mem = {}

    for i in f.readlines():
        if i[:4] == "mask":
            cmask = i.rstrip()[7:]
        elif i[:3] == "mem" or "\n":
            masked_binary = apply_mask(convert_to_binary(int(i.partition(" = ")[-1])), cmask)
            mem[re.match(regex, i).groups()[0]] = convert_to_base(masked_binary)

    sum_in_memory = 0

    for key in mem:
        sum_in_memory = sum_in_memory + mem[key]
    print("Sum in memory = ", sum_in_memory)
