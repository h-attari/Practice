class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        temp_set = set()
        for num in nums:
            if num in temp_set:
                temp_set.remove(num)
            else:
                temp_set.add(num)
        return list(temp_set)
        