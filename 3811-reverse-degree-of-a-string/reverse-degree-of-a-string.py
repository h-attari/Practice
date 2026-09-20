class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        index = 1
        for char in s:
            result += ((26 - (ord(char) - 97)) * index)
            index += 1
        return result