class NQueen:
    def __init__(self, num_of_queens):
        self.N = num_of_queens
        self.solutions = []

    def solveNQueen(self):
        grid = [[0] * self.N for _ in range(self.N)]
        if self.solveNQueenUtils(grid, 0) == False:
            print("Solution Does Not Exist For: ", str(self.N), "Queens")
            return False
        print("Found " + str(len(self.solutions)) + " Solutions For: ", str(self.N), "Queens")
        for i, solution in enumerate(self.solutions):
            print("Solution " + str(i+1) + ":")
            self.printSolution(solution)
            print()

    def solveNQueenUtils(self, grid, column):
        if column >= self.N:
            # For All Possible Solutions
            solution = []
            for i in range(self.N):
                row = []
                for j in range(self.N):
                    row.append(grid[i][j])
                solution.append(row)
            self.solutions.append(solution)
            return True

        for row in range(self.N):
            if self.is_safe(grid, row, column) == True:
                grid[row][column] = 1
                self.solveNQueenUtils(grid, column + 1)
                grid[row][column] = 0

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
            print(" ".join(str(cell) for cell in row))


NumOfQueens = int(input("number of Queens: "))
Queen = NQueen(NumOfQueens)
Queen.solveNQueen()
