class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)-1):
            if nums[index] == nums[index+1]:
                nums[index] *= 2
                nums[index+1] = 0
        temp = [num for num in nums if num > 0]
        return temp + ([0] * (len(nums) - len(temp)))
        