class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i,temp,n=1,1,len(nums)  
        lst=[1]*n   
        for i in range(n): 
            lst[i]=temp 
            temp*=nums[i]   
        temp=1
        for i in range(n-1,-1,-1): 
            lst[i]*=temp 
            temp*=nums[i]
        return lst