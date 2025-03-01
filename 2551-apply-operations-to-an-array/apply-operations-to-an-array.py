class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        temp = []
        for index in range(len(nums)-1):
            if nums[index] == nums[index+1]:
                nums[index] *= 2
                nums[index+1] = 0
            if nums[index] > 0:
                temp.append(nums[index])
        temp.append(nums[-1])
        return temp + ([0] * (len(nums) - len(temp)))
        