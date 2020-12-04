import re
from enum import Enum

class Categories(Enum):
    byr = 'byr'
    iyr = 'iyr'
    eyr = 'eyr'
    hgt = 'hgt'
    hcl = 'hcl'
    ecl = 'ecl'
    pid = 'pid' 

eye_colors = ["brn","amb","grn","blu","hzl","gry","oth"]
# Add 2 newlines to 'input' for easier processing

f = open("input", "r")

def check_data_validity(key, var):
    if ((key == Categories.byr.value) and (1920 <= int(var) <= 2002)):
        return True

    if ((key == Categories.iyr.value) and (2010 <= int(var) <= 2020)):
        return True

    if ((key == Categories.eyr.value) and (2020 <= int(var) <= 2030)):
        return True

    if (key == Categories.hgt.value):
        if ((var[-2:] == "cm") and (150 <= int(var[:-2]) <= 193)):
            return True
        if ((var[-2:] == "in") and (59 <= int(var[:-2]) <= 76)):
            return True

    if (key == Categories.hcl.value):
        return (re.search(r'^#[0-9a-f]{6}$', var))

    if ((key == Categories.ecl.value) and (var in eye_colors)):
        return True

    if (key == Categories.pid.value):
        return(re.match('^[0-9]{9}$', var))
    
    return False

def check_pass_validity(p):
    passscore = 0

    for v in p: 
        x = v.split(":")

        if ((x[0] in [v.value for v in Categories.__members__.values()]) and (check_data_validity(x[0],x[1].rstrip()))):
            passscore += 1
    if (passscore == 7):
        return True

passport = []
valid = 0

for line in f:
    if (line == "\n"):
        if(check_pass_validity(passport) == True):
            valid += 1
        passport = []
        continue
    passport = passport + line.split(" ")
    continue

print("Result = ", valid)

f.close()
