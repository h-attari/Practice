# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 1:  # base case
            return [TreeNode()]
        return [TreeNode(left = subTree1, right = subTree2) 
                for i in range(1, n-1) 
                for subTree1 in self.allPossibleFBT(i) 
                for subTree2 in self.allPossibleFBT(n-1-i)]