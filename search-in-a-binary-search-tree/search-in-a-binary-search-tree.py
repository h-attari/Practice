# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traverse(node):
            if node is None:
                return None
            if node.val == val:
                return node
            left = traverse(node.left)
            if left is not None:
                return left
            right = traverse(node.right)
            return right
        return traverse(root)
