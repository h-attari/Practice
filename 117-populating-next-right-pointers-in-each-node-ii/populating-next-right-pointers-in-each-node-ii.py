"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: return root
        temp_queue = [root]
        while temp_queue != []:
            level_len = len(temp_queue)
            while level_len > 0:
                node = temp_queue.pop(0)
                if node.left is not None: temp_queue.append(node.left)
                if node.right is not None: temp_queue.append(node.right)
                level_len -= 1
                if level_len == 0:
                    node.next = None
                else:
                    node.next = temp_queue[0]
        return root
        