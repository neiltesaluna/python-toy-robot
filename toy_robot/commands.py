# listing out type of robot commands
from abc import ABC, abstractmethod
from toy_robot.robot import Robot
from toy_robot.position import Direction
from toy_robot.platform import Platform
from toy_robot.validators import Validator

class Commands(ABC):
    x: int
    y: int
    direction: Direction

    @abstractmethod
    def command(self, robot: Robot) -> tuple[int, int, Direction]:
        pass

class Report(Commands):
    def command(self, robot: Robot) -> tuple[int, int, Direction]:
        return robot.x, robot.y, robot.direction

class Move(Commands):
    def command(self, robot: Robot) -> tuple[int, int, Direction]:
        pass

class Left(Commands):
    def command(self, robot: Robot) -> tuple[int, int, Direction]:
        pass

class Right(Commands):
    def command(self, robot: Robot) -> tuple[int, int, Direction]:
        pass

class Place(Commands):
    def __init__(self, place_command:str, platform: Platform, validator: Validator):
        self.place_command = place_command
        self.platform = platform
        self.validator = validator

    def command(self, robot: Robot) -> tuple[int, int, Direction]:
        _, location = self.place_command.split()
        x, y, direction = location.split(',')
        placement_validator = self.validator(self.platform, int(x), int(y), Direction[direction])
        if placement_validator.check():
            robot.on_table = True
            robot.x, robot.y, robot.direction = int(x), int(y), Direction[direction]
        return robot.x, robot.y, robot.direction