from rest_framework.views import APIView
from rest_framework.response import Response
from random import randint, shuffle
from copy import deepcopy
import time

numberList = [1,2,3,4,5,6,7,8,9]
backup_grid = None
counter = 0

def checkGrid(grid):
  for row in range(9):
    for col in range(9):
      if grid[row][col] == 0:
        return False

  return True

def fillGrid(grid):
  for i in range(81):
    row = i // 9
    col = i % 9

    if grid[row][col] == 0:
      shuffle(numberList)
      for value in numberList:
        if not (value in grid[row]):
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
            square = []
            if row < 3:
              if col < 3:
                square = [grid[i][0:3] for i in range(0,3)]
              elif col < 6:
                square = [grid[i][3:6] for i in range(0,3)]
              else:
                square = [grid[i][6:9] for i in range(0,3)]
            elif row < 6:
              if col < 3:
                square = [grid[i][0:3] for i in range(3,6)]
              elif col < 6:
                square = [grid[i][3:6] for i in range(3,6)]
              else:
                square = [grid[i][6:9] for i in range(3,6)]
            else:
              if col < 3:
                square = [grid[i][0:3] for i in range(6,9)]
              elif col < 6:
                square = [grid[i][3:6] for i in range(6,9)]
              else:
                square = [grid[i][6:9] for i in range(6,9)]

            if not value in (square[0] + square[1] + square[2]):
              grid[row][col] = value
              if checkGrid(grid):
                return True
              else:
                if fillGrid(grid):
                  return True
      break

  grid[row][col]=0

def solveGrid(grid):
  global counter

  for i in range(81):
    row = i // 9
    col = i % 9
    if grid[row][col] == 0:
      for value in range (1,10):
        if not (value in grid[row]):
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
            square = []
            if row < 3:
              if col < 3:
                square = [grid[i][0:3] for i in range(0,3)]
              elif col < 6:
                square = [grid[i][3:6] for i in range(0,3)]
              else:
                square = [grid[i][6:9] for i in range(0,3)]
            elif row < 6:
              if col < 3:
                square = [grid[i][0:3] for i in range(3,6)]
              elif col < 6:
                square = [grid[i][3:6] for i in range(3,6)]
              else:
                square = [grid[i][6:9] for i in range(3,6)]
            else:
              if col < 3:
                square = [grid[i][0:3] for i in range(6,9)]
              elif col < 6:
                square = [grid[i][3:6] for i in range(6,9)]
              else:
                square = [grid[i][6:9] for i in range(6,9)]

            if not value in (square[0] + square[1] + square[2]):
              grid[row][col] = value
              if checkGrid(grid):
                counter += 1
                break
              else:
                if solveGrid(grid):
                  return True
      break

  grid[row][col] = 0

def printGrid(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")

class SudokuManager(APIView):
  def post(self, request):
    # grid = [
    #   [6, 7, 1, 2, 3, 5, 8, 9, 0],
    #   [2, 8, 5, 9, 1, 4, 6, 7, 0],
    #   [4, 3, 0, 8, 0, 6, 2, 1, 5],
    #   [8, 1, 3, 4, 0, 7, 0, 2, 6],
    #   [7, 0, 4, 3, 2, 0, 5, 8, 1],
    #   [9, 5, 2, 6, 0, 1, 3, 4, 7],
    #   [5, 0, 0, 1, 4, 8, 7, 3, 9],
    #   [1, 9, 8, 7, 0, 3, 0, 5, 2],
    #   [3, 0, 7, 0, 9, 2, 1, 6, 8]
    # ]
    # backup_grid = [
    #   [6, 7, 1, 2, 3, 5, 8, 9, 4],
    #   [2, 8, 5, 9, 1, 4, 6, 7, 3],
    #   [4, 3, 9, 8, 7, 6, 2, 1, 5],
    #   [8, 1, 3, 4, 5, 7, 9, 2, 6],
    #   [7, 6, 4, 3, 2, 9, 5, 8, 1],
    #   [9, 5, 2, 6, 8, 1, 3, 4, 7],
    #   [5, 2, 6, 1, 4, 8, 7, 3, 9],
    #   [1, 9, 8, 7, 6, 3, 4, 5, 2],
    #   [3, 4, 7, 5, 9, 2, 1, 6, 8]
    # ]

    failed = True
    while failed:
      failed = False
      grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
      ]
      difficulty_list = {
        1: [35, 37],
        2: [40, 42],
        3: [45, 47],
        4: [50, 52],
        5: [55, 56]
      }
      difficulty = request.data['difficulty']
      last_number = None
      last_number_time = 0
      last_time = time.time()
      empty_slots = randint(difficulty_list[difficulty][0], difficulty_list[difficulty][1])

      fillGrid(grid)
      backup_grid = deepcopy(grid)

      while empty_slots > 0:
        row = randint(0,8)
        col = randint(0,8)
        while grid[row][col] == 0:
          row = randint(0,8)
          col = randint(0,8)

        backup = grid[row][col]
        grid[row][col] = 0
        copyGrid = deepcopy(grid)

        global counter
        counter = 0
        solveGrid(copyGrid)

        if counter != 1:
          grid[row][col] = backup
        else:
          empty_slots -= 1

        now = time.time()

        if empty_slots == last_number:
          last_number_time += (now - last_time)
          if last_number_time >= 10:
            failed = True
            break
        else:
          last_number = empty_slots
          last_number_time = (now - last_time)

        last_time = now

    return Response({"grid": grid, "solution": backup_grid})