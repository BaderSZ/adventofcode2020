char_arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ",", "."]
bag_dict = {}
possible_bags = 0
total = 0


def clean_val(string):
    lst = []
    for elem in string:
        if elem == "no other bags.":
            return [(0, None)]
        lst = lst + [(int(elem[0]), ''.join(i for i in elem if i not in char_arr)
                        .replace("bags", "")
                        .replace("bag", "")[1:-1])]
    return lst


def make_key(line):
    key = line.split(' bags contain ')[0]
    value_arr = clean_val(line.split(' bags contain ')[1].split(", "))
    return {key: value_arr}



def contains_gold(container, bag):
    for _, c in bag_dict.get(container):
        if c == bag or c and contains_gold(c, bag):
            return True
    return False


with open("input","r") as f:
    inp = f.readlines()

for line in inp:
    bag_dict.update(make_key(line.rstrip()))

for i in bag_dict.keys():
    if contains_gold(i, "shiny gold"):
        total = total + 1

print("Result =", total)
