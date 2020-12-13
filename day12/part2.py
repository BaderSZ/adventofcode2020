from enum import Enum

inp = []


class Direction(Enum):
    north = "N"
    south = "S"
    east = "E"
    west = "W"

class Rotation(Enum):
    left = "L"
    right = "R"

class Move(Enum):
    forward = "F"


class Waypoint(object):
    def __init__(self, pos_north=0, pos_east=0, unit_north=1, unit_east=10):
        self.pos_north = pos_north
        self.pos_east = pos_east
        self.unit_north = unit_north
        self.unit_east = unit_east

    def rotate_facing(self, d: str):
        if d == Rotation.right.value:
            temp = self.unit_east
            self.unit_east = self.unit_north
            self.unit_north = 0 - temp
        elif d == Rotation.left.value:
            temp = self.unit_north
            self.unit_north = self.unit_east
            self.unit_east = 0 - temp

    def rotate_deg(self, direction, degrees):
        times = int(degrees / 90)
        for _ in range(times):
            self.rotate_facing(direction)

    def move_facing(self, distance):
        self.pos_north = self.pos_north + distance*self.unit_north
        self.pos_east = self.pos_east + distance*self.unit_east


    def move_direction(self, direction, distance):
        if direction == Direction.north.value:
            self.unit_north = self.unit_north + distance
        elif direction == Direction.south.value:
            self.unit_north = self.unit_north - distance
        elif direction == Direction.east.value:
            self.unit_east = self.unit_east + distance
        elif direction == Direction.west.value:
            self.unit_east = self.unit_east - distance


with open("input", "r") as f:
    for l in f.readlines():
        inp.append(l.rsplit()[0])


waypoint = Waypoint()

for i in inp:
    P = i[0]
    V = int(i[1:])
    if P in [e.value for e in Direction]:
        waypoint.move_direction(P, V)
    elif P in [e.value for e in Rotation]:
        waypoint.rotate_deg(P, V)
    elif P in [e.value for e in Move]:
        waypoint.move_facing(V)


print("Result = ", abs(waypoint.pos_east) + abs(waypoint.pos_north))

