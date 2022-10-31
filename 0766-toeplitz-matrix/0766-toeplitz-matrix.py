import numpy as np

class Solution:
    def isToeplitzMatrix(self, m: List[List[int]]) -> bool:
        return all(len(set(np.diagonal(m,d)))==1 for d in range(-len(m)+1,len(m[0])))
