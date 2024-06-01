class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        for i, j in zip(range(len(s)-1), range(1, len(s))):
            result += abs(ord(s[i]) - ord(s[j]))
        return result
        