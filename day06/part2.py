f = open("input","r")

sum = 0

for group in f.read().split("\n\n"):
    sum = sum + len(set.intersection(
        *map(set, group.rsplit("\n"))))

print("Result = ", sum)

f.close()