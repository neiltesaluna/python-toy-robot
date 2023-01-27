#!/usr/bin/env python3.11
import unittest
from toy_robot.platform import Table
from toy_robot.blueprint import Robot
from toy_robot.processor import MovesetParser, Runner

table = Table(5, 5)

robot = Robot()
moveset = MovesetParser('moveset.txt').parse_moveset()
runner = Runner(moveset, robot, table)
print(runner.action())



class IntegrationTests(unittest.TestCase):
  def test_a(self):
    robot = Robot()
    moveset = MovesetParser('fixtures/test_a.txt').parse_moveset()
    runner = Runner(moveset, robot, table)
    self.assertEqual(runner.action(), "End of commands, last location is: (0, 2) SOUTH")

  def test_b(self):
    robot = Robot()
    moveset = MovesetParser('fixtures/test_b.txt').parse_moveset()
    runner = Runner(moveset, robot, table)
    self.assertEqual(runner.action(), "End of commands, last location is: (1, 1) EAST")

  def test_c(self):
    robot = Robot()
    moveset = MovesetParser('fixtures/test_c.txt').parse_moveset()
    runner = Runner(moveset, robot, table)
    self.assertEqual(runner.action(), "End of commands, last location is: (3, 0) SOUTH")

  def test_d(self):
    robot = Robot()
    moveset = MovesetParser('fixtures/test_d.txt').parse_moveset()
    runner = Runner(moveset, robot, table)
    self.assertEqual(runner.action(), "End of commands, robot was never placed on the table!")

if __name__ == '__main__':
  unittest.main()