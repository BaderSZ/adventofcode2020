with open("input", "r") as f:
    inp = list(map(int, f.read().rsplit()))
    inp.sort()

def diff_product(inp):
    diff_one = 0
    diff_three = 1
    eff_jolt = 0


    for _ in range(len(inp)):
        x = min(inp)
        d = x - eff_jolt
        eff_jolt = x
        if d == 1:
            diff_one = diff_one + 1
        elif d == 3:
            diff_three = diff_three + 1
        inp.remove(x)
    
    return diff_one * diff_three

# Result =  2775
print("Result = ", diff_product(inp))
