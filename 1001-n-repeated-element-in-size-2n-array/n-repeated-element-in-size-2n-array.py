class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        temp_set = set()
        for num in nums:
            if num in temp_set:
                return num
            temp_set.add(num)
        return -1