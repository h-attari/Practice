class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True
        i, j = 0, len(s)-1
        while not (i ==j or i > j):
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                result = False
                break
            i += 1
            j -= 1
        return result
