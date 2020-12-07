with open("input","r") as f:
    inp = f.readlines()

res = 0

for line in inp:
    arr = line.split(" ")

    rang = arr[0].split("-")
    r1   = int(rang[0])
    r2   = int(rang[1])

    key    = arr[1].split(":")[0]
    string = arr[2]

    if ((string[r1-1] == key) ^ (string[r2-1] == key)):
        res = res + 1

print("Results: ", res)

f.close()
