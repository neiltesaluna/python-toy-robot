from toy_robot.toy_robot import Table, Robot, Command
# table size is (x,y) = 5 x 5
table = Table(5, 5)
robot = Robot()
command = Command()

command.run_robot(table, robot, 'commands.txt')