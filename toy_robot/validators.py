from abc import ABC, abstractmethod
from toy_robot.platform import Platform
from toy_robot.position import Direction

class Validator(ABC):
    @abstractmethod
    def check(self) -> bool:
        pass

class PlacementCheck(Validator):
    def __init__(self, platform: Platform, x: int, y: int, direction: Direction):
        self.platform = platform
        self.x = x
        self.y = y
        self.direction = direction

    def check(self) -> bool:
        available_placement = self.platform.available_blocks()
        try:
            if available_placement[self.x][self.y] == 1:
                return True
            else:
                return False
        except IndexError:
            print("You've missed the table!")
            return False