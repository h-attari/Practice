class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0     
        ans=len(nums)+1 
        s=0    
        for r in range(len(nums)):  
            s+=nums[r]  
            if s>=target:  
                ans=min(ans,r-l+1)  
            while s>target: 
                s-=nums[l]
                l+=1
                if s>=target:
                    ans=min(ans,r-l+1)  
        return ans if ans<len(nums)+1 else 0