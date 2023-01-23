import unittest
from toy_robot.toy_robot import Table, Robot, Command

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

  # Test rotating the robot to the right
  def test_right_rotation(self):
    robot = Robot()
    # avail_directions ('NORTH', 'EAST', 'SOUTH', 'WEST')
    orientation = robot.avail_directions
    for i in range(len(orientation)):
      robot.direction = orientation[i]
      robot.rotation('RIGHT')
      if i == len(orientation)-1:
       self.assertEqual(robot.direction, orientation[0])
      else:
        self.assertEqual(robot.direction, orientation[i+1])

  # Testing rotating the robot to the left
  def test_left_rotation(self):
    robot = Robot()
    # avail_directions ('NORTH', 'EAST', 'SOUTH', 'WEST')
    orientation = robot.avail_directions
    for i in range(len(orientation)):
      robot.direction = orientation[i]
      robot.rotation('LEFT')
      if i == 0:
       self.assertEqual(robot.direction, orientation[len(orientation)-1])
      else:
        self.assertEqual(robot.direction, orientation[i-1])





if __name__ == '__main__':
  unittest.main()
