class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        str_index, space_index = 0, 0
        while str_index < len(s):
            if space_index < len(spaces) and str_index == spaces[space_index]:
                result += " "
                space_index += 1
            else:
                result += s[str_index]
                str_index += 1
        return result
        