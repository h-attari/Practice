# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        lst = [root]
        while lst != []:
            node = lst.pop(-1)
            if node.val == val:
                return node
            if node.left is not None:
                lst.append(node.left)
            if node.right is not None:
                lst.append(node.right)
        return None
        