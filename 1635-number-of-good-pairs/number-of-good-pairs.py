class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        for index1 in range(len(nums)-1):
            for index2 in range(index1+1, len(nums)):
                if nums[index1] == nums[index2]:
                    result += 1
        return result