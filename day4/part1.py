# Add 2 newlines to 'input' for easier processing
f = open("input", "r")
# f.close()
def check_validity(p):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passscore = 0

    for v in p: 
        x = v.split(":")

        if (x[0] in required):
            passscore += 1
    if (passscore == 7):
        return True

passport = []
valid = 0

for line in f:
    if (line == "\n"):
        if(check_validity(passport) == True):
            valid += 1
        passport = []
        continue
    passport = passport + line.split(" ")
    continue

print("Result = ", valid)

f.close()
