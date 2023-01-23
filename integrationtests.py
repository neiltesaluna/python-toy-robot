import unittest
from toy_robot.toy_robot import Table, Robot, Command

table = Table(5, 5)

class IntegrationTests(unittest.TestCase):
  def test_a(self):
    robot = Robot()
    command = Command(table, robot, 'fixtures/test_a.txt')
    self.assertEqual(command.run_robot(), "End of commands, last location is: (0, 2, 'SOUTH')")

  def test_b(self):
    robot = Robot()
    command = Command(table, robot, 'fixtures/test_b.txt')
    self.assertEqual(command.run_robot(), "End of commands, last location is: (1, 1, 'EAST')")

  def test_c(self):
    robot = Robot()
    command = Command(table, robot, 'fixtures/test_c.txt')
    self.assertEqual(command.run_robot(), "End of commands, last location is: (3, 0, 'SOUTH')")

  def test_d(self):
    robot = Robot()
    command = Command(table, robot, 'fixtures/test_d.txt')
    self.assertEqual(command.run_robot(), "End of commands, robot was never placed on the table!")

if __name__ == '__main__':
  unittest.main()