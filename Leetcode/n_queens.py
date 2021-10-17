from collections import deque
import copy

class Queen:

  def __init__(self, i, j):
    self.i = i
    self.j = j

  def influences(self, i, j):
    return i == self.i or j == self.j or abs(i - self.i) == abs(j - self.j)

  def __str__(self):
    return f'({self.i}, {self.j})'

class Board:
  def __init__(self, n, queens=None):
    self.queens = queens or []
    self.n = n

  def pushQueen(self, i, j):
    queen = Queen(i, j)
    self.queens.append(queen)

  def isOpen(self, i, j):
    for queen in self.queens:
      if queen.influences(i,j):
        return False
    return True

  def frozen(self):
    return frozenset([str(queen) for queen in self.queens])

  @property
  def full(self):
    return len(self.queens) == self.n
    # if self.n % 2 == 0:
    #   return len(self.queens) == self.n // 2
    # else:
    #   return len(self.queens) == self.n // 2 + 1

  def popQueen(self):
    self.queens.pop()

  def clone(self):
    return Board(self.n, copy.deepcopy(self.queens))

  def serialize(self):
    ret = [['.']*self.n for _ in range(self.n)]
    for queen in self.queens:
      ret[queen.i][queen.j] = 'Q'
    return '\n'.join([''.join(r) for r in ret])

class Solution:
  def solveNQueens(self, n):
    print("Solving board", n)
    board = Board(n)
    if n % 2 == 1:
      board.pushQueen(n // 2, n // 2)
    validBoards = []
    stack = deque()
    stack.append(board)
    crumbs = set()
    while stack:
      currBoard = stack.pop()
      if currBoard.full:
        validBoards.append(currBoard)
      else:
        for i in range(n):
          for j in range(n):
            if currBoard.isOpen(i, j):
              copyBoard = currBoard.clone()
              copyBoard.pushQueen(i, j)
              if copyBoard.frozen() not in crumbs:
                crumbs.add(copyBoard.frozen())
                copyBoard.popQueen()
                copyBoard.pushQueen(n - i, n - j)
                crumbs.add(copyBoard.frozen())
                crumbs.add(copyBoard.frozen())
                copyBoard.popQueen()
                copyBoard.pushQueen(n - j, n - i)
                crumbs.add(copyBoard.frozen())
                copyBoard.popQueen()
                copyBoard.pushQueen(j, i)
                crumbs.add(copyBoard.frozen())
                copyBoard.popQueen()
                copyBoard.pushQueen(i, j)
                stack.append(copyBoard)
    allB = [board.serialize() for board in validBoards]
    allB = list(set(allB))
    return allB

for i in range(1, 10):
  for b in Solution().solveNQueens(i):
    print("==========")
    print(b)
    print("==========")



    