class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive_count = 0
        result = 0
        for num in nums:
            if num == 0:
                result = max(result, consecutive_count)
                consecutive_count = 0
                continue
            consecutive_count += 1
        return max(result, consecutive_count)