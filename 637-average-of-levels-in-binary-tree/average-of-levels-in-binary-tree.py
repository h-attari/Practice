# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None: return []
        temp_queue = [root]
        result = []
        while temp_queue != []:
            level_len = len(temp_queue)
            temp_sum = 0
            for _ in range(level_len):
                node = temp_queue.pop(0)
                if node.left is not None: temp_queue.append(node.left)
                if node.right is not None: temp_queue.append(node.right)
                temp_sum += node.val
            result.append(temp_sum / level_len)
        return result