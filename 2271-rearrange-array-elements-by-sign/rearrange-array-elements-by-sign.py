class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [None] * len(nums)
        p_index, n_index = 0, 1
        for num in nums:
            if num < 0:
                result[n_index] = num
                n_index += 2
            else:
                result[p_index] = num
                p_index += 2
        return result
        