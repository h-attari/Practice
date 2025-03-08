class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, left_index = 0, 0
        for right_index in range(1, len(prices)):
            if prices[right_index] < prices[left_index]:
                left_index = right_index
            profit = max(profit, prices[right_index] - prices[left_index])
        return profit