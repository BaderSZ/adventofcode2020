from math import floor,ceil

left  = "L"
right = "R"
front = "F"
back  = "B"

matrix = [[False] * 8 for r in range(128)]

class Ticket(object):
    row    = 0
    column = 0
    id     = 0


class Range(object):
    def __init__(self, _range_):
        self.low  =  _range_[0]
        self.high = _range_[1]
    def max(self) -> int:
        return max([self.low, self.high])
    def min(self) -> int:
        return min([self.low, self.high])


f = open("input", "r")

for lines in f:
    line = lines.rsplit()[0]
    ticket = Ticket()

    X = Range([0, 7])
    Y = Range([0, 127])

    for pos in line[:-3]:
        if pos == front:
            Y.high = Y.low + floor((Y.high - Y.low)/2)
        elif pos == back:
            Y.low = Y.low + ceil((Y.high - Y.low)/2)

    if line[6] == front:
        ticket.column = min([Y.low, Y.high])
    elif line[6] == back:
        ticket.column = max([Y.low, Y.high])

    for pos in line[-3:]:
        if pos == left:
            X.high = X.low + floor((X.high - X.low)/2)
        elif pos == right:
            X.low = X.low + ceil((X.high - X.low)/2)
    
    if line[-1:] == right:
        ticket.row = X.max()
    elif line[-1:] == left:
        ticket.row = X.min()

    matrix[ticket.column][ticket.row] = True


b = False

for i in range(128):
    for j in range(8):
        if not matrix[i][j]:
            if 12 < i < 108:
                print("Seat free at y, x = ", i, ", ", j)
                print("My seat ID = ", i * 8 + j)
                b = True
    if b:
        break


f.close()
