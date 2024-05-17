# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def traverse(node):
            if node is None: return None
            node.left = traverse(node.left)
            node.right = traverse(node.right)
            if all([node.left is None, node.right is None, node.val == target]):
                return None
            return node
        
        result = traverse(root)
        return result