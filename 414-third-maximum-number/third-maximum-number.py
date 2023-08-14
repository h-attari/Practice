class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        x, y, z = float("-inf"), float("-inf"), float("-inf")
        for num in nums:
            if num > x:
                z = y
                y = x
                x = num
            elif num > y:
                z = y
                y = num
            elif num > z:
                z = num
        return z