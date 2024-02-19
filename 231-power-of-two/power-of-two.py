class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        count = 0
        while n > 0:
            if (n & 1) > 0:
                count += 1
            if count > 1:
                return False
            n = n >> 1
        return True