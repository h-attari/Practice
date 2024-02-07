class Solution:
    def frequencySort(self, s: str) -> str:
        temp_dict = dict()
        for char in s:
            if ord(char) in temp_dict:
                temp_dict[ord(char)] += 1
            else:
                temp_dict[ord(char)] = 1
        temp_dict = sorted(temp_dict.items(), key=lambda x:x[1], reverse=True)
        result = ""
        for item in temp_dict:
            for x in range(item[1]):
                result += chr(item[0])
        return result