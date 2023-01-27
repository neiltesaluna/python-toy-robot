from typing import TypeAlias, Mapping, TypeVar
from toy_robot.blueprint import Robot
from toy_robot.commands import Commands, Place
from toy_robot.platform import Platform

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
                Place(move, self.platform).command(self.robot)
            else:
                if self.robot.on_table:
                    try:
                        operation = available_actions[move]
                        operation(self.platform).command(self.robot)
                    except KeyError:
                        print(f"That command {move} doesn't have an associated action! Ignoring...")
        if self.robot.on_table:
            return f'End of commands, last location is: {self.robot.location.get_location()} {self.robot.direction.name}'
        else:
            return 'End of commands, robot was never placed on the table!'