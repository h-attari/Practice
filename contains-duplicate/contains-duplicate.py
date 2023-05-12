class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_counts = Counter(nums)
        for num, count in num_counts.items():
            if count > 1:
                return True
        return False