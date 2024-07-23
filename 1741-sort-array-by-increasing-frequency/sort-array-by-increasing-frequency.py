from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        temp = Counter(nums)
        return sorted(nums, key=lambda x: (temp[x], -x))