class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        temp_str = s[:len(s)//2]
        while temp_str:
            temp_result = temp_str * (len(s)//len(temp_str))
            if temp_result == s:
                return True
            temp_str = temp_str[:len(temp_str)-1]
        return False