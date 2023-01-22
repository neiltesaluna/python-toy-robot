# table object
class Table:
  def __init__(self, width:int, height:int):
    self.width:int = width
    self.height:int = height

# end of table object

# robot object
class Robot:

# defining available directions and commands
  avail_directions:tuple[str, str, str, str] = ('NORTH', 'EAST', 'SOUTH', 'WEST')
  avail_commands:tuple[str, str, str, str, str] = ('PLACE', 'REPORT', 'RIGHT', 'LEFT', 'MOVE')

  def __init__(self, on_table:bool=False, x:int=0, y:int=0, direction:str='NORTH') -> None:
    self.on_table:bool = on_table
    self.x:int = x
    self.y:int = y
    self.direction:str = direction
  
# checking commands then passing to relevant methods
  def command_check(self, command:str, table: Table) -> None:
    if 'PLACE' in command:
      self.place_on_table(command, table)
    elif 'REPORT' == command:
      print(self.location_report())
    elif 'RIGHT' == command or 'LEFT' == command:
      self.rotation(command)
    elif 'MOVE' == command:
      self.move(table)

# returns on_table bool value
  def check_on_table(self) -> bool:
    return self.on_table
    
# returning locations x, y and direction robot is facing
  def location_report(self) -> tuple[int, int, str]:
    return int(self.x), int(self.y), self.direction

# defining where the robot will be placed from parsing command and changes self.on_table to True
  def place_on_table(self, command:str, table:Table) -> None:
    _, location = command.split()
    x, y, direction = location.split(',')
    if int(x) > table.width or int(y) > table.height or direction not in self.avail_directions:
      print('You have missed the table!')
    else:
      self.on_table = True
      self.x, self.y, self.direction = int(x), int(y), direction

# comparing current direction to what index is it on 'avail_directions'. Then updating direction based on index. 
# ++ for right, -- for left and also have edge cases when index reaches the start and end of sequence
  def rotation(self, command:str) -> None:
    current_direction:str = self.direction
    index:int = self.avail_directions.index(current_direction)
    if 'RIGHT' == command:
      if index != len(self.avail_directions)-1:
        self.direction = self.avail_directions[index+1]
      else:
        self.direction = self.avail_directions[0]
    if 'LEFT' == command:
      if index != self.avail_directions[0]:
        self.direction = self.avail_directions[index-1]
      else:
        self.direction = self.avail_directions[len(self.avail_directions)-1]

# checking if movement is x or y based on direction robot is facing, then incrementing or decreasing x or y until table limit
  def move(self, table:Table) -> None:
    if self.direction == 'EAST':
      if self.x < table.width:
        self.x += 1
    elif self.direction == 'WEST':
      if self.x > 0:
        self.x -= 1
    if self.direction == 'NORTH':
      if self.y < table.height:
        self.y += 1
    elif self.direction == 'SOUTH':
      if self.y > 0:
        self.y -= 1
    else:
      print('Edge of the table')
# end of robot object


# command object
class Command:
  # called by run_robot method, open commands files reads lines and formats to uppercase and removes spaces
  def __init__(self, table:Table, robot:Robot, filename:str):
    self.table:Table = table
    self.robot:Robot = robot
    self.filename:str = filename

  def read_commands(self) -> list[str]:
    with open(self.filename, 'r') as f:
      commands:list[str] = f.readlines()
      for i, cmd in enumerate(commands):
        commands[i] = cmd.upper()
        commands[i] = cmd.strip()
      return commands

  # defining what commands to pass to the robot
  def run_robot(self) -> None:
    robot_commands:list[str] = self.read_commands()
    for cmd in robot_commands:
      if self.robot.check_on_table():
        self.robot.command_check(cmd, self.table)
      elif 'PLACE' in cmd:
        self.robot.command_check(cmd, self.table)
      else:
        print('Robot not on the table')
    print('End of commands, last location is:')
    print(self.robot.location_report())
    return self.robot.location_report()
# end of command object