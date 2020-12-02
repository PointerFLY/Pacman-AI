# mazeGenerator.py
# ----------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import random, sys

"""
maze generator code

algorithm:
start with an empty grid
draw a wall with gaps, dividing the grid in 2
repeat recursively for each sub-grid

pacman details:
players 1,3 always start in the bottom left; 2,4 in the top right
food is placed in dead ends and then randomly (though not too close to the pacmen starting positions)

notes:
the final map includes a symmetric, flipped copy
the first wall has k gaps, the next wall has k/2 gaps, etc. (min=1)

@author: Dan Gillick
@author: Jie Tang
"""

W = '%'
F = '.'
C = 'o'
E = ' '

class Maze:

  def __init__(self, rows, cols, anchor=(0, 0), root=None):
    """
    generate an empty maze
    anchor is the top left corner of this grid's position in its parent grid
    """
    self.r = rows
    self.c = cols
    self.grid = [[E for col in range(cols)] for row in range(rows)]
    self.anchor = anchor
    self.rooms = []
    self.root = root
    if not self.root: self.root = self

  def to_map(self):
    """
    add a flipped symmetric copy on the right
    add a border
    """

    ## add a flipped symmetric copy
    for row in range(self.r):
      for col in range(self.c-1, -1, -1):
        self.grid[self.r-row-1].append(self.grid[row][col])
    self.c *= 2

    ## add a border
    for row in range(self.r):
      self.grid[row] = [W] + self.grid[row] + [W]
    self.c += 2
    self.grid.insert(0, [W for c in range(self.c)])
    self.grid.append([W for c in range(self.c)])
    self.r += 2

  def __str__(self):
    s = ''
    for row in range(self.r):
      for col in range(self.c):
        s += self.grid[row][col]
      s += '\n'
    return s[:-1]

  def add_wall(self, i, gaps=1, vert=True):
    """
    add a wall with gaps
    """
    add_r, add_c = self.anchor
    if vert:
      gaps = min(self.r, gaps)
      slots = [add_r+x for x in range(self.r)]
      if not 0 in slots:
        if self.root.grid[min(slots)-1][add_c+i] == E: slots.remove(min(slots))
        if len(slots) <= gaps: return 0
      if not self.root.c-1 in slots:
        if self.root.grid[max(slots)+1][add_c+i] == E: slots.remove(max(slots))
      if len(slots) <= gaps: return 0
      random.shuffle(slots)
      for row in slots[int(round(gaps)):]:
        self.root.grid[row][add_c+i] = W
      self.rooms.append(Maze(self.r, i, (add_r,add_c), self.root))
      self.rooms.append(Maze(self.r, self.c-i-1, (add_r,add_c+i+1), self.root))
    else:
      gaps = min(self.c, gaps)
      slots = [add_c+x for x in range(self.c)]
      if not 0 in slots:
        if self.root.grid[add_r+i][min(slots)-1] == E: slots.remove(min(slots))
        if len(slots) <= gaps: return 0
      if not self.root.r-1 in slots:
        if self.root.grid[add_r+i][max(slots)+1] == E: slots.remove(max(slots))
      if len(slots) <= gaps: return 0
      random.shuffle(slots)
      for col in slots[int(round(gaps)):]:
        self.root.grid[add_r+i][col] = W
      self.rooms.append(Maze(i, self.c, (add_r,add_c), self.root))
      self.rooms.append(Maze(self.r-i-1, self.c, (add_r+i+1,add_c), self.root))

    return 1

def make_with_prison(room, depth, gaps=1, vert=True, min_width=1, gapfactor=0.5):
  """
  Build a maze with 0,1,2 layers of prison (randomly)
  """
  p = random.randint(0,2)
  proll = random.random()
  if proll < 0.5:
    p = 1
  elif proll < 0.7:
    p = 0
  elif proll < 0.9:
    p = 2
  else:
    p = 3


  add_r, add_c = room.anchor
  print p
  for j in range(p):
    cur_col = 2*(j+1)-1
    for row in range(room.r):
      room.root.grid[row][cur_col] = W
    if j % 2 == 0:
      room.root.grid[0][cur_col] = E
    else:
      room.root.grid[room.r-1][cur_col] = E

  room.rooms.append(Maze(room.r, room.c-(2*p), (add_r, add_c+(2*p)), room.root))
  for sub_room in room.rooms:
    make(sub_room, depth+1, gaps, vert, min_width, gapfactor)

  return 2*p

