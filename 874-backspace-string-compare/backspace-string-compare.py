class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s, new_t = [], []
        for char in s:
            if char == "#":
                if len(new_s) == 0:
                    continue
                new_s.pop(-1)
            else:
                new_s.append(char)
        for char in t:
            if char == "#":
                if len(new_t) == 0:
                    continue
                new_t.pop(-1)
            else:
                new_t.append(char)
        return new_s == new_t