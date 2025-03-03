class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums)-1
        switches = 0
        while i <= j:
            if nums[j] == val:
                switches += 1
                j -= 1
                continue
            if nums[i] == val:
                switches += 1
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            i += 1
        return len(nums) - switches
        