class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for bit in range(32):
            if n & (1 << bit) != 0:
                result += 1
        return result