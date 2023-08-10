class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        index = 0
        while index < len(nums):
            if nums[index] == 0:
                temp.append(nums.pop(index))
                continue
            index += 1
        nums.extend(temp)