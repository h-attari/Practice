class Solution:
    @staticmethod
    def is_prefix_suffix(word1: str, word2: str) -> bool:
        return True if (word2.startswith(word1) and word2.endswith(word1)) else False
    
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                result += int(Solution.is_prefix_suffix(words[i], words[j]))
        return result
        