from enum import Enum

class Categories(Enum):
    byr = 'byr'
    iyr = 'iyr'
    eyr = 'eyr'
    hgt = 'hgt'
    hcl = 'hcl'
    ecl = 'ecl'
    pid = 'pid' 

# Add 2 newlines to 'input' for easier processing

with open("input", "r") as f:
    inp = f.readlines()

def check_validity(p):
    passscore = 0

    for v in p: 
        x = v.split(":")
        if (x[0] in [v.value for v in Categories.__members__.values()]):
            passscore += 1

    if (passscore == 7):
        return True

passport = []
valid = 0

for line in inp:
    if (line == "\n"):
        if(check_validity(passport) == True):
            valid += 1
        passport = []
        continue
    passport = passport + line.split(" ")
    continue

print("Result = ", valid)

