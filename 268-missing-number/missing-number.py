class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            while nums[index] < len(nums) and nums[index] != index:
                temp = nums[index]
                nums[index], nums[temp] = nums[temp], temp
        
        for index in range(len(nums)):
            if nums[index] != index:
                return index
        
        return len(nums)
        