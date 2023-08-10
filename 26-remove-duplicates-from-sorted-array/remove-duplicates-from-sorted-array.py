class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        index = 1
        while index < len(nums):
            if nums[index] == nums[index-1]:
                nums.pop(index)
                continue
            index += 1
        return len(nums)