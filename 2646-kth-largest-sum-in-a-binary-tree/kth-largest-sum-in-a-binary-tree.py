from heapq import heapify, heappush, heappop
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        heapify(heap)
        heap_len = 0
        lst = [root]
        result = None
        while lst != []:
            current_level = len(lst)
            temp_sum = 0
            while current_level > 0:
                node = lst.pop(0)
                temp_sum += node.val
                if node.left is not None: lst.append(node.left)
                if node.right is not None: lst.append(node.right)
                current_level -= 1
            if heap_len < k:
                heappush(heap, temp_sum)
                heap_len += 1
            else:
                result = heappop(heap)
                result = max(temp_sum, result)
                heappush(heap, result)
        return -1 if heap_len < k else heappop(heap)
        