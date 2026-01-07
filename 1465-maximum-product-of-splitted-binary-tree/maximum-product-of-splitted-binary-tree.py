# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def getTotal(node):
            val = node.val
            if node.left:
                val += getTotal(node.left)
            if node.right:
                val += getTotal(node.right)
            return val

        total = getTotal(root)
        output = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            s1 = (total - left) * left
            s2 = (total - right) * right
            nonlocal output
            output = max(output, s1, s2)
            
            return node.val + left + right

        dfs(root)
        return output % (10 ** 9 + 7)