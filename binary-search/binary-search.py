class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first_index, last_index = 0, len(nums)-1

        while first_index <= last_index:
            mid_index = (first_index + last_index) // 2
            if nums[mid_index] == target:
                return mid_index
            if nums[mid_index] < target:
                first_index = mid_index + 1
            else:
                last_index = mid_index - 1
        
        return -1