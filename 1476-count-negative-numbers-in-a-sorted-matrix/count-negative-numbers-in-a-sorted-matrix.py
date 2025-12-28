class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negative_count = 0
        for row in grid:
            negative_count += len(list(filter(lambda x: x < 0, row)))
        return negative_count