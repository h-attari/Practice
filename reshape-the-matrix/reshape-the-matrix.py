class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if (len(mat) * len(mat[0])) != (r * c):
            return mat
        result_mat = []
        col_counter = 0
        temp = []
        for row in mat:
            for col in row:
                temp.append(col)
                col_counter += 1
                if col_counter == c:
                    result_mat.append(temp)
                    temp = []
                    col_counter = 0
        return result_mat