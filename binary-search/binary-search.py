class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first_index, last_index = 0, len(nums)-1
        target_index = -1
        while first_index <= last_index:
            mid_index = (first_index + last_index) // 2
            if nums[mid_index] == target:
                target_index = mid_index
                break
            elif nums[mid_index] < target:
                first_index = mid_index + 1
            elif nums[mid_index] > target:
                last_index = mid_index - 1
        return target_index