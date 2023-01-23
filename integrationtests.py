import unittest
from toy_robot.toy_robot import Table, Robot, Command

table = Table(5, 5)

class IntegrationTests(unittest.TestCase):
  def test_a(self):
    robot = Robot()
    command = Command(table, robot, 'fixtures/test_a.txt')
    command.run_robot()
    self.assertEqual(robot.position(), (0, 2, 'SOUTH'))

  def test_b(self):
    robot = Robot()
    command = Command(table, robot, 'fixtures/test_b.txt')
    command.run_robot()
    self.assertEqual(robot.position(), (1, 1, 'EAST'))

  def test_c(self):
    robot = Robot()
    command = Command(table, robot, 'fixtures/test_c.txt')
    command.run_robot()
    self.assertEqual(robot.position(), (3, 0, 'SOUTH'))

if __name__ == '__main__':
  unittest.main()