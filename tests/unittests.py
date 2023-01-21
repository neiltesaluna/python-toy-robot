import unittest
from toy_robot.toy_robot import Table, Robot

table = Table(5, 5)
robot = Robot()

class RobotLocationChecks(unittest.TestCase):
  def test_default(self):
    pass

if __name__ == '__main__':
  unittest.main()