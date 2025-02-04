class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        cur_sum = 0
        last_ele = -1
        for num in nums:
            if num > last_ele:
                cur_sum += num
            else:
                cur_sum = num
            result = max(result, cur_sum)
            last_ele = num
        return result
