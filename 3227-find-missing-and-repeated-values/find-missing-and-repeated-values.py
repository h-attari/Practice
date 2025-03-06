class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        result = [None, None]
        temp_lst = [None] * (len(grid) * len(grid))

        for row in grid:
            for num in row:
                index = num - 1
                if temp_lst[index] is not None:
                    result[0] = num
                    continue
                temp_lst[index] = num
        
        for index in range(len(temp_lst)):
            if temp_lst[index] is None:
                result[1] = index + 1
                break
        
        return result
        