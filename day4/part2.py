import re
# Add 2 newlines to 'input' for easier processing
f = open("input", "r")

def check_data_validity(key, var):
    if (key == "byr"):
        if ( 1920 <= int(var) <= 2002):
            return True

    if (key == "iyr"):
        if (2010 <= int(var) <= 2020):
            return True

    if (key == "eyr"):
        if(2020 <= int(var) <= 2030):
            return True

    if (key == "hgt"):
        if (var[-2:] == "cm"):
            if (150 <= int(var[:-2]) <= 193):
                return True

        if (var[-2:] == "in"):
            if (59 <= int(var[:-2]) <= 76):
                return True

    if (key == "hcl"):
        return (re.search(r'^#[0-9a-f]{6}$', var))

    if (key == "ecl"):
        if (var in ["brn","amb","grn","blu","hzl","gry","oth"]):
            return True
    if (key == "pid"):
        return(re.match('^[0-9]{9}$', var))
    
    return False

def check_pass_validity(p):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passscore = 0

    for v in p: 
        x = v.split(":")

        if ((x[0] in required) and (check_data_validity(x[0],x[1].rstrip()))):
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
