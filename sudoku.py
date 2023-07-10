import os
import sys
import time

import numpy as np


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class SudokuSolver:
    def __init__(self, grid, row_size=9, column_size=9):
        self.grid = grid

        self.row_size = row_size
        self.column_size = column_size

    def find_empty(self):
        for row in range(self.column_size):
            for column in range(self.row_size):
                if self.grid[row][column] == 0:
                    return row, column

    def check(self, num, pos):
        row, col = pos
        # Check if all row elements include this number
        for j in range(self.row_size):
            if self.grid[row][j] == num:
                return False

        # Check if all column elements include this number
        for i in range(self.column_size):
            if self.grid[i][col] == num:
                return False

        # Check if the number is already included in the block
        row_block_start = 3 * (row // 3)
        col_block_start = 3 * (col // 3)

        row_block_end = row_block_start + 3
        col_block_end = col_block_start + 3
        for i in range(row_block_start, row_block_end):
            for j in range(col_block_start, col_block_end):
                if self.grid[i][j] == num:
                    return False

        return True

    def solve(self):
        blank = self.find_empty()

        if not blank:
            return True
        else:
            row, col = blank

        for i in range(1, self.column_size + 1):

            if self.check(i, blank):
                self.grid[row][col] = i

                if self.solve():
                    return True

                self.grid[row][col] = 0
        return False

    def visualize(self):
        visualized = ""
        counter = 0

        for i in self.grid:
            for j in i:
                if counter % 3 == 0:
                    if counter % (3 * len(self.grid[0])) == 0:
                        visualized += "\n"
                    visualized += " "

                visualized += f"{j} "
                counter += 1
            visualized += "\n"

        return visualized


grid = np.zeros([9, 9], dtype='int8')
sudoku = SudokuSolver(grid)

print(sudoku.visualize())
sudoku.solve()
print(sudoku.visualize())
