class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in ("(", "{", "["):
                stack.append(bracket)
                continue
            if bracket in (")", "}", "]") and stack == []:
                return False
            if bracket == ")":
                if stack[-1] != "(":
                    return False
            else:
                if ord(bracket)-2 != ord(stack[-1]):
                    return False
            stack.pop(-1)
        return stack == [] 
