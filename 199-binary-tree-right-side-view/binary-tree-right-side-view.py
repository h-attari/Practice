# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        temp_queue = [root]
        result = []
        while temp_queue != []:
            result.append(temp_queue[0].val)
            level_count = len(temp_queue)
            for _ in range(level_count):
                node = temp_queue.pop(0)
                if node.right is not None: temp_queue.append(node.right)
                if node.left is not None: temp_queue.append(node.left)
        return result
        