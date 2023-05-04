class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_lst = [s for s in magazine]
        for s in ransomNote:
            if s not in magazine_lst:
                return False
            magazine_lst.remove(s)
        return True