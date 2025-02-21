# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def recover(self, node):
        if node is None: return
        if node.val == -1: node.val = 0
        if node.left is not None:
            node.left.val = (2 * node.val) + 1
            self.numbers.add((2 * node.val) + 1)
        if node.right is not None:
            node.right.val = (2 * node.val) + 2
            self.numbers.add((2 * node.val) + 2)
        self.recover(node.left)
        self.recover(node.right)
        return

    
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.numbers = {0}
        self.recover(self.root)
        

    def find(self, target: int) -> bool:
        return target in self.numbers
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)