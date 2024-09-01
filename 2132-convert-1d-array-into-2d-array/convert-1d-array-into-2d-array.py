class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != (m * n):
            return []
        result = []
        temp = []
        for num in original:
            temp.append(num)
            if len(temp) == n:
                result.append(temp)
                temp = []
        return result
        