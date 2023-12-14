class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m , n = len(grid) , len(grid[0                                                       ])
        onesRow , onesCol = [0] * m , [0] * n 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    onesRow[i] += 1
                    onesCol[j] += 1 
        for i in range(m):
            for j in range(n):
                grid[i][j] = onesRow[i] + onesCol[j] -(m - onesRow[i] + n - onesCol[j])
        return grid
        