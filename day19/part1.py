## Chomsky Normal Form grammar
## At least I learned something from school :D

import re

grammar = {}
with open("rules", "r") as f:
    for rule in f.readlines():
        n, r = rule.rstrip().split(": ")
        grammar[n] = r

with open("words", "r") as f:
    words = [word.rsplit()[0] for word in f.readlines()]

g = {}
while "0" not in g.keys():
    for n, arr in grammar.items():
        if  "\"" in arr:
            g[n] = arr.strip("\"")
        else:
            parts = arr.split(" ")
            c = True
            for i in parts:
                if i == "|":
                    continue
                if i not in g.keys():
                    c = False

            r = ""

            if c:
                for i in parts:
                    if i == "|":
                        r += i
                    else:
                        r = r + g[i]

                g[n] = "(" + r + ")"


print("Result = ", sum([1 for word in words if re.fullmatch(g["0"], word)]))
