
class Solution:
  def isValidSudoku(self, board):
    for i in range(9):
      row = board[i]
      numsInRow = set()
      numsInCol = set()
      for j in range(9):
        if board[i][j] != '.' and board[i][j] in numsInRow:
          return False
        else:
          numsInRow.add(board[i][j])
        if board[j][i] != '.' and board[j][i] in numsInCol:
          return False
        else:
          numsInCol.add(board[j][i])
    for squareCenterX in range(1, 9, 3):
      for squareCenterY in range(1, 9, 3):
        squareSet = set()
        for i in range(squareCenterX-1, squareCenterX+2):
          for j in range(squareCenterY-1, squareCenterY+2):
            if board[i][j] != '.' and board[i][j] in squareSet:
              return False
            else:
              squareSet.add(board[i][j])
    return True