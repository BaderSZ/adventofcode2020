inp = [9, 6, 0, 10, 18, 2, 1]
d = {}
end = inp[-1]

for i, val in enumerate(inp):
    d[val] = [i+1]

i = len(inp) + 1

while i < 30000001:
    if end not in d:
        d[end] = [i-1]
        end = 0
        if i == 2020:
            print(end)
        elif i == 30000000:
            print(end)
            break
    else:
        d[end].append(i-1)
        end = d[end][-1] - d[end][-2]
        if i == 2020:
            print(end)
        elif i == 30000000:
            print(end)
            break
    i = i + 1
