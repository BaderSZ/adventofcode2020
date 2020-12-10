
with open("input", "r") as f:
    inp = list(map(int, f.read().rsplit()))
    inp.sort()

def massive_num(inp):
    res = [1]+ [0]*inp[-1]
    for i in inp[:]:
        res[i] = res[i-3] + res[i-2] + res[i-1]
    return res[-1]

# Result =  518344341716992
print("Result = ", massive_num(inp))
