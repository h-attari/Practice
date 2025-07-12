class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + ((high - low) // 2)
            if mid == 0 and (nums[mid] > nums[mid+1]):
                return mid
            if mid == (len(nums)-1) and (nums[mid] > nums[mid-1]):
                return mid
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            if nums[mid+1] > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        