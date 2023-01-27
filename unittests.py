#!/usr/bin/env python3.11
import unittest
from toy_robot.blueprint import Robot
from toy_robot.platform import Table
from toy_robot.position import Direction
from toy_robot.commands import Place, Right, Left, Move

table = Table(5, 5)

class Tests(unittest.TestCase):
  # Test the default position of robot
  def test_default_position(self):
    robot = Robot()
    self.assertEqual(robot.get_orientation(), (0,0,'NORTH')),
    self.assertFalse(robot.on_table)

  # Test that the validation for place_ontable is working
  def test_placement_edge(self):
    placement_edge = [
        'PLACE -1,0,NORTH',
        'PLACE 0,-1,NORTH',
        'PLACE 0,0,POTATO',
        'PLACE 5,0,NORTH',
        'PLACE 0,5,NORTH'
    ]
    for placement in placement_edge:
      robot = Robot()
      place = Place(placement, table)
      place.command(robot)
      self.assertFalse(robot.on_table)

  # Test that the place_ontable is working
  def test_place_on_table(self):
    robot = Robot()
    placement_test = 'PLACE 2,2,NORTH'
    robot = Robot()
    place = Place(placement_test, table)
    place.command(robot)
    self.assertEqual(robot.get_orientation(), (2,2,'NORTH'))
    self.assertTrue(robot.on_table)

  # Test rotating the robot to the right
  def test_right_rotation(self):
    robot = Robot()
    orientation = {
      Direction.NORTH: 'EAST',
      Direction.EAST: 'SOUTH',
      Direction.SOUTH: 'WEST',
      Direction.WEST: 'NORTH'
    }
    for direction, expected_result in orientation.items():
      right = Right(table)
      robot.direction = direction
      right.command(robot)
      self.assertEqual(robot.direction.name, expected_result)

  # Testing rotating the robot to the left
  def test_left_rotation(self):
    robot = Robot()
    orientation = {
      Direction.NORTH: 'WEST',
      Direction.WEST: 'SOUTH',
      Direction.SOUTH: 'EAST',
      Direction.EAST: 'NORTH'
    }
    for direction, expected_result in orientation.items():
      left = Left(table)
      robot.direction = direction
      left.command(robot)
      self.assertEqual(robot.direction.name, expected_result)

  # Testing robot movement depending on direction
  def test_left_rotation(self):
    robot = Robot()
    orientation = {
      Direction.NORTH: (2,3,'NORTH'),
      Direction.EAST: (3,2,'EAST'),
      Direction.SOUTH: (2,1,'SOUTH'),
      Direction.WEST: (1,2,'WEST')
    }
    for direction, expected_result in orientation.items():
      place = Place('PLACE 2,2,NORTH', table)
      place.command(robot)
      robot.direction = direction
      move = Move(table)
      move.command(robot)
      self.assertEqual(robot.get_orientation(), expected_result)

if __name__ == '__main__':
  unittest.main()
