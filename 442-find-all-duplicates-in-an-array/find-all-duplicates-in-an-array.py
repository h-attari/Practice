class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        temp_set = set()
        for num in nums:
            if num in temp_set:
                result.append(num)
            temp_set.add(num)
        return result