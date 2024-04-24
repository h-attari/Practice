class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        a, b, c, d = 0, 1, 1, 1
        for _ in range(2, n):
            d = a + b + c
            a = b
            b = c
            c = d
        return c
        