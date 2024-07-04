# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = head
        while cur_node is not None:
            if cur_node.val == 0:
                cur_node = cur_node.next
                continue
            temp_node = cur_node.next
            while temp_node.val != 0:
                cur_node.val += temp_node.val
                temp_node = temp_node.next
            cur_node.next = temp_node.next
            cur_node = cur_node.next
        return head.next
        