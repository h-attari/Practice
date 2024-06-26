# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def traverse(node):
            if node.left is None and node.right is None:
                return True if node.val == 1 else False
            left = traverse(node.left)
            right = traverse(node.right)
            if node.val == 2:
                return left or right
            return left and right
        return traverse(root)
        