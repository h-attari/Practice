from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = 0
        for count in range(1, len(tiles)+1):
            result += len(set(permutations(tiles, count)))
        return result
        