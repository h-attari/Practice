class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            temp = str(num)
            num = 0
            for digit in temp:
                num += int(digit)
        return num