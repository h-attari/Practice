class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        left = 1
        right = max(candies)
        result = 0
        while left<=right:
            mid = (left+right)//2
            if sum(candy // mid for candy in candies) >= k:
                result = mid
                left = mid+1
            else:
                right = mid-1
        return result