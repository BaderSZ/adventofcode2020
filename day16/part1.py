def split_range(arr):
    return [[int(x) for x in arr[0].split("-")], [int(x) for x in arr[2].split("-")]]

def in_range(x, arr):
    for r in arr:
        if x in range(r[0], r[1]+1):
            return True
    return False

testranges = []
nearbytickets = []
error = 0

with open("input", "r") as f:
    for i, line in enumerate(f.readlines()):
        if i < 20:
            testranges = testranges + split_range([x.rsplit() for x in line.split(":")][1])
        if i >= 25:
            nearbytickets = nearbytickets + [int(x) for x in line.rsplit()[0].split(",")]

for t in nearbytickets:
    if not in_range(t, testranges):
        error = error + t

print("Result = ", error)
