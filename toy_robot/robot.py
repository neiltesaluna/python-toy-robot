# creating new robot object
from abc import ABC, abstractmethod
from toy_robot.position import Location, Direction

class Robot(ABC):
    """setting up robot with initial location values of (0, 0, NORTH)"""
    def __init__(
        self,
        location: Location = Location(0, 0),
        direction: Direction = Direction.NORTH,
        on_table: bool = False
        ):

            self.location = location
            self.direction = direction
            self.on_table = on_table

    def get_orientation(self):
        return self.location.x, self.location.y, self.direction.name
