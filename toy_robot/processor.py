from typing import TypeAlias, Mapping, TypeVar
from toy_robot.robot import Robot
from toy_robot.commands import Commands, Place
from toy_robot.platform import Platform
from toy_robot.validators import PlacementCheck


CommandsChild = TypeVar('CommandsChild', bound=Commands)

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
        available_actions: Mapping[str, TypeAlias[CommandsChild]] = {action_class.__name__.upper(): action_class for action_class in Commands.__subclasses__()}
        for move in self.moveset:
            if "PLACE" in move:
                place_validator = PlacementCheck()
                Place(move, self.platform, place_validator).command(self.robot)
            else:
                if self.robot.on_table:
                    operation = available_actions.get(move)
                    try:
                        operation().command(self.robot)
                    except TypeError:
                        print(f"That command {move} doesn't have an associated action! Ignoring...")

        return f'End of commands, last location is: {self.robot.location.get_location()} and is facing {self.robot.direction.name}'