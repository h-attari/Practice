class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums)-1
        while i < j:
            pos, neg = nums[j], nums[i] * (-1)
            if pos == neg:
                return pos
            if pos > neg:
                j -= 1
            else:
                i += 1
        return -1
        