# see: https://docs.python.org/3/library/functions.html#eval

import re

def parse_into(line):
    while ("+" in line) or ("*" in line):
        e = re.findall(r"^(\d+ [\*\+] \d+)", line)[0]
        line = str(eval(e)) + line[len(e):]
    return int(line)


def parse(line):
    while line.count("("):
        eval = re.findall(r"\(\d+ [\*\+] [\d+|\d+ \[\*\+\] \d+]+\)", line)
        for e in eval:
            line = line.replace(e, str(parse_into(e[1:-1])))
    return parse_into(line)


sum = 0

with open("input", "r") as f:
    for l in f.readlines():
        sum = sum + parse(l)

print("Result = ", sum)
