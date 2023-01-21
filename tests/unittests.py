import unittest
from toy_robot.toy_robot import Table, Robot, Command

table = Table(5, 5)
robot = Robot()
command = Command(table, robot, 'commands.txt')

class RobotLocationChecks(unittest.TestCase):
  def test_default(self):
    pass

if __name__ == '__main__':
  unittest.main()