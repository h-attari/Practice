class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i, j = 0, 0
        cur_white, result = 0, 0
        while j < k:
            if blocks[j] == "W":
                cur_white += 1
            j += 1
        result = cur_white
        j -= 1
        while j < len(blocks)-1:
            if blocks[i] == "W":
                cur_white -= 1
            if blocks[j+1] == "W":
                cur_white += 1
            result = min(result, cur_white)
            i += 1
            j += 1
        return result
        