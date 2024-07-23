from collections import Counter
from functools import cmp_to_key

class Solution:
    def comparator(a, b):
        global temp
        if temp[a] < temp[b]:
            return -1
        elif temp[b] < temp[a]:
            return 1
        else:
            if a < b:
                return 1
            else:
                return -1
    
    def frequencySort(self, nums: List[int]) -> List[int]:
        global temp
        temp = Counter(nums)
        return sorted(nums, key=cmp_to_key(Solution.comparator))