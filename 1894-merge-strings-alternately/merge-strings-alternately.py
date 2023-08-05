class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        index = 0
        while index < min(len(word1), len(word2)):
            result += (word1[index] + word2[index])
            index += 1
        if len(word2) < len(word1):
            result += word1[index:]
        elif len(word2) > len(word1):
            result += word2[index:]
        return result