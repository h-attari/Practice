class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        
        mid_index = (len(nums)) // 2
        if nums[mid_index] == target:
            return mid_index
        if nums[mid_index] < target:
            target_index = self.search(nums[mid_index+1:], target)
            return target_index if target_index == -1 else mid_index + target_index + 1
        return self.search(nums[:mid_index], target)