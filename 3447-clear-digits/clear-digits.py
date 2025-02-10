class Solution:
    def clearDigits(self, s: str) -> str:
        temp_stack = []
        for char in s:
            if char.isdigit() is True:
                if len(temp_stack) > 0:
                    temp_stack.pop(-1)
                continue
            temp_stack.append(char)
        return "".join(temp_stack)
        