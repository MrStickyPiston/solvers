import numpy as np


class SudokuSolver:
    def __init__(self, grid, size=9, row_block_size=3, col_block_size=3):
        self.grid = grid

        self.size = size

        self.row_block_size = row_block_size
        self.col_block_size = col_block_size

        if self.size != self.row_block_size*self.col_block_size:
            raise SyntaxError(f"{self.size} must be equal to row block size * column block size")

    def find_empty(self):
        for row in range(self.size):
            for column in range(self.size):
                if self.grid[row][column] == 0:
                    return row, column

    def check(self, num, pos):
        row, col = pos

        for i in range(self.size):
            if self.grid[i][col] == num:
                return False
            if self.grid[row][i] == num:
                return False

        # Check if the number is already included in the block
        row_block_start = self.row_block_size * (row // self.row_block_size)
        col_block_start = self.col_block_size * (col // self.col_block_size)

        row_block_end = row_block_start + self.row_block_size
        col_block_end = col_block_start + self.col_block_size
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

        for i in range(1, self.size + 1):

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
                if counter % self.row_block_size == 0:
                    visualized += " "

                if counter % self.size == 0:
                    visualized += "\n"

                if counter % (self.col_block_size * self.size) == 0:
                    visualized += "\n"

                spaces = (3 - len(str(j))) * " "
                visualized += f"{j}{spaces}"
                counter += 1

        return visualized


size = 9
row_block_size = 3
col_block_size = 3

grid = np.zeros([size, size], dtype='int8')
sudoku = SudokuSolver(grid,
                      size=size,
                      row_block_size=row_block_size,
                      col_block_size=col_block_size)

print(sudoku.visualize())
sudoku.solve()
print(sudoku.visualize())
