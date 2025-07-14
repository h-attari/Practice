class Solution:
    def search_first(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        result = -1
        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] == target:
                result = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return result
    
    def search_last(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        result = -1
        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] == target:
                result = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return result
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [
            self.search_first(nums, target),
            self.search_last(nums, target)
        ]
        