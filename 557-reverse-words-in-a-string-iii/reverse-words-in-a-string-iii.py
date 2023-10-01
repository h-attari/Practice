class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(" ")
        for index in range(len(lst)):
            lst[index] = lst[index][::-1]
        return " ".join(lst)