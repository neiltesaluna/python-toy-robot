from enum import Enum, auto
# determining the position of the robot
class Location:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def get_location(self) -> tuple[int, int]:
        return self.x, self.y

    def update_location(self, x: int, y: int):
        self.x += x
        self.y += y

# determining the direction the robot is facing
class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()