class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp_set = set(nums)
        for num in temp_set:
            if nums.count(num) == 1:
                return num
