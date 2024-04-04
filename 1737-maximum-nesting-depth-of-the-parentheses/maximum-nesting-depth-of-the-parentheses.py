class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth, cur_depth = 0, 0
        for char in s:
            if char not in ("(", ")"):
                continue
            if char == "(":
                cur_depth += 1
            else:
                max_depth = max(max_depth, cur_depth)
                cur_depth -= 1
        return max_depth
        