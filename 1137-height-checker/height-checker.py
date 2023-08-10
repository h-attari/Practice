class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        result = 0
        for index in range(len(heights)):
            if expected[index] != heights[index]:
                result += 1
        return result