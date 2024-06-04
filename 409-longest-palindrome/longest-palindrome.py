class Solution:
    def longestPalindrome(self, s: str) -> int:
        allow_odd = True
        result = 0
        for count in Counter(s).values():
            if (count & 1) == 1:
                if allow_odd:
                    result += 1
                    allow_odd = False
                result += (count - 1)
            else:
                result += count
        return result
        