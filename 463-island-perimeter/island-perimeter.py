class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    continue
                result += 4
                if row > 0 and grid[row-1][col] == 1:
                    result -= 1
                if row < len(grid)-1 and grid[row+1][col] == 1:
                    result -= 1
                if col > 0 and grid[row][col-1] == 1:
                    result -= 1
                if col < len(grid[row])-1 and grid[row][col+1] == 1:
                    result -= 1
        
        return result
        