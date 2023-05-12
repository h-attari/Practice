class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m,temp=nums[0],nums[0]
        for x in range(1,len(nums)):
            temp=max(nums[x],temp+nums[x])
            m=max(temp,m)
        return m