ROMAN_VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        for x in s[::-1]:
            temp = ROMAN_VALUES[x]
            if 4 * temp < num: num -= temp
            else: num += temp
        return num