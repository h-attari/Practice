"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        
        def traverse(node):
            if node is None:
                return
            nonlocal result
            for child in node.children:
                traverse(child)
            result.append(node.val)
            return
        
        traverse(root)
        return result
        