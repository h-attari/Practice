# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traverse(node, is_left, result):
            if node is None: return result
            if all([node.left is None, node.right is None, is_left is True]):
                result += node.val
                return result
            result = traverse(node.left, True, result)
            result = traverse(node.right, False, result)
            return result
        return traverse(root, False, 0)
        