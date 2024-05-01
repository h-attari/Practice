class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        lst = [char for char in word]
        
        end_index = 0
        while end_index < len(lst) and lst[end_index] != ch:
            end_index += 1
        
        if end_index == len(lst):
            return word
        
        i, j = 0, end_index
        while i < j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
        
        return "".join(lst)
        