# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: return None
        mid_index = len(nums) // 2
        root = TreeNode(nums[mid_index])
        root.left = None if mid_index == 0 else self.sortedArrayToBST(nums[:mid_index])
        root.right = None if mid_index == len(nums)-1 else self.sortedArrayToBST(nums[mid_index+1:])
        return root
