# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        queue = deque([root])
        leftmost = None

        while queue:
            leftmost = queue.popleft()

            if leftmost.right:
                queue.append(leftmost.right)
            if leftmost.left:
                queue.append(leftmost.left)

        return leftmost.val