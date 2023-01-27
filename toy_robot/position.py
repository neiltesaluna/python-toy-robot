from enum import Enum, auto
# determining the position of the robot
class Location:
    def __init__(self, x:int, y:int) -> tuple[int, int]:
        self.x = x
        self.y = y

    def location(self):
        return self.x, self.y

# determining the direction the robot is facing
class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()