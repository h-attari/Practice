class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod_nums = 1
        for num in nums:
            prod_nums *= num
        if prod_nums == 0:
            return 0
        return prod_nums // abs(prod_nums)