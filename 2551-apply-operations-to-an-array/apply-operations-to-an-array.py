class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)-1):
            if nums[index] == nums[index+1]:
                nums[index] *= 2
                nums[index+1] = 0
        for i in range(1, len(nums)):
            j = i
            while nums[j] > 0 and j > 0 and nums[j-1] == 0:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
        return nums
        