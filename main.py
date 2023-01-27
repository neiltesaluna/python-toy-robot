#!/usr/bin/env python3.11
from toy_robot.blueprint import Robot
from toy_robot.processor import MovesetParser, Runner
from toy_robot.platform import Table

def main():
    robot = Robot()
    moveset = MovesetParser('moveset.txt').parse_moveset()
    table = Table(5, 5)
    runner = Runner(moveset, robot, table)
    print(runner.action())

if __name__ == '__main__':
    main()