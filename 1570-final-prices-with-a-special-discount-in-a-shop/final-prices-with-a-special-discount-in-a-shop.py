class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for index in range(len(prices)):
            for index2 in range(index + 1, len(prices)):
                if prices[index2] <= prices[index]:
                    prices[index] -= prices[index2]
                    break
        return prices
        