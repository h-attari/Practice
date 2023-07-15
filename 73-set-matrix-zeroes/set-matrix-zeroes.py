class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_0, cols_0 = [], []
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    rows_0.append(row)
                    cols_0.append(col)
        for row in range(len(matrix)):
            flag_0 = True if row in rows_0 else False
            for col in range(len(matrix[row])):
                if flag_0:
                    matrix[row][col] = 0
                elif col in cols_0:
                    matrix[row][col] = 0