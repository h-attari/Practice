from collections import namedtuple


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        Range = namedtuple("Range", ["start", "end"])
        def checkBST(node, check_range):
            if node is None: return True
            if node.val not in range(check_range.start, check_range.end):
                return False
            left = checkBST(node.left, Range(check_range.start, node.val))
            right = checkBST(node.right, Range(node.val+1, check_range.end))
            return left and right
        
        limit = 2 ** 31
        return checkBST(root, Range(-limit, limit))
