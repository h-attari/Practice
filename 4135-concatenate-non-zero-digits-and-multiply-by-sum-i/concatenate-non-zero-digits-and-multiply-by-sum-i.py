class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x, num_sum = 0, 0
        for digit in str(n):
            digit = int(digit)
            if digit > 0:
                x = (x * 10) + digit
                num_sum += digit
        return x * num_sum
        