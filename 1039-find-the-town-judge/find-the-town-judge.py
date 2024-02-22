class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        temp_dict = {}
        trusting = set()
        for x, y in trust:
            if y in temp_dict:
                temp_dict[y] += 1
            else:
                temp_dict[y] = 1
            trusting.add(x)
        for key, value in temp_dict.items():
            if value == n - 1 and key not in trusting:
                return key
        return -1
