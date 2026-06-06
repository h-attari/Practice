class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = [0]
        right_sum = []
        for num in nums:
            right_sum.append(total_sum - left_sum[-1] - num)
            left_sum.append(left_sum[-1] + num)
        result = []
        for index in range(len(nums)):
            result.append(abs(left_sum[index] - right_sum[index]))
        return result
        