def make(room, depth, gaps=1, vert=True, min_width=1, gapfactor=0.5):
  """
  recursively build a maze
  TODO: randomize number of gaps?
  """

  ## extreme base case
  if room.r <= min_width and room.c <= min_width: return

  ## decide between vertical and horizontal wall
  if vert: num = room.c
  else: num = room.r
  if num < min_width + 2:
    vert = not vert
    if vert: num = room.c
    else: num = room.r

  ## add a wall to the current room
  if depth==0: wall_slots = [num-2]  ## fix the first wall
  else: wall_slots = range(1, num-1)
  if len(wall_slots) == 0: return
  choice = random.choice(wall_slots)
  if not room.add_wall(choice, gaps, vert): return

  ## recursively add walls
  # if random.random() < 0.8:
  #     vert = not vert
  for sub_room in room.rooms:
    make(sub_room, depth+1, max(1,gaps*gapfactor), not vert,
         min_width, gapfactor)
  # for sub_room in room.rooms:
  #     make(sub_room, depth+1, max(1,gaps/2), not vert, min_width)

def copy_grid(grid):
  new_grid = []
  for row in range(len(grid)):
    new_grid.append([])
    for col in range(len(grid[row])):
      new_grid[row].append(grid[row][col])
  return new_grid

def add_pacman_stuff(maze, max_food=60, max_capsules=4, toskip=0):
  """
  add pacmen starting position
  add food at dead ends plus some extra
  """

  ## parameters
  max_depth = 2

  ## add food at dead ends
  depth = 0
  total_food = 0
  while True:
    new_grid = copy_grid(maze.grid)
    depth += 1
    num_added = 0
    for row in range(1, maze.r-1):
      for col in range(1+toskip, (maze.c/2)-1):
        if (row > maze.r-6) and (col < 6): continue
        if maze.grid[row][col] != E: continue
        neighbors = (maze.grid[row-1][col]==E) + (maze.grid[row][col-1]==E) + (maze.grid[row+1][col]==E) + (maze.grid[row][col+1]==E)
        if neighbors == 1:
          new_grid[row][col] = F
          new_grid[maze.r-row-1][maze.c-(col)-1] = F
          num_added += 2
          total_food += 2
    maze.grid = new_grid
    if num_added == 0: break
    if depth >= max_depth: break

  ## starting pacmen positions
  maze.grid[maze.r-2][1] = '3'
  maze.grid[maze.r-3][1] = '1'
  maze.grid[1][maze.c-2] = '4'
  maze.grid[2][maze.c-2] = '2'

  ## add capsules
  total_capsules = 0
  while total_capsules < max_capsules:
    row = random.randint(1, maze.r-1)
    col = random.randint(1+toskip, (maze.c/2)-2)
    if (row > maze.r-6) and (col < 6): continue
    if(abs(col - maze.c/2) < 3): continue
    if maze.grid[row][col] == E:
      maze.grid[row][col] = C
      maze.grid[maze.r-row-1][maze.c-(col)-1] = C
      total_capsules += 2

  ## extra random food
  while total_food < max_food:
    row = random.randint(1, maze.r-1)
    col = random.randint(1+toskip, (maze.c/2)-1)
    if (row > maze.r-6) and (col < 6): continue
    if(abs(col - maze.c/2) < 3): continue
    if maze.grid[row][col] == E:
      maze.grid[row][col] = F
      maze.grid[maze.r-row-1][maze.c-(col)-1] = F
      total_food += 2

MAX_DIFFERENT_MAZES = 10000

def generateMaze(seed = None):
  if not seed:
    seed = random.randint(1,MAX_DIFFERENT_MAZES)
  random.seed(seed)
  maze = Maze(16,16)
  gapfactor = min(0.65,random.gauss(0.5,0.1))
  skip = make_with_prison(maze, depth=0, gaps=3, vert=True, min_width=1, gapfactor=gapfactor)
  maze.to_map()
  add_pacman_stuff(maze, 2*(maze.r*maze.c/20), 4, skip)
  return str(maze)

if __name__ == '__main__':
  seed = None
  if len(sys.argv) > 1:
    seed = int(sys.argv[1])
  print generateMaze(seed)
