class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        self.sum_matrix = [[0]*self.COLS for i in range(self.ROWS)]
        
        for i in range(self.ROWS):
            row_sum = 0
            for j in range(self.COLS):
                if(i > 0):
                    self.sum_matrix[i][j] += self.sum_matrix[i - 1][j]
                if(j > 0):
                    self.sum_matrix[i][j] += row_sum

                row_sum += matrix[i][j]
                self.sum_matrix[i][j] += matrix[i][j]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # print(self.sum_matrix)
        sum_val = self.sum_matrix[row2][col2]
        top = 0
        side = 0
        overlap = 0
        if(row1 - 1 >= 0):
            top = self.sum_matrix[row1 - 1][col2]
        if(col1 - 1 >= 0):
            side = self.sum_matrix[row2][col1 - 1]
        if(row1 - 1 >= 0 and col1 - 1 >= 0):
            overlap = self.sum_matrix[row1 - 1][col1 - 1]
        
        return sum_val - top - side + overlap



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)