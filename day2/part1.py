f = open("input","r")

res = 0

for line in f:
    arr = line.split(" ")

    rang = arr[0].split("-")
    r1   = int(rang[0])
    r2   = int(rang[1])

    key    = arr[1].split(":")[0]
    string = arr[2]

    o = 0
    for i in range(0,len(string)):
        if string[i] == key:
            o = o+1

    if (o >=r1 and o <= r2):
        res = res+ 1   

print("Result: ", res)

f.close()
