from collections import deque
import copy

class Solution:
  def solveSudoku(self, board):
    lastBoard = self.makeCertainMoves(board)
    for i in range(9):
      for j in range(9):
        board[i][j] = lastBoard[i][j]


  def makeCertainMoves(self, workingBoard): # Returns a delta from before any moves were made
    allValues = set(['1','2','3','4','5','6','7','8','9'])
    deltas = {}
    decisionTree = deque()
    decisionTree.append(workingBoard)
    while decisionTree:
      board = decisionTree.popleft()
      fullInSquare = [set() for _ in range(9)]
      fullInRow = [set() for _ in range(9)]
      fullInCol = [set() for _ in range(9)]
      full = True
      for i in range(9):
        for j in range(9):
          if board[i][j] == '.':
            full = False
      if full:
        if self.isValidSudoku(board):
          return board
        else:
          continue
      for i in range(9):
        for j in range(9):
          if board[i][j] != '.':
            fullInCol[i].add(board[i][j])
            squareInd = (i // 3) + (j // 3) * 3
            fullInSquare[squareInd].add(board[i][j])
          if board[j][i] != '.':
            fullInRow[i].add(board[j][i])
      needsDecision = True
      decisionPoints = {}
      # print(fullInCol[0])
      # print(fullInRow[0])
      # print(fullInSquare[0])
      for i in range(9):
        for j in range(9):
          if board[i][j] == '.':
            squareInd = (i // 3) + (j // 3) * 3
            availInAll = allValues - fullInCol[i] - fullInRow[j] - fullInSquare[squareInd]
            # print(availInAll)
            if len(availInAll) == 0:
              pass
            elif len(availInAll) == 1:
              needsDecision = False
              board[i][j] = list(availInAll)[0]
            elif len(availInAll) in decisionPoints:
              decisionPoints[len(availInAll)].append((i,j, availInAll))
            else:
              decisionPoints[len(availInAll)] = [(i,j, availInAll)]
      if needsDecision and len(decisionPoints):
        minNumDecisions = min(decisionPoints.keys())
        for i, j, availInAll in decisionPoints[minNumDecisions]:
          for choice in availInAll:
            boardCopy = copy.deepcopy(board)
            boardCopy[i][j] = choice
            decisionTree.append(boardCopy)
      else:
        decisionTree.appendleft(board)
    return workingBoard

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



# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]] 
# board = [[".",".",".","2",".",".",".","6","3"],["3",".",".",".",".","5","4",".","1"],[".",".","1",".",".","3","9","8","."],[".",".",".",".",".",".",".","9","."],[".",".",".","5","3","8",".",".","."],[".","3",".",".",".",".",".",".","."],[".","2","6","3",".",".","5",".","."],["5",".","3","7",".",".",".",".","8"],["4","7",".",".",".","1",".",".","."]]
board = [["1",".",".",".","7",".",".","3","."],["8","3",".","6",".",".",".",".","."],[".",".","2","9",".",".","6",".","8"],["6",".",".",".",".","4","9",".","7"],[".","9",".",".",".",".",".","5","."],["3",".","7","5",".",".",".",".","4"],["2",".","3",".",".","9","1",".","."],[".",".",".",".",".","2",".","4","3"],[".","4",".",".","8",".",".",".","9"]]
solver = Solution()
solver.solveSudoku(board)
for row in board:
  print(row)
print(solver.isValidSudoku(board))