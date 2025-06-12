class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        result = abs(nums[0] - nums[-1])
        for index in range(len(nums)-1):
            result = max(result, abs(nums[index] - nums[index + 1]))
        return result
        