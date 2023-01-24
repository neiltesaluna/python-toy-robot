#!/usr/bin/env python3.11
import unittest
from toy_robot.toy_robot import Table, Robot

table = Table(5, 5)

class Tests(unittest.TestCase):
  # Test the default position of robot
  def test_default_position(self):
    robot = Robot()
    self.assertEqual(robot.position(), (0,0,'NORTH')),
    self.assertFalse(robot.check_on_table())

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
      robot.place_on_table(placement, table)
      self.assertFalse(robot.check_on_table())

  # Test that the place_ontable is working
  def test_place_on_table(self):
    robot = Robot()
    placement_test = 'PLACE 2,2,NORTH'
    robot.place_on_table(placement_test, table)
    self.assertEqual(robot.position(), (2,2,'NORTH'))
    self.assertTrue(robot.check_on_table())

  # Test rotating the robot to the right
  def test_right_rotation(self):
    robot = Robot()
    orientation = {
      'NORTH': 'EAST',
      'EAST': 'SOUTH',
      'SOUTH': 'WEST',
      'WEST': 'NORTH'
    }
    for direction, expected_result in orientation.items():
      robot.direction = direction
      robot.rotation('RIGHT')
      self.assertEqual(robot.direction, expected_result)

  # Testing rotating the robot to the left
  def test_left_rotation(self):
    robot = Robot()
    orientation = {
      'NORTH': 'WEST',
      'WEST': 'SOUTH',
      'SOUTH': 'EAST',
      'EAST': 'NORTH'
    }
    for direction, expected_result in orientation.items():
      robot.direction = direction
      robot.rotation('LEFT')
      self.assertEqual(robot.direction, expected_result)

  # Testing robot movement depending on direction
  def test_left_rotation(self):
    robot = Robot()
    orientation = {
      'NORTH': (2,3,'NORTH'),
      'EAST': (3,2,'EAST'),
      'SOUTH': (2,1,'SOUTH'),
      'WEST': (1,2,'WEST')
    }
    for direction, expected_result in orientation.items():
      robot.place_on_table('PLACE 2,2,NORTH',table)
      robot.direction = direction
      robot.move(table)
      self.assertEqual(robot.position(), expected_result)

if __name__ == '__main__':
  unittest.main()
