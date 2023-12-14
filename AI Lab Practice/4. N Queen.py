class NQueen:
    def __init__(self, num_of_queens):
        self.N = num_of_queens

    def solveNQueen(self):
        grid = [[0] * self.N for _ in range(self.N)]
        if self.solveNQueenUtils(grid, 0) == False:
            print("Solution Does Not Exist For: ", str(self.N), "Queens")
            return False
        print("Solution Exists For: ", str(self.N), "Queens")
        self.printSolution(grid)
        return True

    def solveNQueenUtils(self, grid, column):
        if column >= self.N:
            return True
        for row in range(self.N):
            if self.is_safe(grid, row, column) == True:
                grid[row][column] = 1
                if self.solveNQueenUtils(grid, column + 1) == True:
                    return True
                grid[row][column] = 0
        return False

    def is_safe(self, grid, row, column):
        for i in range(column):
            if grid[row][i] == 1:
                return False

        i = row
        j = column
        while i >= 0 and j >= 0:
            if grid[i][j] == 1:
                return False
            i -= 1
            j -= 1

        i = row
        j = column
        while j >= 0 and i < self.N:
            if grid[i][j] == 1:
                return False
            i += 1
            j -= 1
        return True

    def printSolution(self, board):
        for row in board:
            print(" " .join(str(cell) for cell in row))


NumOfQueens = int(input("number of Queens: "))
Queen = NQueen(NumOfQueens)
Queen.solveNQueen()
