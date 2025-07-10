class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums)-1
        while first <= last:
            mid = (first + last) // 2
            if nums[mid] < target:
                first = mid + 1
            elif nums[mid] > target:
                last = mid - 1
            else:
                return mid
        return first