# listing out type of robot commands
from abc import ABC, abstractmethod
from toy_robot.robot import Robot
from toy_robot.position import Location, Direction
from toy_robot.platform import Platform
from toy_robot.validators import PlatformCheck

class Commands(ABC):
    @abstractmethod
    def __init__(self, platform: Platform):
        self.platform = platform
    @abstractmethod
    def command(self, robot: Robot) -> tuple[Location, Direction]:
        pass

class Report(Commands):
    def __init__(self, platform: Platform):
        self.platform = platform
    def command(self, robot: Robot) -> tuple[Location, Direction]:
        print(robot.location.x, robot.location.y, robot.direction.name)
        return robot.location, robot.direction

class Move(Commands):
    def __init__(self, platform: Platform):
        self.platform = platform
    def command(self, robot: Robot) -> tuple[Location, Direction]:
        move = {
            "NORTH":(0, 1),
            "EAST": (1, 0),
            "SOUTH":(0, -1),
            "WEST": (-1, 0)
        }
        x, y = move[robot.direction.name]
        move_validator = PlatformCheck()
        if move_validator.check(self.platform, robot.location.x + x, robot.location.y + y, robot.direction):
            robot.location.update_location(x, y)
        return robot.location, robot.direction

class Left(Commands):
    def __init__(self, platform: Platform):
        self.platform = platform
    def command(self, robot: Robot) -> tuple[Location, Direction]:
        left = {
            "NORTH": Direction.WEST,
            "WEST": Direction.SOUTH,
            "SOUTH": Direction.EAST,
            "EAST": Direction.NORTH
        }
        robot.direction = left[robot.direction.name]
        return robot.location, robot.direction

class Right(Commands):
    def __init__(self, platform: Platform):
        self.platform = platform
    def command(self, robot: Robot) -> tuple[Location, Direction]:
        right = {
            "NORTH": Direction.EAST,
            "EAST": Direction.SOUTH,
            "SOUTH": Direction.WEST,
            "WEST": Direction.NORTH
        }
        robot.direction = right[robot.direction.name]
        return robot.location, robot.direction


class Place(Commands):
    def __init__(self, place_command:str, platform: Platform):
        self.place_command = place_command
        self.platform = platform
    def command(self, robot: Robot) -> tuple[Location, Direction]:
        place_validator = PlatformCheck()
        _, location = self.place_command.split()
        x, y, direction = location.split(',')
        if place_validator.check(self.platform, int(x), int(y), Direction[direction]):
            robot.on_table = True
            robot.location, robot.direction = Location(int(x),int(y)), Direction[direction]
        return robot.location, robot.direction