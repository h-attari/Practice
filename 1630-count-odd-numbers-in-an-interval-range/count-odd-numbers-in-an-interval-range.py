class Solution:
    def countOdds(self, low: int, high: int) -> int:
        buffer = 0 if low%2==0 and high%2==0 else 1
        return (high - low) // 2 + buffer