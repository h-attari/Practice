class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = dict()
        for string in strs:
            temp = "".join(sorted(string))
            if temp in anagram_dict.keys():
                anagram_dict[temp].append(string)
            else:
                anagram_dict[temp] = [string]
        return list(anagram_dict.values())
        