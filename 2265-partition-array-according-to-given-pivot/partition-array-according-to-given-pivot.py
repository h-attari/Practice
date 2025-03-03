class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return sorted(nums, key=lambda x: 0 if (x == pivot) else ((x - pivot) // abs(x - pivot)))
        