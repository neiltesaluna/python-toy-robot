# listing out type of robot commands
from abc import ABC, abstractmethod
from toy_robot.robot import Robot
from toy_robot.position import Location, Direction
from toy_robot.platform import Platform
from toy_robot.validators import Validator

class Commands(ABC):

    @abstractmethod
    def command(self, robot: Robot) -> tuple[Location, Direction]:
        pass

class Report(Commands):
    def command(self, robot: Robot) -> tuple[Location, Direction]:
        print(robot.location.x, robot.location.y, robot.direction.name)
        return robot.location, robot.direction

class Move(Commands):
    def command(self, robot: Robot) -> tuple[Location, Direction]:
        pass

class Left(Commands):
    def command(self, robot: Robot) -> tuple[Location, Direction]:
        pass

class Right(Commands):
    def command(self, robot: Robot) -> tuple[Location, Direction]:
        pass

class Place(Commands):
    def __init__(self, place_command:str, platform: Platform, validator: Validator):
        self.place_command = place_command
        self.platform = platform
        self.validator = validator

    def command(self, robot: Robot) -> tuple[Location, Direction]:
        _, location = self.place_command.split()
        x, y, direction = location.split(',')
        if self.validator.check(self.platform, int(x), int(y), Direction[direction]):
            robot.on_table = True
            robot.location, robot.direction = Location(int(x),int(y)), Direction[direction]
        return robot.location, robot.direction