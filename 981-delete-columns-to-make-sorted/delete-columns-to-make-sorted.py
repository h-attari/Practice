class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        lst = []
        index = 0
        while index < len(strs[0]):
            temp = []
            for string in strs:
                temp.append(string[index])
            lst.append(temp)
            index += 1
        count = 0
        for col in lst:
            if col != sorted(col):
                count += 1
        return count
