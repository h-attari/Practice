class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp_set = set()
        result = None
        for num in nums:
            if num in temp_set:
                result = num
                break
            temp_set.add(num)
        return result
