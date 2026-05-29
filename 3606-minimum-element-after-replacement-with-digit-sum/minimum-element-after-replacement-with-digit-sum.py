class Solution:
    def get_sum(self, num):
        if num == 0: return num
        return (num % 10) + self.get_sum(num // 10)
    
    def minElement(self, nums: List[int]) -> int:
        min_ele = float("inf")
        for num in nums:
            digits_sum = self.get_sum(num)
            min_ele = min(digits_sum, min_ele)
        return min_ele
        