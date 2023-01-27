#!/usr/bin/env python3.11
from toy_robot.robot import Robot
from toy_robot.processor import MovesetParser, Runner
from toy_robot.platform import Table

def main():
    robot = Robot()
    moveset = MovesetParser('moveset.txt').parse_moveset()
    runner = Runner(moveset, robot)
    table = Table(5, 5)
    print(table.available_blocks())
    runner.action()

if __name__ == '__main__':
    main()