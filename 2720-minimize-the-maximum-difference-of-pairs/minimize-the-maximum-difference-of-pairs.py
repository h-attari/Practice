class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        def can_form_pairs(mid): 
            count = 0 
            i = 0 
            while i < len(nums) - 1 and count < p: 
                if nums[i+1] - nums[i] <= mid: 
                    count += 1 
                    i += 2 
                else: 
                    i += 1 
            return count == p 

        nums.sort() 
        low, high = 0, nums[-1] - nums[0] 

        while low < high: 
            mid = (low + high) // 2 
            if can_form_pairs(mid): 
                high = mid 
            else: 
                low = mid + 1 

        return low 