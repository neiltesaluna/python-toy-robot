from abc import ABC, abstractmethod
from toy_robot.platform import Platform
from toy_robot.position import Direction

class Validator(ABC):
    @abstractmethod
    def check(self, platform: Platform, x: int, y: int, direction: Direction) -> bool:
        pass

class PlatformCheck(Validator):
    def check(self, platform: Platform, x: int, y: int, direction: Direction) -> bool:
        available_placement = platform.available_blocks()
        try:
            if available_placement[x][y] == 1:
                return True
            else:
                return False
        except IndexError:
            print("You've missed the table!")
            return False