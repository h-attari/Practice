class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = ""
        for word in words:
            temp_sum = 0
            for char in word:
                temp_sum += weights[ord(char) - 97]
            result += (chr(122 - (temp_sum % 26)))
        return result