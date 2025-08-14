from functools import cache
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        # Avoid unnecessary computation for edge case
        if k == 0 or n == 0:
            return 0

        # Precompute profitable moves from i to j
        options = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i+1, n):
                if prices[j] > prices[i]:
                    options[i].append((prices[j] - prices[i], j))

        @cache
        def f(i: int, k: int) -> int:
            if k == 0 or i >= n:
                return 0

            ans = f(i + 1, k)  # Option to skip this day entirely

            for profit, j in options[i]:
                ans = max(ans, profit + f(j, k - 1))  # Make a transaction

            return ans

        return f(0, k)