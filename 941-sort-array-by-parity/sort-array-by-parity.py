class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        index = 0
        while index < len(nums):
            if nums[index] % 2 == 0:
                temp = nums.pop(index)
                nums.insert(0, temp)
            index += 1
        return nums