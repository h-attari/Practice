class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        joined_words = " ".join(words)
        words_set = set(words)
        result = []
        for word in words:
            if joined_words.count(word) > 1:
                result.append(word)
        return result
        