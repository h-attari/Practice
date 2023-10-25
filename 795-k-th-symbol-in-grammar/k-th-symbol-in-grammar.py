class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        k, n = k-1, n-1
        def get_answer(row, col):
            if col == 0: return 0
            if col%2 == 0: return get_answer(row-1, col//2)
            else: return 1 - get_answer(row-1, col//2)
        result = get_answer(n, k)
        return result