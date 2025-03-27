class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index_a, index_b = 0, 0
        while index_a < len(s) and index_b < len(t):
            if s[index_a] == t[index_b]:
                index_a += 1
            index_b += 1
        return True if index_a == len(s) else False
        