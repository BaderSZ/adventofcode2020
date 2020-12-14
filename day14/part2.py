from typing import List
import re
from copy import deepcopy

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

possibilities = []

def apply_mask(b: List[int], mask: List[str]) -> List[str]:
    """Loops through and applies mask, returning new binary list"""
    res = deepcopy(b)
    possibilities = [res]*mask.count("X")
    print(possibilities)
    for j, m in enumerate(mask):
        if m == "X":
            for i, arr in enumerate(possibilities):
                if i == 0 or i%2==0:
                    arr[j] = 0
                    possibilities[i] = arr
                else:
                    arr[j] = 1
                    possibilities[i] = arr
        elif m == "0":
            continue
        elif m == "1":
            res[j] = 1
    return res


with open("test", "r") as f:
    """Create a dict (mask: str, [vals]: List[int]) for each group."""
    cmask = ""
    mem = {}
    instance = {}

    for i in f.readlines():
        if i[:4] == "mask":
            cmask = i.rstrip()[7:]
        elif i[:3] == "mem" or "\n":
            masked_binary = apply_mask(convert_to_binary(int(i.partition(" = ")[-1])), cmask)


    # Result = 4574598714592
    print("Sum in memory = ", sum(possibilities))
