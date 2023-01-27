from toy_robot.robot import Robot
from toy_robot.commands import Commands, Report
from toy_robot.platform import Platform
from toy_robot.validators import Validator, PlacementCheck
from abc import ABC, abstractmethod
# reads the file for list of commands
class MovesetParser:
    def __init__(self, filename:str):
        self.filename:str = filename

    def parse_moveset(self) -> list[str]:
        with open(self.filename, 'r') as f:
            moveset:list[str] = f.readlines()
            for i, cmd in enumerate(moveset):
                moveset[i] = cmd.upper()
                moveset[i] = cmd.strip()
            return moveset

class Runner:
    def __init__(self, moveset: list[str], robot: Robot, platform: Platform):
        self.moveset = moveset
        self.robot = robot
        self.platform = platform

    def action(self) -> str:
        available_actions = {action_class.__name__.upper(): action_class for action_class in Commands.__subclasses__()}
        for move in self.moveset:
            if move in available_actions:
                operation = available_actions[move]()
                operation.command(self.robot)
            elif "PLACE" in move:
                place_command = available_actions["PLACE"]
                place_command(move, self.platform, PlacementCheck).command(self.robot)

        return f'End of commands, last location is: {self.robot.location.get_location()} and is facing {self.robot.direction.name}'