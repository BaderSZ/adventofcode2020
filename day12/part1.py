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


class Boat(object):
    def __init__(self, facing=Direction.east.value, pos_north=0, pos_east=0):
        self.facing = facing
        self.pos_north = pos_north
        self.pos_east = pos_east

    def rotate_facing(self, d: str):
        if d == Rotation.right.value:
            if self.facing == Direction.north.value:
                self.facing = Direction.east.value
            elif self.facing == Direction.east.value:
                self.facing = Direction.south.value
            elif self.facing == Direction.south.value:
                self.facing = Direction.west.value
            elif self.facing == Direction.west.value:
                self.facing = Direction.north.value
        elif d == Rotation.left.value:
            if self.facing == Direction.east.value:
                self.facing = Direction.north.value
            elif self.facing == Direction.south.value:
                self.facing = Direction.east.value
            elif self.facing == Direction.west.value:
                self.facing = Direction.south.value
            elif self.facing == Direction.north.value:
                self.facing = Direction.west.value

    def rotate_deg(self, direction, degrees):
        times = int(degrees / 90)
        for _ in range(times):
            self.rotate_facing(direction)

    def move_facing(self, distance):
        if self.facing == Direction.north.value:
            self.pos_north = self.pos_north + distance
        elif self.facing == Direction.south.value:
            self.pos_north = self.pos_north - distance
        elif self.facing == Direction.east.value:
            self.pos_east = self.pos_east + distance
        elif self.facing == Direction.west.value:
            self.pos_east = self.pos_east - distance

    def move_direction(self, direction, distance):
        if direction == Direction.north.value:
            self.pos_north = self.pos_north + distance
        elif direction == Direction.south.value:
            self.pos_north = self.pos_north - distance
        elif direction == Direction.east.value:
            self.pos_east = self.pos_east + distance
        elif direction == Direction.west.value:
            self.pos_east = self.pos_east - distance


with open("input", "r") as f:
    for l in f.readlines():
        inp.append(l.rsplit()[0])

boat = Boat()

for i in inp:
    P = i[0]
    V = int(i[1:])
    if P in [e.value for e in Direction]:
        boat.move_direction(P, V)
    elif P in [e.value for e in Rotation]:
        boat.rotate_deg(P, V)
    elif P in [e.value for e in Move]:
        boat.move_facing(V)


print("Result = ", abs(boat.pos_east) + abs(boat.pos_north))
