class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = Counter(s)
        for index in range(len(s)):
            if char_count[s[index]] == 1:
                return index
        return -1