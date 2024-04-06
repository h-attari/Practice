class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removing_queue = []
        
        for index, char in enumerate(s):
            if char == "(":
                stack.append((index, char))
            elif char == ")":
                if stack and stack[-1][1] == "(":
                    stack.pop(-1)
                else:
                    removing_queue.append((index, char))
        removing_queue += stack
        removing_queue = sorted(removing_queue, key=lambda x: x[0])

        result = ""
        removing_index = 0
        for index, char in enumerate(s):
            if (removing_index < len(removing_queue)) and (index == removing_queue[removing_index][0]):
                removing_index += 1
                continue
            result += char
        
        return result
        