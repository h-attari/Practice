class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = None
        for index in range(1, len(nums)):
            if nums[index] == nums[index-1]:
                continue
            if increasing is None:
                if nums[index] > nums[index-1]:
                    increasing = True
                else:
                    increasing = False
            else:
                if nums[index] > nums[index-1] and increasing is False:
                    return False
                elif nums[index] < nums[index-1] and increasing is True:
                    return False
        return True