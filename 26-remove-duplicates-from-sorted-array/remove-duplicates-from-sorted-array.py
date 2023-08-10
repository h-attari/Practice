class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp_set = set()
        index = 0
        while index < len(nums):
            if nums[index] in temp_set:
                nums.pop(index)
                continue
            temp_set.add(nums[index])
            index += 1
        return len(nums)