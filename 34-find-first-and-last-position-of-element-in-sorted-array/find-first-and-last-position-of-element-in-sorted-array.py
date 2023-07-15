class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = 0, len(nums)-1
        while first <= last:
            mid = (first + last) // 2
            if nums[mid] == target:
                start, end = mid, mid
                while start > 0 and nums[start-1] == target:
                    start -= 1
                while end < len(nums)-1 and nums[end+1] == target:
                    end += 1
                return [start, end]
            if nums[mid] < target:
                first = mid + 1
            else:
                last = mid - 1
        return [-1, -1]