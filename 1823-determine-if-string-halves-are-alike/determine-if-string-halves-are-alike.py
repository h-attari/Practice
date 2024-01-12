class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a_count, b_count = 0, 0
        s_len = len(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for char in s[:s_len//2]:
            if char in vowels:
                a_count += 1
        for char in s[s_len//2:]:
            if char in vowels:
                b_count += 1
        return a_count == b_count