class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in ("(", "[", "{"):
                stack.append(x)
            else:
                if not stack:
                    return False
                if x == ")" and stack[-1] == "(":
                    stack.pop(-1)
                elif x == "]" and stack[-1] == "[":
                    stack.pop(-1)
                elif x == "}" and stack[-1] == "{":
                    stack.pop(-1)
                else:
                    return False
        return stack == []
