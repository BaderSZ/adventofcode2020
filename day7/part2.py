char_arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ",", "."]
bag_dict = {}
possible_bags = 0

with open("input", "r") as f:
    inp = f.readlines()


def clean_val(string):
    lst = []
    for elem in string:
        if elem == "no other bags.":
            return [(0, None)]
        else:
            lst = lst + [(int(elem[0]), ''.join(i for i in elem if i not in char_arr)
                            .replace("bags", "")
                            .replace("bag", "")[1:-1])]
    return lst


def make_key(line):
    key = line.split(' bags contain ')[0]
    value_arr = clean_val(line.split(' bags contain ')[1].split(", "))
    return {key: value_arr}

for line in inp:
    bag_dict.update(make_key(line.rstrip()))


def contains_gold(container, bag):
    for _, c in bag_dict.get(container):
        if c == bag or c and contains_gold(c, bag):
            return True
    return False


def count_bags(container):
    total = 1
    for i, c in bag_dict.get(container):
        if c:
            total = total + i * count_bags(c)

    return total


print(count_bags('shiny gold')-1) #-1)
