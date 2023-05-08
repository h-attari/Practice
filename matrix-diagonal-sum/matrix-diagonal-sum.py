class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        first, last = 0, len(mat[0])-1
        diag_sum = 0
        for row in mat:
            if first == last:
                diag_sum += row[first]
            else:
                diag_sum += (row[first] + row[last])
            first += 1
            last -= 1
        return diag_sum